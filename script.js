// EdgeVision · Pattern AI Labs — site behavior
(() => {
  const topbar = document.getElementById('topbar');
  const btn    = document.getElementById('navMenu');
  const links  = document.querySelector('.topnav');
  const ctxEl  = document.getElementById('topbarCtx');
  const fill   = document.getElementById('progressFill');

  /* — Mobile menu — */
  btn?.addEventListener('click', () => {
    const open = topbar.classList.toggle('topbar--open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    document.body.style.overflow = open ? 'hidden' : '';
  });
  links?.addEventListener('click', (e) => {
    if (e.target.tagName === 'A') {
      topbar.classList.remove('topbar--open');
      btn?.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    }
  });

  /* — Persistent context label: shows the section the viewer is in — */
  const sections = Array.from(document.querySelectorAll('[data-ctx]'));
  if (sections.length && ctxEl) {
    const ctxObs = new IntersectionObserver(
      (entries) => {
        // Find the entry that's most prominently in view (largest intersection ratio of those visible).
        const visible = entries.filter(e => e.isIntersecting);
        if (!visible.length) return;
        const top = visible.reduce((a, b) =>
          a.intersectionRatio > b.intersectionRatio ? a : b);
        const label = top.target.dataset.ctx;
        if (label && ctxEl.textContent !== label) ctxEl.textContent = label;
      },
      { threshold: [0.15, 0.4, 0.7], rootMargin: '-30% 0px -30% 0px' }
    );
    sections.forEach(s => ctxObs.observe(s));
  }

  /* — Bottom progress bar — */
  const onScroll = () => {
    const h = document.documentElement;
    const total = h.scrollHeight - h.clientHeight;
    const pct = total > 0 ? (h.scrollTop / total) * 100 : 0;
    if (fill) fill.style.width = pct + '%';
  };
  document.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* — Reveal on scroll — */
  const reveal = new IntersectionObserver(
    (entries) => entries.forEach(en => {
      if (en.isIntersecting) {
        en.target.style.opacity = 1;
        en.target.style.transform = 'translateY(0)';
        reveal.unobserve(en.target);
      }
    }),
    { threshold: 0.08, rootMargin: '0px 0px -10% 0px' }
  );
  document.querySelectorAll(
    '.num-card, .circ, .pipe-card, .tl-card, .lens, .week, .contact-card, .feature, .quote, .ll'
  ).forEach(el => {
    el.style.opacity = 0;
    el.style.transform = 'translateY(14px)';
    el.style.transition = 'opacity .55s cubic-bezier(.2,.6,.2,1), transform .55s cubic-bezier(.2,.6,.2,1)';
    reveal.observe(el);
  });

  /* — Animate horizontal heat-mapping bars when they enter view — */
  const heatBars = document.querySelectorAll('.hbar__t');
  const heatObs = new IntersectionObserver((entries) => {
    entries.forEach(en => {
      if (en.isIntersecting) {
        const w = en.target.dataset.w || 0;
        const inner = en.target.querySelector('i');
        inner.style.width = '0%';
        requestAnimationFrame(() => {
          inner.style.transition = 'width 1.2s cubic-bezier(.2,.6,.2,1)';
          inner.style.width = w + '%';
        });
        heatObs.unobserve(en.target);
      }
    });
  }, { threshold: 0.3 });
  heatBars.forEach(b => heatObs.observe(b));
})();
