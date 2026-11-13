(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];

  const EN = {
    'skip': 'Skip to content',
    'ribbon.text': 'ILAS 2023 data can now be requested for research.',
    'ribbon.link': 'See the dataset',
    'nav.data': 'Public data',
    'nav.pubs': 'Publications',
    'nav.about': 'About',
    'nav.contact': 'Contact',
    'nav.cta': 'Request data access',
    'nav.menu': 'Menu',
    'nav.close': 'Close',
    'hero.title': 'Measuring Indonesian household life,',
    'hero.titleEm': 'since 2002.',
    'hero.lead': 'A research institute in Yogyakarta. Our team comes from the Indonesia Family Life Survey fieldwork with RAND Corporation, and now opens panel data to researchers.',
    'hero.cta': 'See the datasets',
    'hero.link': 'Read publications',
    'glance.kicker': 'At a glance',
    'glance.title': 'What SurveyMETER has worked on',
    'glance.facts': 'Facts and figures',
    'facts.pause': 'Pause the facts rotation',
    'facts.play': 'Play the facts rotation',
    'fact.1': 'year the institute was founded in Yogyakarta',
    'fact.2u': 'provinces',
    'fact.2': 'in eastern Indonesia covered by the IFLS East panel',
    'fact.3u': 'years',
    'fact.3': 'of team experience running IFLS with RAND before the institute was founded',
    'fact.4u': 'datasets',
    'fact.4': 'open for researchers to request',
    'glance.story': 'Latest release',
    'story.title': 'ILAS 2023: health, family, and economic life of older Indonesians.',
    'story.by': 'With the Asian Development Bank. Released 2024.',
    'story.cta': 'See the ILAS 2023 dataset',
    'glance.partners': 'Partners',
    'partners.head': 'Working with donors, universities, and ministries',
    'partners.count': ' partner institutions',
    'glance.case': 'Panel dataset',
    'case.title': 'IFLS East: households in 7 eastern Indonesian provinces',
    'glance.pubs': 'Publications',
    'quotes.prev': 'Previous publication',
    'quotes.next': 'Next publication',
    'data.title': 'Public data',
    'data.note': 'Three datasets can be requested for research. Describe what you need and the data team decides on access.',
    'data.searchLabel': 'Search datasets',
    'data.searchPh': 'e.g. elderly, Aceh, STATA',
    'data.request': 'Request access',
    'data.meta': 'Download metadata (JSON)',
    'data.empty': 'No dataset matches',
    'data.clear': 'Show all datasets',
    'ilas.year': 'released 2024',
    'ilas.desc': 'Physical and mental health of older people, family networks, and economic readiness for old age. Built with the Asian Development Bank.',
    'ilas.contents': 'Microdata, questionnaires, caregiver module.',
    'ifls.title': 'Eastern Indonesia Household Life Survey',
    'ifls.desc': 'Multi-topic panel on households and communities in 7 eastern Indonesian provinces.',
    'ifls.fine': 'STATA (.dta), SPSS, codebook PDF. Open with researcher registration.',
    'star.title': 'Aceh Post-Tsunami Recovery Study',
    'star.desc': 'Economic recovery, housing relocation, and social resilience after the tsunami. With Duke University and the World Bank.',
    'star.fine': 'Multi-round panel data.',
    'pubs.title': 'Publications',
    'pubs.summary': 'Request summary',
    'pubs.adb': 'With the Asian Development Bank',
    'tab.all': 'All',
    'tab.aging': 'Aging',
    'tab.health': 'Health',
    'tab.econ': 'Economy',
    'about.title': 'About SurveyMETER',
    'about.p1': 'Our name stands for Survey, Measurement, Training, and Research. The institute was formed by a team with more than 15 years of experience running Indonesia Family Life Survey data collection with RAND Corporation.',
    'leaders.title': 'Executive directors',
    'leaders.now': 'since Feb 2024',
    'tl.1': 'Yayasan SurveyMETER founded in Yogyakarta on 20 February.',
    'tl.2': 'Took on a stronger role in public policy research and advocacy.',
    'tl.3': 'Became PT SurveyMETER to expand international research partnerships.',
    'partners.title': 'We have worked with',
    'partners.g1': 'Donors and multilaterals',
    'partners.g2': 'Research and universities',
    'partners.g3': 'Government',
    'footer.title': 'Yogyakarta office',
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

  const ID = { 'nav.close': 'Tutup', 'facts.play': 'Putar fakta' };
  $$('[data-i18n]').forEach(el => { ID[el.dataset.i18n] ??= el.textContent; });
  $$('[data-i18n-placeholder]').forEach(el => { ID[el.dataset.i18nPlaceholder] ??= el.placeholder; });

  let lang = 'id';
  const t = key => (lang === 'en' ? EN : ID)[key] ?? ID[key] ?? key;

  function setLang(next) {
    lang = next;
    document.documentElement.lang = next;
    $$('[data-i18n]').forEach(el => { el.textContent = t(el.dataset.i18n); });
    $$('[data-i18n-placeholder]').forEach(el => { el.placeholder = t(el.dataset.i18nPlaceholder); });
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

  const search = $('#dataset-search');
  const datasets = $$('[data-dataset]');
  const empty = $('#dataset-empty');
  function runSearch() {
    const q = search.value.trim();
    const terms = q.toLowerCase().split(/\s+/).filter(Boolean);
    let shown = 0;
    datasets.forEach(el => {
      const hay = (el.dataset.search + ' ' + el.textContent).toLowerCase();
      const match = terms.every(term => hay.includes(term));
      el.hidden = !match;
      if (match) shown++;
    });
    $('#empty-term').textContent = `"${q}"`;
    empty.hidden = shown > 0;
  }
  search.addEventListener('input', runSearch);
  $('#search-clear').addEventListener('click', () => {
    search.value = '';
    runSearch();
    search.focus();
  });

  const tabs = $$('.tab');
  const pubs = $$('.pub');
  tabs.forEach(tab => tab.addEventListener('click', () => {
    tabs.forEach(other => other.setAttribute('aria-selected', String(other === tab)));
    const f = tab.dataset.filter;
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

  function slider(slides, start = 0) {
    let i = start;
    return step => {
      slides[i].hidden = true;
      slides[i].classList.remove('is-active');
      i = (i + step + slides.length) % slides.length;
      slides[i].hidden = false;
      slides[i].classList.add('is-active');
    };
  }

  function deal(tile) {
    tile.classList.add('is-dealing');
    setTimeout(() => tile.classList.remove('is-dealing'), 320);
  }

  const factsTile = $('.tile--facts');
  const ringFill = $('.ring__fill', factsTile);
  const ringLabel = $('#facts-toggle span');
  const nextFact = slider($$('.fact', factsTile));
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function setFactsState(state) {
    factsTile.dataset.state = state;
    ringLabel.dataset.i18n = state === 'playing' ? 'facts.pause' : 'facts.play';
    ringLabel.textContent = t(ringLabel.dataset.i18n);
  }
  function restartRing() {
    ringFill.style.animation = 'none';
    void ringFill.getBoundingClientRect();
    ringFill.style.animation = '';
  }
  ringFill.addEventListener('animationend', () => {
    nextFact(1);
    deal(factsTile);
    restartRing();
  });
  $('#facts-toggle').addEventListener('click', () => {
    const state = factsTile.dataset.state;
    if (state === 'playing') setFactsState('paused');
    else {
      if (state === 'stopped') restartRing();
      setFactsState('playing');
    }
  });
  setFactsState(reduceMotion ? 'stopped' : 'playing');

  const pubsTile = $('.tile--pubs');
  const stepQuote = slider($$('.quote', pubsTile));
  $$('.arrow', pubsTile).forEach(btn => btn.addEventListener('click', () => {
    stepQuote(Number(btn.dataset.step));
    deal(pubsTile);
  }));

  $('#year').textContent = new Date().getFullYear();
})();
