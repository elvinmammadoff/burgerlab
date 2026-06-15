/* ==========================================================================
   BurgerLab — Documentation behavior
   Mobile sidebar toggle, scrollspy (active TOC link), current year.
   Vanilla, dependency-free.
   ========================================================================== */
(function () {
  "use strict";

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  ready(function () {
    initSidebar();
    initScrollSpy();
    document.querySelectorAll("[data-year]").forEach(function (el) {
      el.textContent = new Date().getFullYear();
    });
  });

  /* ----- Mobile sidebar ----- */
  function initSidebar() {
    var toggle = document.querySelector(".docs-menu-toggle");
    var sidebar = document.getElementById("docs-sidebar");
    var overlay = document.querySelector(".docs-sidebar__overlay");
    if (!toggle || !sidebar) return;

    var open = function () {
      sidebar.classList.add("is-open");
      if (overlay) overlay.classList.add("is-open");
      toggle.setAttribute("aria-expanded", "true");
    };
    var close = function () {
      sidebar.classList.remove("is-open");
      if (overlay) overlay.classList.remove("is-open");
      toggle.setAttribute("aria-expanded", "false");
    };

    toggle.addEventListener("click", function () {
      if (sidebar.classList.contains("is-open")) close();
      else open();
    });
    if (overlay) overlay.addEventListener("click", close);
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") close(); });
    sidebar.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { if (window.innerWidth < 1024) close(); });
    });
  }

  /* ----- Scrollspy: highlight the TOC link for the section in view ----- */
  function initScrollSpy() {
    var links = Array.prototype.slice.call(document.querySelectorAll(".docs-nav a"));
    if (!links.length || !("IntersectionObserver" in window)) return;
    var byId = {};
    links.forEach(function (a) {
      var id = (a.getAttribute("href") || "").replace("#", "");
      if (id) byId[id] = a;
    });
    var sections = Object.keys(byId)
      .map(function (id) { return document.getElementById(id); })
      .filter(Boolean);

    var setActive = function (id) {
      links.forEach(function (a) { a.classList.remove("is-active"); });
      if (byId[id]) byId[id].classList.add("is-active");
    };

    // Highlight the first section by default, before anything has scrolled
    // into the observer's margin (e.g. while the hero is still in view).
    if (sections[0]) setActive(sections[0].id);

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) setActive(entry.target.id);
      });
    }, { rootMargin: "-80px 0px -65% 0px", threshold: 0 });

    sections.forEach(function (s) { io.observe(s); });
  }
})();
