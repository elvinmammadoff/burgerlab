/* ==========================================================================
   BurgerLab — main.js
   Vanilla JS (no jQuery). Single IIFE. Progressive-enhancement first:
   nothing here is allowed to keep the preloader from disappearing.
   ========================================================================== */

(function () {
  "use strict";

  /* ----- Config ------------------------------------------------------------
     Web3Forms public access key. Sign up free at https://web3forms.com,
     create your own key, and replace the value below — that's the only edit
     needed to receive reservation & contact submissions in your inbox. */
  var BL = {
    WEB3FORMS_KEY: "1689852d-c68d-46fa-977e-51c4bc04d29a",
  };
  window.BL_CONFIG = BL;

  var prefersReduced = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;
  var isTouch = window.matchMedia("(max-width: 767.98px), (hover: none)").matches;
  var hasGSAP = !!(window.gsap && window.ScrollTrigger);

  if (!hasGSAP) document.documentElement.classList.add("no-gsap");
  if (hasGSAP) gsap.registerPlugin(ScrollTrigger);

  var ready = function (fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  };

  ready(function () {
    initPreloader();
    initNav();
    initHeroVideo();
    initMarquee();
    initReveals();
    initStatsCounter();
    initReviewsSlider();
    initExpChips();
    initFavButtons();
    initMenuFilter();
    initFancybox();
    initForms();
    initToTop();
    initYear();
  });

  /* ----- Preloader (always hides — window load OR 5s failsafe) ----- */
  function initPreloader() {
    var pre = document.querySelector(".bl-preloader");
    if (!pre) {
      document.body.classList.add("is-loaded");
      return;
    }
    var bar = pre.querySelector(".bl-preloader__bar span");
    var count = pre.querySelector(".bl-preloader__count");
    var done = false;

    var finish = function () {
      if (done) return;
      done = true;
      pre.style.opacity = "0";
      pre.style.transition = "opacity .5s ease";
      setTimeout(function () {
        pre.style.display = "none";
      }, 520);
      document.body.classList.add("is-loaded");
      playHero();
    };

    // MANDATORY failsafe: never trap the visitor behind the overlay.
    var failsafe = setTimeout(finish, 5000);

    if (hasGSAP && !prefersReduced) {
      var obj = { v: 0 };
      gsap.to(obj, {
        v: 100,
        duration: 1.4,
        ease: "power2.inOut",
        onUpdate: function () {
          var n = Math.round(obj.v);
          if (count) count.textContent = String(n).padStart(3, "0") + " / 100";
          if (bar) bar.style.width = n + "%";
        },
        onComplete: function () {
          clearTimeout(failsafe);
          finish();
        },
      });
    } else {
      // No animation lib (or reduced motion) — hide on window load, capped at 5s.
      window.addEventListener("load", function () {
        clearTimeout(failsafe);
        finish();
      });
    }
  }

  /* ----- Header / nav ----- */
  function initNav() {
    var header = document.querySelector(".bl-header");
    if (header) {
      var onScroll = function () {
        header.classList.toggle("is-scrolled", window.scrollY > 60);
      };
      window.addEventListener("scroll", onScroll, { passive: true });
      onScroll();
    }

    // Mobile drawer
    var burger = document.querySelector(".bl-burger");
    var menu = document.querySelector(".bl-mobile-menu");
    var closeBtn = document.querySelector(".bl-mobile-menu__close");
    if (burger && menu) {
      var open = function () {
        menu.classList.add("is-open");
        burger.classList.add("is-active");
        burger.setAttribute("aria-expanded", "true");
        document.body.style.overflow = "hidden";
      };
      var close = function () {
        menu.classList.remove("is-open");
        burger.classList.remove("is-active");
        burger.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      };
      burger.addEventListener("click", function () {
        menu.classList.contains("is-open") ? close() : open();
      });
      if (closeBtn) closeBtn.addEventListener("click", close);
      menu.querySelectorAll("a").forEach(function (a) {
        a.addEventListener("click", close);
      });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape") close();
      });
      // If the viewport grows to desktop while the drawer is open, close it
      // and release the body scroll-lock (the drawer is mobile-only).
      var mqDesktop = window.matchMedia("(min-width: 1024px)");
      var onMqChange = function (e) {
        if (e.matches) close();
      };
      if (mqDesktop.addEventListener) mqDesktop.addEventListener("change", onMqChange);
      else if (mqDesktop.addListener) mqDesktop.addListener(onMqChange);
    }

    // Smooth anchor scrolling (native)
    document.querySelectorAll('a[href^="#"]').forEach(function (a) {
      a.addEventListener("click", function (e) {
        var id = a.getAttribute("href");
        if (!id || id.length < 2) return;
        var target = document.querySelector(id);
        if (!target) return;
        e.preventDefault();
        target.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });
  }

  /* ----- Hero background video -----
     Plain autoplaying, muted, looped background video on desktop. The page
     scrolls normally (no pinning / scroll-scrub). On touch/small screens the
     video is hidden via CSS and the lightweight poster image is shown instead,
     so phones never download the full clip. */
  function initHeroVideo() {
    var hero = document.querySelector(".bl-hero");
    var video = hero && hero.querySelector(".bl-hero__video");
    if (!hero || !video) return;

    // Touch / small screens: poster only — don't fetch or play the video.
    if (isTouch) {
      video.pause();
      return;
    }

    // Desktop: buffer + autoplay loop in the background.
    video.preload = "auto";
    video.loop = true;
    video.muted = true;
    var p = video.play();
    if (p && p.catch) p.catch(function () {});
  }

  /* ----- Marquee (duplicate track for seamless 50% loop) ----- */
  function initMarquee() {
    document.querySelectorAll(".bl-ticker__track").forEach(function (track) {
      track.innerHTML = track.innerHTML + track.innerHTML;
    });
  }

  /* ----- Hero kinetic reveal (runs after preloader) ----- */
  function playHero() {
    if (!hasGSAP || prefersReduced) return;
    var lines = document.querySelectorAll(".bl-hero__title .bl-line");
    if (lines.length) {
      gsap.set(lines, { yPercent: 110 });
      gsap.to(lines, {
        yPercent: 0,
        duration: 1.2,
        ease: "expo.out",
        stagger: 0.08,
      });
    }
    gsap.from(".bl-hero__chips, .bl-hero__lede, .bl-hero__actions, .bl-order-card", {
      y: 30,
      opacity: 0,
      duration: 1,
      delay: 0.4,
      ease: "power3.out",
      stagger: 0.12,
    });
  }

  /* ----- Scroll reveals ----- */
  function initReveals() {
    if (!hasGSAP || prefersReduced) {
      // Reveal everything immediately (CSS .no-gsap handles the static case too).
      document
        .querySelectorAll(".bl-reveal-up, .bl-reveal-fade")
        .forEach(function (el) {
          el.style.opacity = "1";
          el.style.transform = "none";
        });
      return;
    }

    // toggleActions: onEnter onLeave onEnterBack onLeaveBack.
    // "play none none reverse" => animate in on scroll-down, animate back out
    // on scroll-up, then play again the next time it scrolls into view.
    var TA = "play none none reverse";

    gsap.utils.toArray(".bl-reveal-up").forEach(function (el) {
      gsap.fromTo(
        el,
        { y: 40, opacity: 0 },
        {
          y: 0,
          opacity: 1,
          duration: 1,
          ease: "power3.out",
          scrollTrigger: { trigger: el, start: "top 85%", toggleActions: TA },
        }
      );
    });
    gsap.utils.toArray(".bl-reveal-fade").forEach(function (el) {
      gsap.fromTo(
        el,
        { opacity: 0 },
        {
          opacity: 1,
          duration: 1.2,
          ease: "power2.out",
          scrollTrigger: { trigger: el, start: "top 88%", toggleActions: TA },
        }
      );
    });
    gsap.utils.toArray("[data-stagger]").forEach(function (parent) {
      var children = parent.querySelectorAll("[data-stagger-item]");
      if (!children.length) return;
      gsap.fromTo(
        children,
        { y: 40, opacity: 0 },
        {
          y: 0,
          opacity: 1,
          duration: 0.9,
          ease: "power3.out",
          stagger: 0.1,
          scrollTrigger: { trigger: parent, start: "top 82%", toggleActions: TA },
        }
      );
    });
  }

  /* ----- Stats counter ----- */
  function initStatsCounter() {
    var nums = document.querySelectorAll(".bl-stat__num[data-count]");
    if (!nums.length) return;
    nums.forEach(function (el) {
      var target = parseFloat(el.dataset.count);
      var suffix = el.dataset.suffix || "";
      if (!hasGSAP || prefersReduced) {
        el.textContent = target.toLocaleString() + suffix;
        return;
      }
      var obj = { v: 0 };
      var render = function () {
        el.textContent = Math.round(obj.v).toLocaleString() + suffix;
      };
      // Count up each time it scrolls into view; reset on the way back up.
      gsap.fromTo(
        obj,
        { v: 0 },
        {
          v: target,
          duration: 2,
          ease: "power2.out",
          onUpdate: render,
          scrollTrigger: {
            trigger: el,
            start: "top 88%",
            toggleActions: "restart none none reverse",
          },
        }
      );
    });
  }

  /* ----- Reviews slider ----- */
  function initReviewsSlider() {
    if (!window.Swiper) return;
    var el = document.querySelector(".bl-reviews__slider");
    if (!el) return;
    new Swiper(el, {
      loop: true,
      autoplay: { delay: 6000, disableOnInteraction: false },
      effect: "fade",
      fadeEffect: { crossFade: true },
      speed: 800,
      pagination: { el: ".bl-reviews__pagination", clickable: true },
    });
  }

  /* ----- Ordering experience meal chips ----- */
  function initExpChips() {
    var groups = document.querySelectorAll(".bl-exp__chips");
    groups.forEach(function (group) {
      var btns = group.querySelectorAll("button");
      btns.forEach(function (btn) {
        btn.addEventListener("click", function () {
          btns.forEach(function (b) {
            b.classList.remove("is-active");
          });
          btn.classList.add("is-active");
        });
      });
    });
  }

  /* ----- Favourite buttons ----- */
  function initFavButtons() {
    document.querySelectorAll("[data-fav]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var active = btn.classList.toggle("is-active");
        btn.setAttribute("aria-pressed", active ? "true" : "false");
      });
    });
  }

  /* ----- Menu / catalog filter (used on menu pages) ----- */
  function initMenuFilter() {
    var filters = document.querySelectorAll(".bl-filter__btn");
    if (!filters.length) return;
    var items = document.querySelectorAll("[data-cat]");
    filters.forEach(function (btn) {
      btn.addEventListener("click", function () {
        filters.forEach(function (b) {
          b.classList.remove("is-active");
        });
        btn.classList.add("is-active");
        var cat = btn.dataset.filter;
        items.forEach(function (item) {
          var show = cat === "all" || item.dataset.cat === cat;
          item.style.display = show ? "" : "none";
        });
        if (hasGSAP) ScrollTrigger.refresh();
      });
    });
  }

  /* ----- Fancybox lightbox (gallery pages) ----- */
  function initFancybox() {
    if (!window.Fancybox) return;
    window.Fancybox.bind('[data-fancybox]', {
      Hash: false,
      compact: false,
      Thumbs: { type: "classic" }
    });
  }

  /* ----- Forms (Web3Forms AJAX submit) ----- */
  function initForms() {
    document.querySelectorAll("form[data-form]").forEach(function (form) {
      var note = form.querySelector(".bl-form__note");
      var btn = form.querySelector('[type="submit"]');
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        if (note) note.className = "bl-form__note";
        var btnText = btn ? btn.textContent : "";
        if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }
        fetch(form.action, {
          method: "POST",
          body: new FormData(form),
          headers: { Accept: "application/json" }
        })
          .then(function (r) { return r.json(); })
          .then(function (data) {
            if (data.success) {
              if (note) { note.textContent = form.dataset.success || "Thanks — we'll be in touch shortly."; note.classList.add("is-success"); }
              form.reset();
            } else {
              if (note) { note.textContent = "Something went wrong. Please try again."; note.classList.add("is-error"); }
            }
          })
          .catch(function () {
            if (note) { note.textContent = "Network error. Please try again."; note.classList.add("is-error"); }
          })
          .finally(function () {
            if (btn) { btn.disabled = false; btn.textContent = btnText; }
          });
      });
    });
  }

  /* ----- Back to top ----- */
  function initToTop() {
    var btn = document.querySelector(".bl-totop");
    if (!btn) return;
    var onScroll = function () {
      btn.classList.toggle("is-visible", window.scrollY > 600);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    btn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ----- Current year ----- */
  function initYear() {
    document.querySelectorAll("[data-year]").forEach(function (el) {
      el.textContent = new Date().getFullYear();
    });
  }
})();
