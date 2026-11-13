(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];

  const EN = {
    'skip': 'Skip to content',
    'ribbon.lead': 'New release:',
    'ribbon.text': 'ILAS 2023, a study of population aging in Indonesia with ADB.',
    'ribbon.link': 'See the dataset',
    'nav.data': 'Public data',
    'nav.pubs': 'Publications',
    'nav.about': 'About',
    'nav.contact': 'Contact',
    'nav.cta': 'Contact us',
    'nav.menu': 'Menu',
    'nav.close': 'Close',
    'hero.l1': 'Measuring Indonesia,',
    'hero.l2': 'one household at a time.',
    'hero.lead': 'A research institute in Yogyakarta that has collected Indonesian household panel data since 2002, with partners at home and abroad.',
    'hero.cta': 'See our surveys',
    'hero.about': 'About SurveyMETER',
    'show.ilas': 'Population aging study with the Asian Development Bank',
    'show.ifls': '7 eastern Indonesian provinces',
    'show.pub': 'Publication, May 2024',
    'proof.title': 'Working with 20 donors, universities, and government bodies',
    'stat.1': 'year the institute was founded',
    'stat.2': 'provinces in the IFLS East panel',
    'stat.3': 'main panel surveys',
    'data.title': 'Panel data for research and policy',
    'data.note': 'Three panel surveys SurveyMETER has run with research partners and donors.',
    'f.contents': 'Contents',
    'f.status': 'Status',
    'f.partner': 'Partner',
    'f.format': 'Format',
    'f.access': 'Access',
    'f.coverage': 'Coverage',
    'f.design': 'Design',
    'ilas.desc': 'Physical and mental health of older people, family networks, and economic readiness for old age. Built with the Asian Development Bank.',
    'ilas.contents': 'Microdata, questionnaires, caregiver module',
    'ilas.status': 'Released 2024',
    'ifls.title': 'Eastern Indonesia Household Life Survey',
    'ifls.desc': 'Multi-topic panel on households and communities in 7 eastern Indonesian provinces.',
    'ifls.access': 'Open with researcher registration',
    'ifls.coverage': '7 eastern Indonesian provinces',
    'star.title': 'Aceh Post-Tsunami Recovery Study',
    'star.desc': 'Economic recovery, housing relocation, and social resilience after the tsunami. With Duke University and the World Bank.',
    'star.design': 'Multi-round panel',
    'star.related': 'Related publication, Dec 2023',
    'pubs.title': 'Latest publications',
    'pubs.adb': 'With the Asian Development Bank',
    'tab.all': 'All',
    'tab.aging': 'Aging',
    'tab.health': 'Health',
    'tab.econ': 'Economy',
    'about.title': 'About SurveyMETER',
    'about.p1': 'Our name stands for Survey, Measurement, Training, and Research. The institute was formed by a team with more than 15 years of experience running Indonesia Family Life Survey data collection with RAND Corporation.',
    'leaders.title': 'Executive directors',
    'leaders.now': 'Since February 2024',
    'tl.title': 'Milestones',
    'tl.1': 'Yayasan SurveyMETER founded in Yogyakarta on 20 February.',
    'tl.2': 'Took on a stronger role in public policy research and advocacy.',
    'tl.3': 'Became PT SurveyMETER to expand international research partnerships.',
    'partners.title': 'We have worked with',
    'partners.g1': 'Donors and multilaterals',
    'partners.g2': 'Research and universities',
    'partners.g3': 'Government',
    'cta.title': 'Contact SurveyMETER',
    'cta.lead': 'For research partnerships, questions about data, or publications, reach our office in Yogyakarta.',
    'cta.email': 'Send an email',
    'cta.phone': 'Phone',
    'cta.office': 'Office',
    'cta.map': 'Open in maps',
    'data.ask': 'Ask about this survey',
    'footer.data': 'Data',
    'footer.org': 'Institute',
    'footer.contact': 'Contact',
    'footer.fax': 'Fax',
  };

  const ID = { 'nav.close': 'Tutup' };
  $$('[data-i18n]').forEach(el => { ID[el.dataset.i18n] ??= el.textContent; });

  let lang = 'id';
  const t = key => (lang === 'en' ? EN : ID)[key] ?? ID[key] ?? key;

  function setLang(next) {
    lang = next;
    document.documentElement.lang = next;
    $$('[data-i18n]').forEach(el => { el.textContent = t(el.dataset.i18n); });
    $$('.lang__btn').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.lang === next)));
    syncMenuLabel();
    try { localStorage.setItem('sm-lang', next); } catch (_) {}
  }

  const nav = $('#nav');
  const onScroll = () => nav.classList.toggle('is-scrolled', window.scrollY > 8);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  const toggle = $('#nav-toggle');
  const menu = $('#nav-menu');
  const isOpen = () => toggle.getAttribute('aria-expanded') === 'true';
  function syncMenuLabel() {
    const label = toggle.querySelector('span');
    label.dataset.i18n = isOpen() ? 'nav.close' : 'nav.menu';
    label.textContent = t(label.dataset.i18n);
  }
  function setMenu(open) {
    toggle.setAttribute('aria-expanded', String(open));
    menu.classList.toggle('is-open', open);
    document.body.classList.toggle('is-locked', open);
    syncMenuLabel();
  }
  toggle.addEventListener('click', () => setMenu(!isOpen()));
  menu.addEventListener('click', e => { if (e.target.closest('a')) setMenu(false); });
  window.matchMedia('(min-width: 761px)').addEventListener('change', e => { if (e.matches) setMenu(false); });

  $$('.lang__btn').forEach(b => b.addEventListener('click', () => setLang(b.dataset.lang)));
  try { if (localStorage.getItem('sm-lang') === 'en') setLang('en'); } catch (_) {}

  // Dataset tabs follow the WAI-ARIA tabs pattern: arrow keys move between tabs.
  const dtabs = $$('.dtab');
  function selectDataset(tab, focus) {
    dtabs.forEach(other => {
      const on = other === tab;
      other.setAttribute('aria-selected', String(on));
      other.tabIndex = on ? 0 : -1;
      const panel = document.getElementById(other.getAttribute('aria-controls'));
      panel.hidden = !on;
      panel.classList.toggle('is-entering', on);
    });
    if (focus) tab.focus();
  }
  dtabs.forEach((tab, i) => {
    tab.addEventListener('click', () => selectDataset(tab));
    tab.addEventListener('keydown', e => {
      const step = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
      if (step) {
        e.preventDefault();
        selectDataset(dtabs[(i + step + dtabs.length) % dtabs.length], true);
      } else if (e.key === 'Home' || e.key === 'End') {
        e.preventDefault();
        selectDataset(dtabs[e.key === 'Home' ? 0 : dtabs.length - 1], true);
      }
    });
  });

  const chips = $$('.chip');
  const pubs = $$('.pub');
  chips.forEach(chip => chip.addEventListener('click', () => {
    chips.forEach(other => other.setAttribute('aria-selected', String(other === chip)));
    const f = chip.dataset.filter;
    pubs.forEach(p => { p.hidden = f !== 'all' && !p.dataset.topics.split(' ').includes(f); });
  }));

  $$('[data-ask]').forEach(a => {
    a.href = 'mailto:sm@surveymeter.org?subject=' + encodeURIComponent('Pertanyaan tentang ' + a.dataset.ask);
  });

  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && isOpen()) { setMenu(false); toggle.focus(); }
  });

  $('#year').textContent = new Date().getFullYear();
})();
