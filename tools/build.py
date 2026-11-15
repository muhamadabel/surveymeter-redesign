#!/usr/bin/env python3
"""Build the static SurveyMETER site into the repo root.

Inputs:  content/site.json (migrated from the old Drupal site), content/home_en.json,
         templates/home.html.
Output:  index.html, en/index.html and one folder per page (pretty URLs), plus
         search-index-*.json and sitemap.xml. Only the Python standard library is used.

Run:     python3 tools/build.py
"""
import html
import json
import os
import re
import shutil
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_URL = 'https://surveymeter.org'
OLD = 'https://www.surveymeter.org'
ASSET_V = '14'
NEWS_PER_PAGE = 18

site = json.load(open(os.path.join(ROOT, 'content/site.json'), encoding='utf-8'))
HOME_EN = json.load(open(os.path.join(ROOT, 'content/home_en.json'), encoding='utf-8'))
IMAGES = {}
img_map = os.path.join(ROOT, 'content/images.json')
if os.path.exists(img_map):
    IMAGES = json.load(open(img_map, encoding='utf-8'))

esc = html.escape
OTHER = {'id': 'en', 'en': 'id'}
PUB_LISTS = ('all_pubs', 'working_paper', 'policy_brief', 'book', 'article', 'research_report', 'annual_report')
DOWNLOADS = {}   # old post path -> download URL (books link to Google Drive)
SKIPPED = {'id': 0, 'en': 0}


def find_post(lang, item):
    """(post, language whose page exists) for a list item, or (None, None) when the old page was broken."""
    p = item['path']
    if p in site[lang]['posts']:
        return site[lang]['posts'][p], lang
    o = OTHER[lang]
    if p in site[o]['posts']:
        return site[o]['posts'][p], o
    swapped = re.sub(r'^/(id|en)/', f'/{lang}/', p)
    if swapped in site[lang]['posts']:
        return site[lang]['posts'][swapped], lang
    return None, None


def prepare():
    for lang in ('id', 'en'):
        L = site[lang]
        # "Semua publikasi" has pages that always fail on the old server: rebuild it from every publication list.
        seen, merged = set(), []
        for k in PUB_LISTS:
            for it in L['lists'].get(k, {}).get('items', []):
                if it['path'] not in seen:
                    seen.add(it['path'])
                    merged.append(it)
        L['lists'].setdefault('all_pubs', {'intro': '', 'items': []})['items'] = merged
    for lang in ('id', 'en'):
        L, O = site[lang], site[OTHER[lang]]
        for k, lst in L['lists'].items():
            if not lst['items'] and O['lists'].get(k, {}).get('items'):
                lst['items'] = list(O['lists'][k]['items'])
                lst['intro'] = lst.get('intro') or ''
        for k in ('ifls_east', 'star', 'ilas'):
            if not L['data'].get(k) and O['data'].get(k):
                L['data'][k] = O['data'][k]
        for k, lst in L['lists'].items():
            kept = []
            for it in lst['items']:
                if it.get('download'):
                    DOWNLOADS[it['path']] = it['download']
                if find_post(lang, it)[0]:
                    kept.append(it)
                else:
                    SKIPPED[lang] += 1
            lst['items'] = kept


prepare()

# ---------------------------------------------------------------- navigation
# (key, title id, title en, path) ; path is relative to the language root.
MENU = [
    ('about', 'Tentang', 'About', [
        ('Tentang kami', 'About us', [
            ('scope', 'Sasaran dan lingkup kegiatan', 'Target and scope of activities', 'tentang/sasaran'),
            ('partners', 'Mitra kerja dan klien', 'Partners and clients', 'tentang/mitra'),
        ]),
        ('Profil', 'Profile', [
            ('profile', 'Profil lembaga', 'Institutional profile', 'tentang/profil'),
            ('staff', 'Struktur organisasi', 'Organizational structure', 'tentang/struktur'),
            ('vision', 'Visi dan misi', 'Vision and mission', 'tentang/visi-misi'),
            ('ability', 'Kemampuan dan pengalaman', 'Ability and experience', 'tentang/kemampuan'),
        ]),
    ]),
    ('activities', 'Kegiatan', 'Activities', [
        ('Survei', 'Survey', [
            ('impact', 'Studi evaluasi dampak', 'Impact evaluation study', 'kegiatan/evaluasi-dampak'),
            ('policy', 'Studi berorientasi kebijakan', 'Policy-based study', 'kegiatan/studi-kebijakan'),
        ]),
        ('Pelatihan dan pengembangan', 'Training and development', [
            ('assistance', 'Pendampingan', 'Assistance', 'kegiatan/pendampingan'),
            ('training', 'Pelatihan', 'Training', 'kegiatan/pelatihan'),
        ]),
        ('Riset', 'Research', [
            ('knowledge', 'Pengelolaan pengetahuan', 'Knowledge management', 'kegiatan/pengelolaan-pengetahuan'),
            ('scientific', 'Penelitian ilmiah', 'Scientific research', 'kegiatan/penelitian-ilmiah'),
            ('study', 'Kajian', 'Study', 'kegiatan/kajian'),
        ]),
    ]),
    ('pubs', 'Publikasi', 'Publication', [
        ('Publikasi', 'Publications', [
            ('all_pubs', 'Semua publikasi', 'All publications', 'publikasi'),
            ('working_paper', 'Working paper', 'Working paper', 'publikasi/working-paper'),
            ('policy_brief', 'Policy brief', 'Policy brief', 'publikasi/policy-brief'),
            ('book', 'Buku', 'Book', 'publikasi/buku'),
            ('article', 'Artikel', 'Article', 'publikasi/artikel'),
            ('research_report', 'Laporan penelitian', 'Research report', 'publikasi/laporan-penelitian'),
            ('annual_report', 'Laporan tahunan', 'Annual report', 'publikasi/laporan-tahunan'),
        ]),
        ('Data publik', 'Public data', [
            ('ifls_east', 'Sakertim (IFLS East)', 'Sakertim (IFLS East)', 'data/ifls-east'),
            ('star', 'STAR', 'STAR', 'data/star'),
            ('ilas', 'ILAS 2023', 'ILAS 2023', 'data/ilas'),
        ]),
    ]),
    ('wg', 'Kelompok kerja', 'Working group', [
        ('Lansia', 'Aging', [
            ('aging_survey', 'Survei', 'Survey', 'kelompok-kerja/lansia/survei'),
            ('aging_assistance', 'Pendampingan', 'Assistance', 'kelompok-kerja/lansia/pendampingan'),
            ('aging_pubs', 'Publikasi', 'Publication', 'kelompok-kerja/lansia/publikasi'),
        ]),
        ('Stunting', 'Stunting', [
            ('stunting_survey', 'Survei', 'Survey', 'kelompok-kerja/stunting/survei'),
            ('assistance', 'Pendampingan', 'Assistance', 'kegiatan/pendampingan'),
            ('stunting_pubs', 'Publikasi', 'Publication', 'kelompok-kerja/stunting/publikasi'),
        ]),
        ('Proyek percontohan', 'Pilot project', [
            ('silani', 'SILANI', 'SILANI', 'kelompok-kerja/silani'),
            ('ltc', 'LTC (perawatan jangka panjang)', 'LTC (long-term care)', 'kelompok-kerja/ltc'),
        ]),
    ]),
    ('career', 'Karir', 'Career', [
        ('Lowongan', 'Vacancies', [
            (f'career_{y}', str(y), str(y), f'karir/{y}') for y in range(2024, 2018, -1)
        ]),
    ]),
]

PAGES = {}       # key -> dict(title_id, title_en, path, group_key, column)
for top_key, tid, ten, cols in MENU:
    for col_id, col_en, links in cols:
        for key, lid, len_, path in links:
            PAGES.setdefault(key, {'id': lid, 'en': len_, 'path': path, 'top': top_key,
                                   'top_id': tid, 'top_en': ten, 'col_id': col_id, 'col_en': col_en})
PAGES['news'] = {'id': 'Berita', 'en': 'News', 'path': 'berita', 'top': 'news', 'top_id': 'Berita',
                 'top_en': 'News', 'col_id': '', 'col_en': ''}
PAGES['contact'] = {'id': 'Kontak', 'en': 'Contact', 'path': 'kontak', 'top': 'contact', 'top_id': 'Kontak',
                    'top_en': 'Contact', 'col_id': '', 'col_en': ''}
PAGES['search'] = {'id': 'Cari', 'en': 'Search', 'path': 'cari', 'top': 'search', 'top_id': 'Cari',
                   'top_en': 'Search', 'col_id': '', 'col_en': ''}

UI = {
    'id': {
        'skip': 'Langsung ke konten', 'home': 'Beranda', 'menu': 'Menu', 'contact_cta': 'Hubungi kami',
        'search': 'Cari', 'read': 'Baca', 'latest': 'Berita terbaru', 'in_section': 'Di bagian ini',
        'all_news': 'Semua berita', 'prev': 'Sebelumnya', 'next': 'Berikutnya', 'page': 'Halaman',
        'of': 'dari', 'items': 'tulisan', 'empty': 'Belum ada tulisan di bagian ini.',
        'date': 'Tanggal', 'type': 'Tipe', 'author': 'Penulis', 'keywords': 'Kata kunci', 'location': 'Lokasi',
        'source': 'Sumber asli', 'back': 'Kembali ke', 'related': 'Tulisan lain di bagian ini',
        'search_label': 'Cari berita, publikasi, atau kegiatan', 'search_ph': 'Contoh: lansia, stunting, IFLS',
        'search_none': 'Tidak ada hasil untuk', 'search_count': 'hasil',
        'footer_about': 'Survey, Measurement, Training, and Research. Lembaga survei, pelatihan, dan penelitian sejak 2002.',
        'footer_legal': 'Yayasan dikukuhkan dengan akta notaris 2009, tercatat di Kemenkumham RI. PT SurveyMETER sejak 2020.',
        'addr_short': 'Jl. Jenengan Raya No. 109, Sleman, Yogyakarta', 'lang_label': 'Bahasa',
        'download': 'Unduh', 'download_pdf': 'Unduh dokumen',
        'nf_title': 'Halaman tidak ditemukan', 'nf_text': 'Alamat ini tidak ada di situs SurveyMETER. Coba menu di atas atau halaman pencarian.',
    },
    'en': {
        'skip': 'Skip to content', 'home': 'Home', 'menu': 'Menu', 'contact_cta': 'Contact us',
        'search': 'Search', 'read': 'Read', 'latest': 'Latest news', 'in_section': 'In this section',
        'all_news': 'All news', 'prev': 'Previous', 'next': 'Next', 'page': 'Page',
        'of': 'of', 'items': 'items', 'empty': 'Nothing has been posted in this section yet.',
        'date': 'Date', 'type': 'Type', 'author': 'Author', 'keywords': 'Keywords', 'location': 'Location',
        'source': 'Original page', 'back': 'Back to', 'related': 'More in this section',
        'search_label': 'Search news, publications, or activities', 'search_ph': 'e.g. ageing, stunting, IFLS',
        'search_none': 'No results for', 'search_count': 'results',
        'footer_about': 'Survey, Measurement, Training, and Research. A survey, training, and research institute since 2002.',
        'footer_legal': 'Foundation established by notarial deed in 2009, registered with the Ministry of Law and Human Rights. PT SurveyMETER since 2020.',
        'addr_short': 'Jl. Jenengan Raya No. 109, Sleman, Yogyakarta', 'lang_label': 'Language',
        'download': 'Download', 'download_pdf': 'Download the document',
        'nf_title': 'Page not found', 'nf_text': 'This address does not exist on the SurveyMETER site. Try the menu above or the search page.',
    },
}

MONTHS = {
    'id': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'],
    'en': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
}
MONTH_NAMES = {'januari': 1, 'februari': 2, 'maret': 3, 'april': 4, 'mei': 5, 'juni': 6, 'juli': 7,
               'agustus': 8, 'september': 9, 'oktober': 10, 'november': 11, 'desember': 12,
               'january': 1, 'february': 2, 'march': 3, 'may': 5, 'june': 6, 'july': 7, 'august': 8,
               'october': 10, 'december': 12}


def url(lang, path=''):
    base = '/en/' if lang == 'en' else '/'
    return base + (path.strip('/') + '/' if path else '')


def iso_date(raw):
    """Return YYYY-MM-DD (or YYYY-MM) from the old site's date strings, or ''."""
    if not raw:
        return ''
    m = re.search(r'(\d{2})/(\d{2})/(\d{4})', raw)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        if b > 12 and a <= 12:  # month/day order on a few English pages
            a, b = b, a
        if 1 <= b <= 12 and 1 <= a <= 31:
            return f'{m.group(3)}-{b:02d}-{a:02d}'
    m = re.search(r'(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})', raw)
    if m and m.group(2).lower() in MONTH_NAMES:
        return f'{m.group(3)}-{MONTH_NAMES[m.group(2).lower()]:02d}-{int(m.group(1)):02d}'
    m = re.search(r'([A-Za-z]+)\s+(\d{4})', raw)
    if m and m.group(1).lower() in MONTH_NAMES:
        return f'{m.group(2)}-{MONTH_NAMES[m.group(1).lower()]:02d}'
    return ''


def human_date(iso, lang):
    if not iso:
        return ''
    parts = iso.split('-')
    y, mo = parts[0], int(parts[1])
    if len(parts) == 3:
        return f'{int(parts[2])} {MONTHS[lang][mo - 1]} {y}'
    return f'{MONTHS[lang][mo - 1]} {y}'


def slug_for(old_path):
    p = old_path.split('?')[0].strip('/').split('/')
    rest = p[2:] if len(p) > 2 else p[-1:]
    if p[1] in ('read', 'acara', 'berita', 'kajian') and len(rest) >= 2:
        s = f'{rest[0]}-{rest[1]}'
    elif p[1] == 'node':
        s = f'node-{rest[0]}'
    else:
        s = '-'.join(rest)
    s = urllib.parse.unquote(s).lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s[:90].rstrip('-') or 'tulisan'


def post_path(lang, old_path):
    return ('read/' if lang == 'en' else 'baca/') + slug_for(old_path)


def img(src):
    """Local copy of an old-site image; '' when it was never downloadable (dead on the old site)."""
    if not src:
        return ''
    if src in IMAGES:
        return IMAGES[src]
    return '' if 'surveymeter.org' in src else src


OLD_SECTION = {}  # old list path (no lang) -> page key
for k, p in {
    'impact': 'Studi%20Evaluasi%20Dampak', 'policy': 'Studi%20Berorientasi%20Kebijakan', 'assistance': 'pendampingan',
    'training': 'acara', 'knowledge': 'pengelola_pengetahuan', 'scientific': 'penelitian_ilmiah', 'study': 'kajian',
    'all_pubs': 'semua_publikasi', 'working_paper': 'working_paper', 'policy_brief': 'policy_brief', 'book': 'buku_k',
    'article': 'artikel', 'research_report': 'laporan_penelitian', 'annual_report': 'laporan', 'aging_survey': 'aging_survei',
    'aging_assistance': 'aging_pendampingan', 'aging_pubs': 'aging_publikasi', 'stunting_survey': 'stunting_survei',
    'stunting_pubs': 'stunting_publikasi', 'silani': 'silani', 'ltc': 'ltc', 'news': 'berita',
    'career_2024': 'karir2024', 'career_2023': 'karir2023', 'career_2022': 'karir2022', 'career_2021': 'karir2021',
    'career_2020': 'karir2020', 'career_2019': 'karir2019', 'profile': 'node/62', 'vision': 'node/61',
    'partners': 'node/513', 'staff': 'node/524', 'scope': 'node/65', 'ability': 'node/64', 'search': 'search',
}.items():
    OLD_SECTION[urllib.parse.unquote(p).lower()] = k
OLD_SECTION['staff'] = 'staff'
DATA_OLD = {'research/3/iflseast': 'ifls_east',
            'research/4/the-study-of-the-tsunami-aftermath-and-recovery-star': 'star',
            'post/indonesia-longitudinal-aging-survey-ilas-2023': 'ilas'}


def rewrite_href(href, lang):
    """Map an old-site link to the new page when one exists."""
    if not href:
        return href
    u = urllib.parse.urlparse(href)
    if u.netloc and 'surveymeter.org' not in u.netloc:
        return href
    path = u.path.replace('/index.php', '')
    m = re.match(r'^/(id|en)/(.*)$', path)
    rest = (m.group(2) if m else path.lstrip('/')).rstrip('/')
    low = urllib.parse.unquote(rest).lower()
    if low in DATA_OLD:
        return url(lang, PAGES[DATA_OLD[low]]['path'])
    if low in OLD_SECTION:
        return url(lang, PAGES[OLD_SECTION[low]]['path'])
    if low in ('', 'data_publik'):
        return url(lang, 'data/ilas') if low else url(lang)
    for l2 in (lang, 'id', 'en'):
        cand = f'/{l2}/{rest}'
        if cand in site[l2]['posts']:
            return url(l2, post_path(l2, cand))
    if href.startswith('/'):
        return OLD + href
    return href


def rewrite_body(body, lang):
    body = re.sub(r'href="([^"]*)"', lambda m: 'href="%s"' % esc(rewrite_href(html.unescape(m.group(1)), lang)), body)
    body = re.sub(r'<img [^>]*src="([^"]*)"[^>]*>',
                  lambda m: m.group(0) if img(html.unescape(m.group(1))) else '', body)
    body = re.sub(r'src="([^"]*)"', lambda m: 'src="%s"' % esc(img(html.unescape(m.group(1)))), body)
    body = re.sub(r'<img ', '<img loading="lazy" ', body)
    body = re.sub(r'href="(https?://(?!surveymeter\.org|www\.surveymeter\.org)[^"]*)"',
                  r'href="\1" target="_blank" rel="noopener"', body)
    return body


# ---------------------------------------------------------------- layout
def mega_menu(lang, current_top):
    t = 'id' if lang == 'id' else 'en'
    out = []
    for top_key, tid, ten, cols in MENU:
        label = tid if t == 'id' else ten
        cls = ' is-current' if top_key == current_top else ''
        panel_cols = []
        for col_id, col_en, links in cols:
            lis = ''.join(
                f'<li><a href="{url(lang, p)}">{esc(lid if t == "id" else len_)}</a></li>'
                for key, lid, len_, p in links)
            panel_cols.append(f'<div class="mega__col"><p class="mega__head">{esc(col_id if t == "id" else col_en)}</p><ul>{lis}</ul></div>')
        out.append(
            f'<li class="menu__item{cls}">'
            f'<button type="button" class="menu__btn" aria-expanded="false" aria-controls="mega-{top_key}">{esc(label)}</button>'
            f'<div class="mega" id="mega-{top_key}" hidden><div class="mega__inner">{"".join(panel_cols)}</div></div></li>')
    news_cls = ' is-current' if current_top == 'news' else ''
    out.append(f'<li class="menu__item{news_cls}"><a class="menu__link" href="{url(lang, "berita")}">{"Berita" if t == "id" else "News"}</a></li>')
    return ''.join(out)


def layout(lang, title, body, *, current_top='', alt_path='', desc='', page_class='', self_path=None):
    u = UI[lang]
    other = 'en' if lang == 'id' else 'id'
    # alt_path: this page in the other language; self_path: this page in its own language.
    paths = {lang: alt_path if self_path is None else self_path, other: alt_path}
    alt = url(other, paths[other])
    home_title = ('SurveyMETER | Survei, pengukuran, pelatihan, dan penelitian' if lang == 'id'
                  else 'SurveyMETER | Survey, measurement, training, and research')
    full_title = f'{title} | SurveyMETER' if title else home_title
    desc = desc or ('Lembaga survei, pelatihan, dan penelitian di Yogyakarta sejak 2002.' if lang == 'id'
                    else 'A survey, training, and research institute in Yogyakarta since 2002.')
    canonical = SITE_URL + url(lang, paths[lang])
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(full_title)}</title>
  <meta name="description" content="{esc(desc[:160])}">
  <meta name="theme-color" content="#0A3322">
  <link rel="canonical" href="{esc(canonical)}">
  <link rel="alternate" hreflang="{other}" href="{esc(SITE_URL + alt)}">
  <link rel="icon" href="/assets/img/surveymeter-logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/styles.css?v={ASSET_V}">
</head>
<body class="{page_class}">
  <a class="skip-link" href="#main">{u['skip']}</a>
  <div class="topbar">
    <div class="container topbar__inner">
      <p class="topbar__info">
        <span>{u['addr_short']}</span>
        <a href="tel:+622744477464">+62 274 4477-464</a>
        <a href="mailto:sm@surveymeter.org">sm@surveymeter.org</a>
      </p>
      <nav class="lang" aria-label="{u['lang_label']}">
        <a class="lang__btn" href="{url('id', paths['id'])}" hreflang="id" lang="id"{' aria-current="true"' if lang == 'id' else ''}>ID</a>
        <a class="lang__btn" href="{url('en', paths['en'])}" hreflang="en" lang="en"{' aria-current="true"' if lang == 'en' else ''}>EN</a>
      </nav>
    </div>
  </div>
  <header class="nav" id="nav">
    <div class="container nav__inner">
      <a href="{url(lang)}" class="nav__logo"><img src="/assets/img/surveymeter-logo.png" alt="SurveyMETER, {u['home'].lower()}" width="168" height="31"></a>
      <nav class="nav__menu" id="nav-menu" aria-label="Utama">
        <ul class="menu">{mega_menu(lang, current_top)}</ul>
        <a class="nav__search" href="{url(lang, 'cari')}">{u['search']}</a>
      </nav>
      <div class="nav__actions">
        <a href="{url(lang, 'kontak')}" class="btn btn--primary nav__cta">{u['contact_cta']}</a>
        <button type="button" class="nav__toggle" id="nav-toggle" aria-expanded="false" aria-controls="nav-menu" data-label-open="{u['menu']}" data-label-close="{'Tutup' if lang == 'id' else 'Close'}"><span>{u['menu']}</span></button>
      </div>
    </div>
  </header>
  <main id="main">
{body}
  </main>
{footer(lang)}
  <script src="/main.js?v={ASSET_V}" defer></script>
</body>
</html>
'''


def footer(lang):
    u = UI[lang]
    t = lang
    cols = []
    for top_key, tid, ten, cs in MENU[:4]:
        links = []
        for _, _, ls in cs:
            for key, lid, len_, p in ls[:4]:
                links.append(f'<li><a href="{url(lang, p)}">{esc(lid if t == "id" else len_)}</a></li>')
        cols.append(f'<div><h2 class="footer__head">{esc(tid if t == "id" else ten)}</h2><ul>{"".join(links[:6])}</ul></div>')
    return f'''  <footer class="footer">
    <div class="container">
      <div class="footer__grid footer__grid--wide">
        <div class="footer__brand">
          <img src="/assets/img/surveymeter-logo.png" alt="SurveyMETER" width="168" height="31" loading="lazy">
          <p>{u['footer_about']}</p>
          <address>Jl. Jenengan Raya No. 109, Maguwoharjo, Depok, Sleman, D.I. Yogyakarta 55282<br>
          <a href="tel:+622744477464">+62 274 4477-464</a> &middot; <a href="mailto:sm@surveymeter.org">sm@surveymeter.org</a></address>
          <p class="footer__social">
            <a href="https://www.facebook.com/Surveymeter/" target="_blank" rel="noopener">Facebook</a>
            <a href="https://x.com/SurveyMETER_Id" target="_blank" rel="noopener">X</a>
            <a href="https://www.youtube.com/channel/UCVvz8wzl-kfUxsB4I0SIEpQ" target="_blank" rel="noopener">YouTube</a>
            <a href="https://www.instagram.com/surveymeter/" target="_blank" rel="noopener">Instagram</a>
          </p>
        </div>
        {''.join(cols)}
      </div>
      <p class="footer__fine">&copy; <span id="year">2026</span> PT SurveyMETER. {u['footer_legal']}</p>
    </div>
  </footer>'''


def page_head(lang, key, title, intro='', crumbs=None):
    u = UI[lang]
    meta = PAGES.get(key)
    trail = [(u['home'], url(lang))]
    if meta and meta['top'] not in ('news', 'contact', 'search'):
        trail.append((meta['top_id'] if lang == 'id' else meta['top_en'], None))
    if crumbs:
        trail += crumbs
    items = ''.join(
        f'<li>{"<a href=%s>%s</a>" % (chr(34) + h + chr(34), esc(n)) if h else esc(n)}</li>' for n, h in trail)
    eyebrow = ''
    if meta and meta.get('col_id'):
        eyebrow = f'<p class="eyebrow">{esc(meta["col_id"] if lang == "id" else meta["col_en"])}</p>'
    intro_html = f'<p class="page-head__intro">{esc(intro)}</p>' if intro else ''
    return f'''    <section class="page-head">
      <div class="container">
        <nav aria-label="Breadcrumb"><ol class="crumbs">{items}</ol></nav>
        {eyebrow}
        <h1>{esc(title)}</h1>
        {intro_html}
      </div>
    </section>'''


def sidebar(lang, key):
    u = UI[lang]
    meta = PAGES.get(key)
    sib = ''
    if meta:
        for top_key, tid, ten, cols in MENU:
            if top_key != meta['top']:
                continue
            groups = []
            for col_id, col_en, links in cols:
                lis = ''.join(
                    f'<li><a href="{url(lang, p)}"{" aria-current=\"page\"" if k == key else ""}>{esc(lid if lang == "id" else len_)}</a></li>'
                    for k, lid, len_, p in links)
                groups.append(f'<p class="side__head">{esc(col_id if lang == "id" else col_en)}</p><ul class="side__nav">{lis}</ul>')
            sib = f'<div class="side__box"><h2 class="side__title">{u["in_section"]}</h2>{"".join(groups)}</div>'
    news = site[lang]['lists']['news']['items'][:5]
    lis = ''.join(
        f'<li><a href="{url(lang, post_path(lang, n["path"]))}">{esc(n["title"])}</a>'
        f'<span>{esc(human_date(item_date(lang, n), lang))}</span></li>' for n in news)
    latest = f'<div class="side__box"><h2 class="side__title">{u["latest"]}</h2><ul class="side__news">{lis}</ul><a class="link" href="{url(lang, "berita")}">{u["all_news"]}</a></div>'
    return f'<aside class="side">{sib}{latest}</aside>'


def item_date(lang, item):
    post = find_post(lang, item)[0] or {}
    return iso_date(post.get('date', '')) or iso_date(post.get('meta', {}).get('Tanggal', '')) or iso_date(item.get('list_date', ''))


def card(lang, item):
    post, link_lang = find_post(lang, item)
    post = post or {}
    link_lang = link_lang or lang
    d = item_date(lang, item)
    pic = img(item.get('img') or post.get('hero', ''))
    typ = (post.get('meta') or {}).get('Tipe') or (post.get('meta') or {}).get('Type') or ''
    excerpt = item.get('excerpt') or re.sub(r'<[^>]+>', ' ', post.get('body', ''))[:200]
    excerpt = re.sub(r'\s+', ' ', html.unescape(excerpt)).strip()
    if len(excerpt) > 160:
        excerpt = excerpt[:160].rsplit(' ', 1)[0] + '...'
    media = f'<img src="{esc(pic)}" alt="" loading="lazy">' if pic else '<span class="card__ph" aria-hidden="true"></span>'
    meta_bits = ' '.join(x for x in [
        f'<time datetime="{d}">{human_date(d, lang)}</time>' if d else '',
        f'<span>{esc(typ)}</span>' if typ else ''] if x)
    target = post.get('path', item['path'])
    dl = item.get('download') or DOWNLOADS.get(item['path'], '')
    dl_html = (f'<a class="card__dl" href="{esc(dl)}" target="_blank" rel="noopener">{UI[lang]["download"]}</a>'
               if dl else '')
    return (f'<li class="card"><div class="card__media">{media}</div><div class="card__body">'
            f'<p class="card__meta">{meta_bits}</p>'
            f'<h3><a href="{url(link_lang, post_path(link_lang, target))}"{" hreflang=" + chr(34) + link_lang + chr(34) if link_lang != lang else ""}>{esc(item["title"])}</a></h3>'
            f'<p class="card__excerpt">{esc(excerpt)}</p>{dl_html}</div></li>')


def no_dashes(text):
    """House style: no em or en dashes anywhere, including migrated old-site text."""
    text = re.sub(r'(\d)\s*–\s*(\d)', r'\1-\2', text)
    text = re.sub(r'\s*[—–]\s*', ' - ', text)
    return text


def write(rel, content):
    content = no_dashes(content)
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(content)


def sorted_items(lang, items):
    return sorted(items, key=lambda i: item_date(lang, i) or '0000', reverse=True)


def list_page(lang, key, *, per_page=0):
    meta = PAGES[key]
    data = site[lang]['lists'].get(key, {'intro': '', 'items': []})
    items = data['items'] if key == 'news' else sorted_items(lang, data['items'])
    title = meta[lang]
    intro = data.get('intro', '')
    pages = [items]
    if per_page and len(items) > per_page:
        pages = [items[i:i + per_page] for i in range(0, len(items), per_page)]
    u = UI[lang]
    other_n = len(site[OTHER[lang]]['lists'].get(key, {}).get('items', []))
    other_pages = max(1, -(-other_n // per_page)) if per_page else 1
    for n, chunk in enumerate(pages, 1):
        rel = meta['path'] if n == 1 else f'{meta["path"]}/{n}'
        cards = ''.join(card(lang, i) for i in chunk) or f'<p class="empty">{u["empty"]}</p>'
        pager = ''
        if len(pages) > 1:
            links = []
            if n > 1:
                prev = meta['path'] if n == 2 else f'{meta["path"]}/{n - 1}'
                links.append(f'<a class="btn btn--outline" href="{url(lang, prev)}" rel="prev">{u["prev"]}</a>')
            links.append(f'<span>{u["page"]} {n} {u["of"]} {len(pages)}</span>')
            if n < len(pages):
                links.append(f'<a class="btn btn--outline" href="{url(lang, meta["path"] + "/" + str(n + 1))}" rel="next">{u["next"]}</a>')
            pager = f'<nav class="pager" aria-label="{u["page"]}">{"".join(links)}</nav>'
        count = f'<p class="count">{len(items)} {u["items"]}</p>'
        body = page_head(lang, key, title, intro) + f'''
    <div class="container with-side">
      <div>
        {count}
        <ul class="cards-grid{' cards-grid--pubs' if key in PUB_LISTS + ('aging_pubs', 'stunting_pubs') else ''}">{cards}</ul>
        {pager}
      </div>
      {sidebar(lang, key)}
    </div>'''
        write(os.path.join(url(lang, rel).strip('/'), 'index.html'),
              layout(lang, title, body, current_top=meta['top'], alt_path=rel if n <= other_pages else meta['path'],
                     self_path=rel, desc=intro))


def post_page(lang, post, section_key):
    u = UI[lang]
    meta = post.get('meta') or {}
    d = iso_date(post.get('date', '')) or iso_date(meta.get('Tanggal', '') or meta.get('Date', ''))
    sec = PAGES.get(section_key, PAGES['news'])
    crumbs = [(sec[lang], url(lang, sec['path']))]
    rows = []
    labels = {'Tanggal': u['date'], 'Date': u['date'], 'Tipe': u['type'], 'Type': u['type'],
              'Penulis': u['author'], 'Author': u['author'], 'Kata Kunci': u['keywords'],
              'Keywords': u['keywords'], 'Lokasi': u['location'], 'Location': u['location']}
    for k, v in meta.items():
        if v and k in labels and k not in ('Tanggal', 'Date'):
            rows.append(f'<div><dt>{labels[k]}</dt><dd>{esc(v)}</dd></div>')
    if d:
        rows.insert(0, f'<div><dt>{u["date"]}</dt><dd><time datetime="{d}">{human_date(d, lang)}</time></dd></div>')
    hero = img(post.get('hero', ''))
    hero_html = f'<figure class="post__hero"><img src="{esc(hero)}" alt=""></figure>' if hero else ''
    if not hero:
        # Publications hide the cover on their detail page; the list thumbnail is the cover.
        cover = next((i.get('img') for lst in site[lang]['lists'].values() for i in lst['items']
                      if i['path'] == post['path'] and i.get('img')), '')
        if cover:
            hero_html = f'<figure class="post__cover"><img src="{esc(img(cover))}" alt=""></figure>'
    body = rewrite_body(post.get('body', ''), lang)
    dl = DOWNLOADS.get(post['path']) or DOWNLOADS.get(re.sub(r'^/(id|en)/', f'/{OTHER[lang]}/', post['path']), '')
    if dl and dl not in body:
        hero_html += (f'<p class="post__download"><a class="btn btn--primary" href="{esc(dl)}" target="_blank" '
                      f'rel="noopener">{u["download_pdf"]}</a></p>')
    related =[i for i in site[lang]['lists'].get(section_key, {}).get('items', []) if i['path'] != post['path']][:4]
    rel_html = ''
    if related:
        rel_html = '<section class="related"><h2>%s</h2><ul class="cards-grid cards-grid--compact">%s</ul></section>' % (
            u['related'], ''.join(card(lang, i) for i in related))
    source = OLD + post['path']
    content = page_head(lang, section_key, post['title'], '', crumbs) + f'''
    <div class="container with-side">
      <article class="post">
        {('<dl class="post__meta">' + ''.join(rows) + '</dl>') if rows else ''}
        {hero_html}
        <div class="prose">{body}</div>
        <p class="post__source"><a class="link" href="{url(lang, sec['path'])}">{u['back']} {esc(sec[lang].lower())}</a></p>
        {rel_html}
      </article>
      {sidebar(lang, section_key)}
    </div>'''
    rel = post_path(lang, post['path'])
    text_desc = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', post.get('body', '')))).strip()[:160]
    write(os.path.join(url(lang, rel).strip('/'), 'index.html'),
          layout(lang, post['title'], content, current_top=sec['top'], alt_path=rel_alt(lang, post['path']), self_path=rel, desc=text_desc))
    return {'t': post['title'], 'u': url(lang, rel), 'd': d, 'h': human_date(d, lang), 's': sec[lang],
            'x': text_desc}


def rel_alt(lang, old_path):
    """Path of the same post in the other language, or that language's news index."""
    other = 'en' if lang == 'id' else 'id'
    swapped = re.sub(r'^/(id|en)/', f'/{other}/', old_path)
    if swapped in site[other]['posts']:
        return post_path(other, swapped)
    return 'berita'


# ---------------------------------------------------------------- special pages
def static_prose(lang, key, extra_top='', extra_bottom=''):
    meta = PAGES[key]
    pg = site[lang]['pages'].get(key, {})
    body = rewrite_body(pg.get('body', ''), lang)
    content = page_head(lang, key, meta[lang]) + f'''
    <div class="container with-side">
      <div class="prose-wrap">{extra_top}<div class="prose">{body}</div>{extra_bottom}</div>
      {sidebar(lang, key)}
    </div>'''
    write(os.path.join(url(lang, meta['path']).strip('/'), 'index.html'),
          layout(lang, meta[lang], content, current_top=meta['top'], alt_path=meta['path']))


def custom_page(lang, key, inner, intro=''):
    meta = PAGES[key]
    content = page_head(lang, key, meta[lang], intro) + f'''
    <div class="container with-side">
      <div class="prose-wrap">{inner}</div>
      {sidebar(lang, key)}
    </div>'''
    write(os.path.join(url(lang, meta['path']).strip('/'), 'index.html'),
          layout(lang, meta[lang], content, current_top=meta['top'], alt_path=meta['path'], desc=intro))


def scope_page(lang):
    if lang == 'id':
        intro = 'Kegiatan SurveyMETER terbagi dalam tiga bidang: survei, pelatihan dan pengembangan, serta riset. Fokus isunya bergeser mengikuti kebutuhan kebijakan.'
        p1, p2 = 'Periode 2012-2017', 'Periode 2018-2022'
        a = ['Kesehatan', 'Pendidikan', 'Kebencanaan']
        b = ['Kesehatan', 'Pendidikan', 'Kependudukan dan lingkungan']
        h_focus, h_area = 'Fokus isu', 'Lingkup kegiatan'
        areas = [('Survei', ['Studi evaluasi dampak', 'Studi berorientasi kebijakan']),
                 ('Pelatihan dan pengembangan', ['Pendampingan', 'Pelatihan']),
                 ('Riset', ['Pengelolaan pengetahuan', 'Penelitian ilmiah', 'Kajian'])]
    else:
        intro = 'SurveyMETER works in three areas: surveys, training and development, and research. Its issue focus shifts with policy needs.'
        p1, p2 = 'Period 2012-2017', 'Period 2018-2022'
        a = ['Health', 'Education', 'Disaster']
        b = ['Health', 'Education', 'Population and environment']
        h_focus, h_area = 'Issue focus', 'Scope of activities'
        areas = [('Survey', ['Impact evaluation study', 'Policy-based study']),
                 ('Training and development', ['Assistance', 'Training']),
                 ('Research', ['Knowledge management', 'Scientific research', 'Study'])]
    keys = {'Studi evaluasi dampak': 'impact', 'Impact evaluation study': 'impact', 'Studi berorientasi kebijakan': 'policy',
            'Policy-based study': 'policy', 'Pendampingan': 'assistance', 'Assistance': 'assistance', 'Pelatihan': 'training',
            'Training': 'training', 'Pengelolaan pengetahuan': 'knowledge', 'Knowledge management': 'knowledge',
            'Penelitian ilmiah': 'scientific', 'Scientific research': 'scientific', 'Kajian': 'study', 'Study': 'study'}
    focus = ''.join(
        f'<div class="focus__period"><h3>{p}</h3><ul>{"".join(f"<li>{x}</li>" for x in lst)}</ul></div>'
        for p, lst in ((p1, a), (p2, b)))
    def area_links(lst):
        return ''.join(f'<li><a href="{url(lang, PAGES[keys[x]]["path"])}">{x}</a></li>' for x in lst)
    area_html = ''.join(f'<div class="scope__area"><h3>{t}</h3><ul>{area_links(lst)}</ul></div>' for t, lst in areas)
    inner = f'<h2>{h_focus}</h2><div class="focus">{focus}</div><h2>{h_area}</h2><div class="scope">{area_html}</div>'
    custom_page(lang, 'scope', inner, intro)


def ability_page(lang):
    if lang == 'id':
        intro = 'Perjalanan SurveyMETER dari tim survei longitudinal menjadi lembaga berbasis pengetahuan.'
        steps = [('2002', 'Pendirian', 'Berdiri 20 Februari 2002 di Yogyakarta.'),
                 ('2002-2006, berlanjut', 'Survei longitudinal', 'Survei untuk keperluan ilmiah (hulu).'),
                 ('2007-2010, berlanjut', 'Survei skala besar', 'Survei evaluasi berdampak dan survei berorientasi kebijakan.'),
                 ('2010-2012, berlanjut', 'Knowledge Sector Initiative (KSI)', 'Transformasi menuju lembaga berbasis pengetahuan.'),
                 ('2013 dan seterusnya', 'Lembaga pengetahuan', 'Menginspirasi dan memperkuat kebijakan berbasis data penelitian.')]
    else:
        intro = 'How SurveyMETER grew from a longitudinal survey team into a knowledge-based institution.'
        steps = [('2002', 'Founding', 'Founded on 20 February 2002 in Yogyakarta.'),
                 ('2002-2006, ongoing', 'Longitudinal surveys', 'Surveys for scientific (upstream) purposes.'),
                 ('2007-2010, ongoing', 'Large-scale surveys', 'Impact evaluation surveys and policy-oriented surveys.'),
                 ('2010-2012, ongoing', 'Knowledge Sector Initiative (KSI)', 'Transformation into a knowledge-based institution.'),
                 ('2013 onwards', 'Knowledge institution', 'Inspiring and strengthening policy based on research data.')]
    inner = '<ol class="journey">' + ''.join(
        f'<li><span class="journey__when">{w}</span><h3>{t}</h3><p>{d}</p></li>' for w, t, d in steps) + '</ol>'
    custom_page(lang, 'ability', inner, intro)


PARTNER_GROUPS = {
    'id': [('Pemerintah', ['Bappenas', 'TNP2K', 'Kementerian Kesehatan RI', 'Kementerian Pendidikan RI', 'Badan Nasional Penanggulangan Bencana (BNPB)']),
           ('Donor dan lembaga pembangunan', ['The World Bank', 'Asian Development Bank', 'UNICEF', 'UNDP', 'AusAID', 'PROSPERA', 'SUM2, USAID', 'Millennium Challenge Account Indonesia']),
           ('Universitas dan lembaga riset', ['RAND Corporation', 'J-PAL', 'Innovations for Poverty Action', 'Mathematica Policy Research', 'RTI International', 'IDinsight', 'Amsterdam Institute for International Development', 'Center for Aging Studies', 'Duke University', 'University of California, Los Angeles', 'University of North Carolina', 'Australian National University', 'University of Melbourne', 'University of Sydney', 'Monash University', 'Hitotsubashi University', 'PUSKAPA Universitas Indonesia', 'Pusat Studi Kependudukan dan Kebijakan UGM']),
           ('Organisasi masyarakat', ['The Asia Foundation', 'HelpAge International', "Women's World Banking", 'GRM International', 'AKATIGA Pusat Analisis Sosial', 'Yayasan Emong Lansia'])],
}
PARTNER_GROUPS['en'] = [('Government', PARTNER_GROUPS['id'][0][1]), ('Donors and development agencies', PARTNER_GROUPS['id'][1][1]),
                        ('Universities and research institutes', PARTNER_GROUPS['id'][2][1]), ('Civil society', PARTNER_GROUPS['id'][3][1])]


def partners_page(lang):
    intro = ('37 lembaga pemerintah, donor, universitas, dan organisasi masyarakat yang pernah bekerja sama dengan SurveyMETER.'
             if lang == 'id' else '37 government bodies, donors, universities, and civil society organisations that have worked with SurveyMETER.')
    inner = '<div class="partner-grid">' + ''.join(
        f'<section><h2>{g} <span>{len(lst)}</span></h2><ul>{"".join(f"<li>{esc(x)}</li>" for x in lst)}</ul></section>'
        for g, lst in PARTNER_GROUPS[lang]) + '</div>'
    custom_page(lang, 'partners', inner, intro)


STAFF = [('Bondan S. Sikoki, M.A.', 'Komisaris', 'Commissioner'),
         ('Dr. Cecep Sukria Sumantri', 'Direktur', 'Director'),
         ('Nasirudin, S.P., M.Ec.Dev.', 'Koordinator Divisi Survei', 'Survey Division Coordinator'),
         ('Dr. Edy Purwanto, M.Sc.', 'Koordinator Divisi Kajian', 'Study Division Coordinator'),
         ('Dani Alfah, S.Sos., M.P.A.', 'Koordinator Divisi Pelatihan', 'Training Division Coordinator'),
         ('Iip Umar Rifai, S.Kom', 'Koordinator Divisi IT Support', 'IT Support Division Coordinator'),
         ('Muhammad Mulia, S.E., M.Sc.', 'Manajer Kantor', 'Office Manager'),
         ('Kawandiyono Santoso', 'Manajer Bisnis', 'Business Manager')]


def initials(name):
    words = [w for w in re.sub(r'^(Dr\.|Ir\.)\s*', '', name.split(',')[0]).replace('Dr. ', '').split() if w[0].isalpha()]
    return (words[0][0] + (words[1][0] if len(words) > 1 else '')).upper()


def staff_page(lang):
    intro = 'Periode 2024-2028.' if lang == 'id' else 'Period 2024-2028.'
    cards = ''.join(
        f'<li><span class="avatar" aria-hidden="true">{initials(n)}</span><div><strong>{esc(n)}</strong><span>{esc(r_id if lang == "id" else r_en)}</span></div></li>'
        for n, r_id, r_en in STAFF)
    hist_title = 'Direktur eksekutif dari masa ke masa' if lang == 'id' else 'Executive directors over time'
    hist = [('Bondan S. Sikoki', '2002-2012'), ('Dr. Ir. Ni Wayan Suriastini, M.Phil', '2012-2024'),
            ('Dr. Cecep Sukria Sumantri', 'sejak Februari 2024' if lang == 'id' else 'since February 2024')]
    hist_html = ''.join(f'<li><strong>{w}</strong><p>{n}</p></li>' for n, w in hist)
    inner = f'<ul class="people people--page">{cards}</ul><h2>{hist_title}</h2><ol class="timeline">{hist_html}</ol>'
    custom_page(lang, 'staff', inner, intro)


def contact_page(lang):
    t = (lambda a, b: a if lang == 'id' else b)
    inner = f'''<div class="contact-page">
        <dl class="contact contact--light">
          <div><dt>{t('Kantor', 'Office')}</dt><dd><address>Jl. Jenengan Raya No. 109, Maguwoharjo, Depok, Sleman, D.I. Yogyakarta 55282</address></dd></div>
          <div><dt>{t('Telepon', 'Phone')}</dt><dd><a href="tel:+622744477464">+62 274 4477-464</a></dd></div>
          <div><dt>{t('Faks', 'Fax')}</dt><dd>+62 274 4477-004</dd></div>
          <div><dt>Email</dt><dd><a href="mailto:sm@surveymeter.org">sm@surveymeter.org</a></dd></div>
          <div><dt>{t('Media sosial', 'Social media')}</dt><dd class="social">
            <a href="https://www.facebook.com/Surveymeter/" target="_blank" rel="noopener">Facebook</a>
            <a href="https://x.com/SurveyMETER_Id" target="_blank" rel="noopener">X</a>
            <a href="https://www.youtube.com/channel/UCVvz8wzl-kfUxsB4I0SIEpQ" target="_blank" rel="noopener">YouTube</a>
            <a href="https://www.instagram.com/surveymeter/" target="_blank" rel="noopener">Instagram</a></dd></div>
        </dl>
        <div class="contact-page__actions">
          <a class="btn btn--primary btn--lg" href="mailto:sm@surveymeter.org">{t('Kirim email', 'Send an email')}</a>
          <a class="btn btn--outline btn--lg" href="https://www.google.com/maps/place/SurveyMETER/@-7.7595736,110.4185988,18z/data=!3m1!4b1!4m6!3m5!1s0x2e7a59844ecbebcb:0xacde1e1d920428f6!8m2!3d-7.7595736!4d110.4185988!16s%2Fg%2F1pzwxft90" target="_blank" rel="noopener">{t('Buka di peta', 'Open in maps')}</a>
        </div>
      </div>'''
    meta = PAGES['contact']
    content = page_head(lang, 'contact', meta[lang], t('Untuk kerja sama riset, pertanyaan soal data, atau publikasi.',
                                                      'For research partnerships, questions about data, or publications.')) + f'''
    <div class="container section-pad">{inner}</div>'''
    write(os.path.join(url(lang, meta['path']).strip('/'), 'index.html'),
          layout(lang, meta[lang], content, current_top='contact', alt_path=meta['path']))


def search_page(lang, index):
    u = UI[lang]
    write(f'search-index-{lang}.json', json.dumps(index, ensure_ascii=False, separators=(',', ':')))
    meta = PAGES['search']
    content = page_head(lang, 'search', meta[lang]) + f'''
    <div class="container section-pad">
      <form class="search-box" role="search" data-search-index="/search-index-{lang}.json" data-none="{u['search_none']}" data-count="{u['search_count']}">
        <label for="q">{u['search_label']}</label>
        <input id="q" name="q" type="search" placeholder="{u['search_ph']}" autocomplete="off">
      </form>
      <p class="count" id="search-status" aria-live="polite"></p>
      <ol class="results" id="search-results"></ol>
    </div>'''
    write(os.path.join(url(lang, meta['path']).strip('/'), 'index.html'),
          layout(lang, meta[lang], content, current_top='search', alt_path=meta['path']))


def not_found():
    u = UI['id']
    content = f'''    <section class="page-head"><div class="container"><h1>{u['nf_title']}</h1>
      <p class="page-head__intro">{u['nf_text']}</p>
      <p><a class="btn btn--primary" href="/">{u['home']}</a> <a class="btn btn--outline" href="/cari/">{u['search']}</a></p></div></section>'''
    write('404.html', layout('id', u['nf_title'], content))


# ---------------------------------------------------------------- home
def home(lang):
    main = open(os.path.join(ROOT, 'templates/home.html'), encoding='utf-8').read()
    main = re.sub(r'href="(https?://(?:www\.)?surveymeter\.org[^"]*)"',
                  lambda m: 'href="%s"' % esc(rewrite_href(html.unescape(m.group(1)), lang)), main)
    main = re.sub(r'(href="/[^"]*") target="_blank" rel="noopener"', r'\1', main)
    main = main.replace('<main id="main">', '').replace('</main>', '')
    main = main.replace('src="assets/', 'src="/assets/')
    main = main.replace('href="#kontak"', f'href="{url(lang, "kontak")}"')
    # News list on the home page comes from the migrated news feed.
    news = site[lang]['lists']['news']['items'][:6]
    lis = ''.join(
        f'<li><time datetime="{item_date(lang, n)}">{human_date(item_date(lang, n), lang)}</time>'
        f'<a href="{url(lang, post_path(lang, n["path"]))}">{esc(n["title"])}</a></li>' for n in news)
    main = re.sub(r'<ol class="news__list">.*?</ol>', f'<ol class="news__list">{lis}</ol>', main, flags=re.S)
    if lang == 'en':
        main = re.sub(r'(<([a-z0-9]+)[^>]*?data-i18n="[^"]+"[^>]*>)(.*?)(</\2>)',
                      lambda m: m.group(1) + esc(HOME_EN.get(re.search(r'data-i18n="([^"]+)"', m.group(1)).group(1), html.unescape(m.group(3)))) + m.group(4),
                      main, flags=re.S)
    main = re.sub(r' data-i18n="[^"]+"', '', main)
    write(os.path.join(url(lang).strip('/'), 'index.html') if lang == 'en' else 'index.html',
          layout(lang, '', main, current_top='', alt_path='', page_class='is-home'))


# ---------------------------------------------------------------- build
def build():
    for d in ('baca', 'read', 'tentang', 'kegiatan', 'publikasi', 'data', 'kelompok-kerja', 'karir', 'berita',
              'kontak', 'cari', 'en'):
        p = os.path.join(ROOT, d)
        if os.path.isdir(p):
            shutil.rmtree(p)
    sitemap = []
    for lang in ('id', 'en'):
        L = site[lang]
        # which section each post belongs to: first list that contains it, news last.
        owner = {}
        order = [k for k in L['lists'] if k not in ('news', 'all_pubs', 'data_publik')] + ['all_pubs', 'news']
        for k in order:
            for it in L['lists'].get(k, {}).get('items', []):
                owner.setdefault(it['path'], k if k in PAGES else 'news')
        index = []
        for path, post in L['posts'].items():
            entry = post_page(lang, post, owner.get(path, 'news'))
            index.append(entry)
            sitemap.append(SITE_URL + entry['u'])
        for key in PAGES:
            if key in L['lists']:
                list_page(lang, key, per_page=NEWS_PER_PAGE if key in ('news', 'all_pubs') else 0)
                sitemap.append(SITE_URL + url(lang, PAGES[key]['path']))
        for key in ('ifls_east', 'star', 'ilas'):
            post = L['data'].get(key)
            if post:
                meta = PAGES[key]
                fake = dict(post)
                entry_path = meta['path']
                d = iso_date(post.get('date', ''))
                content = page_head(lang, key, post['title'] or meta[lang]) + f'''
    <div class="container with-side">
      <article class="post">
        {('<figure class="post__hero"><img src="%s" alt=""></figure>' % esc(img(post['hero']))) if post.get('hero') else ''}
        <div class="prose">{rewrite_body(post.get('body', ''), lang)}</div>
      </article>
      {sidebar(lang, key)}
    </div>'''
                write(os.path.join(url(lang, entry_path).strip('/'), 'index.html'),
                      layout(lang, meta[lang], content, current_top='pubs', alt_path=entry_path))
                sitemap.append(SITE_URL + url(lang, entry_path))
        static_prose(lang, 'profile')
        static_prose(lang, 'vision')
        staff_page(lang)
        partners_page(lang)
        scope_page(lang)
        ability_page(lang)
        contact_page(lang)
        search_page(lang, sorted(index, key=lambda e: e['d'] or '0', reverse=True))
        home(lang)
        for k in ('profile', 'vision', 'staff', 'partners', 'scope', 'ability', 'contact', 'search'):
            sitemap.append(SITE_URL + url(lang, PAGES[k]['path']))
        sitemap.append(SITE_URL + url(lang))
    not_found()
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
          ''.join(f'  <url><loc>{esc(u)}</loc></url>\n' for u in sorted(set(sitemap))) + '</urlset>\n'
    write('sitemap.xml', xml)
    print('built', len(set(sitemap)), 'pages; list items hidden because the old page was broken:', SKIPPED)


if __name__ == '__main__':
    build()
