/* ==========================================================================
   BurgerLab — Landing page behavior
   (1) Demo filter chips  (2) Page-transition overlay on demo links.
   Vanilla, dependency-free, respects prefers-reduced-motion.
   ========================================================================== */
(function () {
  "use strict";

  var prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  ready(function () {
    initFilters();
    initTransitions();
  });

  /* ----- Demo filter chips ----- */
  function initFilters() {
    var chips = Array.prototype.slice.call(document.querySelectorAll(".bl-chip"));
    var cards = Array.prototype.slice.call(document.querySelectorAll(".bl-demo-card"));
    if (!chips.length || !cards.length) return;

    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        var filter = chip.getAttribute("data-filter");
        chips.forEach(function (c) { c.classList.remove("is-active"); });
        chip.classList.add("is-active");
        cards.forEach(function (card) {
          var tags = card.getAttribute("data-tags") || "";
          var show = filter === "all" || tags.split(/\s+/).indexOf(filter) !== -1;
          card.classList.toggle("is-hidden", !show);
        });
      });
    });
  }

  /* ----- Page-transition overlay ----- */
  function initTransitions() {
    var overlay = document.getElementById("bl-transition");
    if (!overlay) return;
    var mark = overlay.querySelector(".bl-trans-mark");

    // Reset on back/forward cache restore so the overlay never stays stuck up.
    window.addEventListener("pageshow", function () {
      overlay.classList.remove("is-active");
      overlay.style.transition = "none";
      overlay.style.transform = "scaleY(0)";
      if (mark) mark.style.opacity = "0";
    });

    document.querySelectorAll("a[data-demo-link]").forEach(function (link) {
      link.addEventListener("click", function (e) {
        var href = link.getAttribute("href");
        // Let modified clicks / new-tab behavior pass through untouched.
        if (!href || e.metaKey || e.ctrlKey || e.shiftKey || e.button !== 0 || link.target === "_blank") return;
        if (prefersReduced) return; // native navigation, no animation

        e.preventDefault();
        overlay.classList.add("is-active");
        overlay.style.transition = "transform .5s cubic-bezier(.76,0,.24,1)";
        overlay.style.transformOrigin = "bottom";
        overlay.style.transform = "scaleY(1)";
        if (mark) {
          mark.style.transition = "opacity .35s ease .15s";
          mark.style.opacity = "1";
        }
        var done = false;
        var go = function () { if (done) return; done = true; window.location.href = href; };
        overlay.addEventListener("transitionend", go, { once: true });
        setTimeout(go, 700); // failsafe
      });
    });
  }
})();
