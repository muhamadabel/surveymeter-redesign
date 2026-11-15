(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const desktop = window.matchMedia('(min-width: 1101px)');

  // Mobile menu
  const toggle = $('#nav-toggle');
  const menu = $('#nav-menu');
  const isOpen = () => toggle.getAttribute('aria-expanded') === 'true';
  function setMenu(open) {
    toggle.setAttribute('aria-expanded', String(open));
    menu.classList.toggle('is-open', open);
    document.body.classList.toggle('is-locked', open);
    $('span', toggle).textContent = open ? toggle.dataset.labelClose : toggle.dataset.labelOpen;
    if (!open) closePanels();
  }
  toggle.addEventListener('click', () => setMenu(!isOpen()));
  desktop.addEventListener('change', e => { if (e.matches) setMenu(false); });

  // Mega menu: a button per top item opens its panel. Hover opens on desktop too.
  const buttons = $$('.menu__btn');
  function setPanel(btn, open) {
    btn.setAttribute('aria-expanded', String(open));
    document.getElementById(btn.getAttribute('aria-controls')).hidden = !open;
  }
  function closePanels(except) {
    buttons.forEach(b => { if (b !== except) setPanel(b, false); });
  }
  buttons.forEach(btn => {
    const item = btn.closest('.menu__item');
    let timer;
    btn.addEventListener('click', () => {
      const open = btn.getAttribute('aria-expanded') !== 'true';
      closePanels(btn);
      setPanel(btn, open);
    });
    item.addEventListener('mouseenter', () => {
      if (!desktop.matches) return;
      clearTimeout(timer);
      closePanels(btn);
      setPanel(btn, true);
    });
    item.addEventListener('mouseleave', () => {
      if (!desktop.matches) return;
      timer = setTimeout(() => setPanel(btn, false), 180);
    });
  });
  document.addEventListener('click', e => {
    if (desktop.matches && !e.target.closest('.menu__item')) closePanels();
  });
  document.addEventListener('keydown', e => {
    if (e.key !== 'Escape') return;
    const openBtn = buttons.find(b => b.getAttribute('aria-expanded') === 'true');
    if (openBtn) { setPanel(openBtn, false); openBtn.focus(); return; }
    if (isOpen()) { setMenu(false); toggle.focus(); }
  });
  $$('.mega a').forEach(a => a.addEventListener('focusout', e => {
    const item = a.closest('.menu__item');
    if (desktop.matches && !item.contains(e.relatedTarget)) setPanel($('.menu__btn', item), false);
  }));

  // Tabs (home page): WAI-ARIA pattern with arrow keys, Home and End.
  $$('[role="tablist"]').forEach(list => {
    const tabs = $$('[role="tab"]', list);
    function select(tab, focus) {
      tabs.forEach(other => {
        const on = other === tab;
        other.setAttribute('aria-selected', String(on));
        other.tabIndex = on ? 0 : -1;
        const panel = document.getElementById(other.getAttribute('aria-controls'));
        panel.hidden = !on;
        panel.classList.toggle('is-entering', on);
      });
      if (focus) tab.focus();
    }
    tabs.forEach((tab, i) => {
      tab.addEventListener('click', () => select(tab));
      tab.addEventListener('keydown', e => {
        const step = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
        if (step) {
          e.preventDefault();
          select(tabs[(i + step + tabs.length) % tabs.length], true);
        } else if (e.key === 'Home' || e.key === 'End') {
          e.preventDefault();
          select(tabs[e.key === 'Home' ? 0 : tabs.length - 1], true);
        }
      });
    });
  });

  // Project filter (home page)
  const chips = $$('.chip[data-filter]');
  const rows = $$('.table tbody tr');
  chips.forEach(chip => chip.addEventListener('click', () => {
    chips.forEach(other => other.setAttribute('aria-pressed', String(other === chip)));
    const f = chip.dataset.filter;
    rows.forEach(r => { r.hidden = f !== 'all' && r.dataset.type !== f; });
  }));

  // Search page
  const form = $('.search-box');
  if (form) {
    const input = $('#q', form);
    const status = $('#search-status');
    const list = $('#search-results');
    let index = [];
    const fold = s => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
    const escapeHtml = s => s.replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
    function run() {
      const q = input.value.trim();
      const terms = fold(q).split(/\s+/).filter(Boolean);
      if (!terms.length) { status.textContent = ''; list.innerHTML = ''; return; }
      const hits = index.filter(e => {
        const hay = fold(`${e.t} ${e.s} ${e.x}`);
        return terms.every(t => hay.includes(t));
      }).slice(0, 60);
      status.textContent = hits.length ? `${hits.length} ${form.dataset.count}` : `${form.dataset.none} "${q}"`;
      list.innerHTML = hits.map(e => `<li><a href="${e.u}">${escapeHtml(e.t)}</a><span>${escapeHtml(e.s)}${e.h ? ' &middot; ' + e.h : ''}</span></li>`).join('');
    }
    fetch(form.dataset.searchIndex).then(r => r.json()).then(data => {
      index = data;
      const q = new URLSearchParams(location.search).get('q');
      if (q) input.value = q;
      run();
    });
    input.addEventListener('input', run);
    form.addEventListener('submit', e => e.preventDefault());
  }

  const year = $('#year');
  if (year) year.textContent = new Date().getFullYear();
})();
