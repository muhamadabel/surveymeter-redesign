(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];

  const EN = {
    'skip': 'Skip to content',
    'ribbon.lead': 'New release:',
    'ribbon.text': 'ILAS 2023 data can now be requested for research.',
    'ribbon.link': 'See the dataset',
    'nav.data': 'Public data',
    'nav.pubs': 'Publications',
    'nav.about': 'About',
    'nav.contact': 'Contact',
    'nav.cta': 'Request data access',
    'nav.menu': 'Menu',
    'nav.close': 'Close',
    'hero.l1': 'Measuring Indonesia,',
    'hero.l2': 'one household at a time.',
    'hero.lead': 'A research institute in Yogyakarta that has collected household panel data since 2002, and opens it to researchers.',
    'hero.cta': 'See the datasets',
    'mock.title': 'Data catalog',
    'mock.datasets': 'Datasets',
    'mock.pubs': 'Publications',
    'mock.ilas': 'Released 2024',
    'mock.ifls': '7 provinces',
    'mock.star': 'Post-tsunami panel',
    'mock.s1': 'Contents',
    'mock.v1': 'Microdata',
    'mock.s2': 'Instrument',
    'mock.v2': 'Questionnaire',
    'mock.s3': 'Extra',
    'mock.v3': 'Caregiver module',
    'mock.pub': 'Publication',
    'mock.pubDate': 'May 2024',
    'proof.title': 'Working with 20 donors, universities, and government bodies',
    'stat.1': 'year the institute was founded',
    'stat.2': 'provinces in the IFLS East panel',
    'stat.3': 'datasets open to researchers',
    'data.title': 'Panel data for research and policy',
    'data.note': 'Three datasets can be requested. Describe what you need and the data team decides on access.',
    'data.request': 'Request access',
    'data.meta': 'Download metadata (JSON)',
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
    'pubs.summary': 'Request summary',
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
    'cta.title': 'Need data for your research?',
    'cta.lead': 'Fill in a short form and we prepare an email draft to the SurveyMETER data team.',
    'cta.request': 'Request data access',
    'cta.email': 'Send an email',
    'footer.data': 'Data',
    'footer.org': 'Institute',
    'footer.contact': 'Contact',
    'footer.fax': 'Fax',
    'form.title': 'Request data access',
    'form.hint': 'This form becomes an email draft to sm@surveymeter.org. You send it.',
    'form.dataset': 'Dataset',
    'form.name': 'Full name',
    'form.org': 'Institution',
    'form.purpose': 'What research is the data for?',
    'form.errName': 'Enter your full name.',
    'form.errOrg': 'Enter your institution or university.',
    'form.errEmail': 'Email format is not valid, e.g. name@university.edu',
    'form.errPurpose': 'Briefly describe your research.',
    'form.submit': 'Prepare email',
    'done.title': 'Email draft ready',
    'done.text': 'Your request is not sent yet. Open the draft in your email app, check it, then send.',
    'done.cta': 'Open email draft',
    'done.back': 'Edit answers'
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

  $$('[data-summary]').forEach(a => {
    const title = a.closest('.pub').querySelector('h3').textContent.trim();
    a.href = 'mailto:sm@surveymeter.org?subject=' + encodeURIComponent('Permintaan ringkasan: ' + title);
  });

  // Built from the facts in AGENT_BRIEF.md until SurveyMETER supplies official DDI or codebook files.
  const METADATA = {
    'ilas-2023': {
      id: 'ILAS 2023',
      title: 'Indonesia Longitudinal Aging Survey',
      topics: ['Kesehatan fisik dan mental', 'Jejaring keluarga', 'Kesiapan ekonomi lansia'],
      partner: 'Asian Development Bank',
      contents: ['Data mikro', 'Kuesioner', 'Modul pengasuh'],
      release: 2024
    },
    'ifls-east': {
      id: 'IFLS East',
      title: 'Survei Aspek Kehidupan Rumah Tangga Indonesia Timur',
      design: 'Panel multi-topik rumah tangga dan komunitas',
      coverage: '7 provinsi Indonesia Timur',
      formats: ['STATA (.dta)', 'SPSS', 'Codebook PDF'],
      access: 'Terbuka dengan registrasi peneliti'
    },
    'star-aceh': {
      id: 'STAR Aceh',
      title: 'Studi Pemulihan Pasca Tsunami Aceh',
      design: 'Panel longitudinal multi-putaran',
      topics: ['Pemulihan ekonomi', 'Relokasi perumahan', 'Ketahanan sosial'],
      partners: ['Duke University', 'World Bank']
    }
  };
  $$('[data-metadata]').forEach(btn => btn.addEventListener('click', () => {
    const key = btn.dataset.metadata;
    const body = { publisher: 'PT SurveyMETER', contact: 'sm@surveymeter.org', ...METADATA[key] };
    const url = URL.createObjectURL(new Blob([JSON.stringify(body, null, 2)], { type: 'application/json' }));
    const a = Object.assign(document.createElement('a'), { href: url, download: `surveymeter-${key}-metadata.json` });
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }));

  const modal = $('#access-modal');
  const form = $('#access-form');
  const done = $('#access-done');
  const select = $('#f-dataset');
  let lastFocus = null;

  function showForm() {
    form.hidden = false;
    done.hidden = true;
  }
  function openModal(dataset) {
    lastFocus = document.activeElement;
    setMenu(false);
    if (dataset) select.value = dataset;
    showForm();
    modal.hidden = false;
    document.body.classList.add('is-locked');
    (dataset ? $('#f-name') : select).focus();
  }
  function closeModal() {
    modal.hidden = true;
    document.body.classList.remove('is-locked');
    if (lastFocus) lastFocus.focus();
  }

  $$('[data-open-access]').forEach(btn => btn.addEventListener('click', () => openModal(btn.dataset.openAccess)));
  modal.addEventListener('click', e => { if (e.target.closest('[data-close]')) closeModal(); });
  $('#access-back').addEventListener('click', () => { showForm(); $('#f-name').focus(); });

  document.addEventListener('keydown', e => {
    if (modal.hidden) {
      if (e.key === 'Escape' && isOpen()) { setMenu(false); toggle.focus(); }
      return;
    }
    if (e.key === 'Escape') closeModal();
    if (e.key === 'Tab') {
      const f = $$('button, a[href], input, select, textarea', $('.modal__panel')).filter(el => !el.closest('[hidden]'));
      const first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });

  const emailOk = v => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);
  form.addEventListener('submit', e => {
    e.preventDefault();
    let firstBad = null;
    ['name', 'org', 'email', 'purpose'].forEach(n => {
      const el = form.elements[n];
      const v = el.value.trim();
      const bad = !v || (n === 'email' && !emailOk(v));
      el.closest('.field').classList.toggle('is-invalid', bad);
      el.setAttribute('aria-invalid', String(bad));
      if (bad && !firstBad) firstBad = el;
    });
    if (firstBad) { firstBad.focus(); return; }

    const d = Object.fromEntries(new FormData(form));
    const body = [
      `Dataset: ${d.dataset}`,
      `Nama: ${d.name}`,
      `Instansi: ${d.org}`,
      `Email: ${d.email}`,
      '',
      'Tujuan riset:',
      d.purpose
    ].join('\n');
    $('#access-mailto').href = 'mailto:sm@surveymeter.org?subject=' +
      encodeURIComponent(`Permohonan akses data ${d.dataset}`) + '&body=' + encodeURIComponent(body);

    form.hidden = true;
    done.hidden = false;
    $('#access-mailto').focus();
  });
  form.addEventListener('input', e => {
    const field = e.target.closest('.field');
    if (field && field.classList.contains('is-invalid')) {
      field.classList.remove('is-invalid');
      e.target.removeAttribute('aria-invalid');
    }
  });

  $('#year').textContent = new Date().getFullYear();
})();
