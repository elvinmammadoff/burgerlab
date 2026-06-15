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
    initHomeSwitcher();
    initHeroSlider();
    initPickers();
    initCountdown();
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
          b.setAttribute("aria-selected", "false");
        });
        btn.classList.add("is-active");
        btn.setAttribute("aria-selected", "true");
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

  /* ----- Countdown (coming-soon page) ----- */
  function initCountdown() {
    var el = document.querySelector("[data-countdown]");
    if (!el) return;
    var target = new Date(el.dataset.countdown).getTime();
    var nums = {
      days: el.querySelector('[data-cd="days"]'),
      hours: el.querySelector('[data-cd="hours"]'),
      minutes: el.querySelector('[data-cd="minutes"]'),
      seconds: el.querySelector('[data-cd="seconds"]'),
    };
    var pad = function (n) { return String(n).padStart(2, "0"); };
    var render = function () {
      var diff = Math.max(0, target - Date.now());
      var sec = Math.floor(diff / 1000);
      if (nums.days) nums.days.textContent = pad(Math.floor(sec / 86400));
      if (nums.hours) nums.hours.textContent = pad(Math.floor((sec % 86400) / 3600));
      if (nums.minutes) nums.minutes.textContent = pad(Math.floor((sec % 3600) / 60));
      if (nums.seconds) nums.seconds.textContent = pad(sec % 60);
    };
    render();
    setInterval(render, 1000);
  }

  /* ----- Home variant switcher ----- */
  function initHomeSwitcher() {
    var el = document.querySelector("[data-home-switcher]");
    if (!el) return;
    var btn = el.querySelector(".bl-home-switcher__btn");
    var close = function () {
      el.classList.remove("is-open");
      btn.setAttribute("aria-expanded", "false");
    };
    btn.addEventListener("click", function () {
      var open = el.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("click", function (e) {
      if (!el.contains(e.target)) close();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") close();
    });
  }

  /* ----- Custom date & time pickers (reservation form) -----
     Replaces native type="date"/type="time" with brand-themed widgets:
     a calendar grid and an analog clock. Each input keeps a human value
     (e.g. "Jun 14, 2026" / "7:30 PM") for the email, plus a machine value
     in dataset.value (ISO date / 24h time) for reliable re-parsing. */
  function initPickers() {
    var MONTHS = ["January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"];
    var MONTHS_SHORT = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
      "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    var WEEKDAYS = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"];
    var open = null; // { wrap, pop, input }

    function pad(n) { return (n < 10 ? "0" : "") + n; }

    function closeOpen() {
      if (!open) return;
      open.wrap.classList.remove("is-open");
      open.pop.setAttribute("hidden", "");
      open.input.setAttribute("aria-expanded", "false");
      open = null;
    }

    // One shared outside-click / Escape handler for whichever pop is open.
    // Runs on the CAPTURE phase, before any delegated click handler inside
    // the popover can re-render (and thus detach) the clicked element —
    // otherwise the bubbling click would see a detached e.target and look
    // like an "outside" click, slamming the popover shut on every selection.
    document.addEventListener("click", function (e) {
      if (open && !open.wrap.contains(e.target)) closeOpen();
    }, true);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeOpen();
    });

    // Shared trigger wiring: block typing, open on click/focus/keydown.
    function wireTrigger(input, doOpen) {
      input.setAttribute("autocomplete", "off");
      input.setAttribute("inputmode", "none");
      input.setAttribute("role", "combobox");
      input.setAttribute("aria-autocomplete", "none");
      input.setAttribute("aria-haspopup", "dialog");
      input.setAttribute("aria-expanded", "false");
      input.classList.add("bl-input--picker");
      input.addEventListener("click", doOpen);
      input.addEventListener("focus", doOpen);
      input.addEventListener("keydown", function (e) {
        if (e.key === "Tab") return;
        e.preventDefault();
        if (e.key === "Escape") { closeOpen(); return; }
        doOpen();
      });
    }

    /* ---------- Calendar ---------- */
    document.querySelectorAll("[data-datepicker]").forEach(function (wrap) {
      var input = wrap.querySelector("input");
      if (!input) return;

      var pop = document.createElement("div");
      pop.className = "bl-picker__pop bl-datepicker";
      pop.setAttribute("role", "dialog");
      pop.setAttribute("aria-label", "Choose a date");
      pop.setAttribute("hidden", "");
      wrap.appendChild(pop);

      var today = new Date();
      today.setHours(0, 0, 0, 0);
      var viewY, viewM, selected;

      function render() {
        var startDow = new Date(viewY, viewM, 1).getDay();
        var daysInMonth = new Date(viewY, viewM + 1, 0).getDate();
        var html = "";
        html += '<div class="bl-datepicker__head">';
        html += '<button type="button" class="bl-datepicker__nav" data-prev aria-label="Previous month"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg></button>';
        html += '<div class="bl-datepicker__title" aria-live="polite">' + MONTHS[viewM] + " " + viewY + "</div>";
        html += '<button type="button" class="bl-datepicker__nav" data-next aria-label="Next month"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg></button>';
        html += "</div>";
        html += '<div class="bl-datepicker__weekdays">';
        WEEKDAYS.forEach(function (d) { html += "<span>" + d + "</span>"; });
        html += "</div>";
        html += '<div class="bl-datepicker__grid">';
        var i;
        for (i = 0; i < startDow; i++) html += '<span class="bl-datepicker__pad"></span>';
        for (var d = 1; d <= daysInMonth; d++) {
          var cur = new Date(viewY, viewM, d);
          var iso = viewY + "-" + pad(viewM + 1) + "-" + pad(d);
          var isToday = cur.getTime() === today.getTime();
          var isSel = selected && cur.getTime() === selected.getTime();
          var disabled = cur < today;
          var cls = "bl-datepicker__day" + (isToday ? " is-today" : "") + (isSel ? " is-selected" : "");
          html += '<button type="button" class="' + cls + '" data-date="' + iso + '"' +
            (disabled ? " disabled" : "") +
            (isSel ? ' aria-pressed="true"' : "") +
            ' aria-label="' + MONTHS[viewM] + " " + d + ", " + viewY + '">' + d + "</button>";
        }
        html += "</div>";
        html += '<div class="bl-datepicker__foot">';
        html += '<button type="button" class="bl-picker__link" data-today>Today</button>';
        html += '<button type="button" class="bl-picker__link" data-clear>Clear</button>';
        html += "</div>";
        pop.innerHTML = html;
      }

      function commit(date) {
        selected = date;
        if (date) {
          input.value = MONTHS_SHORT[date.getMonth()] + " " + date.getDate() + ", " + date.getFullYear();
          input.dataset.value = date.getFullYear() + "-" + pad(date.getMonth() + 1) + "-" + pad(date.getDate());
        } else {
          input.value = "";
          delete input.dataset.value;
        }
        input.dispatchEvent(new Event("change", { bubbles: true }));
      }

      function doOpen() {
        if (open && open.pop !== pop) closeOpen();
        if (input.dataset.value) {
          var p = input.dataset.value.split("-");
          selected = new Date(+p[0], +p[1] - 1, +p[2]);
          viewY = selected.getFullYear();
          viewM = selected.getMonth();
        } else {
          selected = null;
          viewY = today.getFullYear();
          viewM = today.getMonth();
        }
        render();
        pop.removeAttribute("hidden");
        wrap.classList.add("is-open");
        input.setAttribute("aria-expanded", "true");
        open = { wrap: wrap, pop: pop, input: input };
      }

      wireTrigger(input, doOpen);

      pop.addEventListener("click", function (e) {
        var t = e.target.closest("button");
        if (!t) return;
        if (t.hasAttribute("data-prev")) { if (--viewM < 0) { viewM = 11; viewY--; } render(); return; }
        if (t.hasAttribute("data-next")) { if (++viewM > 11) { viewM = 0; viewY++; } render(); return; }
        if (t.hasAttribute("data-today")) { commit(new Date(today.getTime())); closeOpen(); return; }
        if (t.hasAttribute("data-clear")) { commit(null); render(); return; }
        if (t.hasAttribute("data-date") && !t.disabled) {
          var p = t.getAttribute("data-date").split("-");
          commit(new Date(+p[0], +p[1] - 1, +p[2]));
          closeOpen();
        }
      });
    });

    /* ---------- Analog clock ---------- */
    document.querySelectorAll("[data-timepicker]").forEach(function (wrap) {
      var input = wrap.querySelector("input");
      if (!input) return;

      var pop = document.createElement("div");
      pop.className = "bl-picker__pop bl-clock";
      pop.setAttribute("role", "dialog");
      pop.setAttribute("aria-label", "Choose a time");
      pop.setAttribute("hidden", "");
      wrap.appendChild(pop);

      var mode = "hour";       // "hour" | "minute"
      var hour = 7, minute = 0, ampm = "PM"; // hour is 1-12

      function faceHtml() {
        var R = 96, cx = 120, cy = 120, nums = [], i;
        if (mode === "hour") {
          for (i = 1; i <= 12; i++) nums.push({ label: i, value: i, deg: i * 30 });
        } else {
          for (i = 0; i < 60; i += 5) nums.push({ label: pad(i), value: i, deg: i * 6 });
        }
        var activeDeg = mode === "hour" ? hour * 30 : minute * 6;
        var html = '<div class="bl-clock__hand" style="transform: translateX(-50%) rotate(' + activeDeg + 'deg)"></div>';
        html += '<span class="bl-clock__center"></span>';
        nums.forEach(function (n) {
          var rad = (n.deg - 90) * Math.PI / 180;
          var x = cx + R * Math.cos(rad);
          var y = cy + R * Math.sin(rad);
          var active = (mode === "hour" && n.value === hour) || (mode === "minute" && n.value === minute);
          html += '<button type="button" class="bl-clock__num' + (active ? " is-active" : "") +
            '" data-val="' + n.value + '" style="left:' + x + "px;top:" + y + 'px">' + n.label + "</button>";
        });
        return html;
      }

      function render() {
        var html = '<div class="bl-clock__readout">';
        html += '<button type="button" class="bl-clock__seg' + (mode === "hour" ? " is-active" : "") + '" data-seg="hour" aria-label="Set hour">' + hour + "</button>";
        html += '<span class="bl-clock__colon">:</span>';
        html += '<button type="button" class="bl-clock__seg' + (mode === "minute" ? " is-active" : "") + '" data-seg="minute" aria-label="Set minutes">' + pad(minute) + "</button>";
        html += '<div class="bl-clock__ampm">';
        html += '<button type="button" class="bl-clock__ampm-btn' + (ampm === "AM" ? " is-active" : "") + '" data-ampm="AM">AM</button>';
        html += '<button type="button" class="bl-clock__ampm-btn' + (ampm === "PM" ? " is-active" : "") + '" data-ampm="PM">PM</button>';
        html += "</div></div>";
        html += '<div class="bl-clock__face">' + faceHtml() + "</div>";
        html += '<div class="bl-clock__foot">';
        html += '<button type="button" class="bl-picker__link" data-clock-cancel>Cancel</button>';
        html += '<button type="button" class="bl-btn bl-btn--primary bl-btn--sm" data-clock-ok>Done</button>';
        html += "</div>";
        pop.innerHTML = html;
      }

      function commit() {
        var h24 = hour % 12 + (ampm === "PM" ? 12 : 0);
        input.value = hour + ":" + pad(minute) + " " + ampm;
        input.dataset.value = pad(h24) + ":" + pad(minute);
        input.dispatchEvent(new Event("change", { bubbles: true }));
      }

      function doOpen() {
        if (open && open.pop !== pop) closeOpen();
        if (input.dataset.value) {
          var p = input.dataset.value.split(":");
          var h24 = +p[0];
          minute = +p[1];
          ampm = h24 >= 12 ? "PM" : "AM";
          hour = h24 % 12 || 12;
        } else {
          hour = 7; minute = 0; ampm = "PM";
        }
        mode = "hour";
        render();
        pop.removeAttribute("hidden");
        wrap.classList.add("is-open");
        input.setAttribute("aria-expanded", "true");
        open = { wrap: wrap, pop: pop, input: input };
      }

      wireTrigger(input, doOpen);

      pop.addEventListener("click", function (e) {
        var t = e.target.closest("button");
        if (!t) return;
        if (t.hasAttribute("data-seg")) { mode = t.getAttribute("data-seg"); render(); return; }
        if (t.hasAttribute("data-ampm")) { ampm = t.getAttribute("data-ampm"); render(); return; }
        if (t.classList.contains("bl-clock__num")) {
          var val = +t.getAttribute("data-val");
          if (mode === "hour") { hour = val; mode = "minute"; } else { minute = val; }
          render();
          return;
        }
        if (t.hasAttribute("data-clock-cancel")) { closeOpen(); return; }
        if (t.hasAttribute("data-clock-ok")) { commit(); closeOpen(); }
      });
    });
  }

  /* ----- Hero image slider (home-v2) ----- */
  function initHeroSlider() {
    if (!window.Swiper) return;
    var el = document.querySelector(".bl-hero-slider");
    if (!el) return;
    new Swiper(el, {
      loop: true,
      autoplay: { delay: 7000, disableOnInteraction: false },
      effect: "fade",
      fadeEffect: { crossFade: true },
      speed: 900,
      pagination: { el: ".bl-hero-slider__pagination", clickable: true },
      navigation: {
        nextEl: ".bl-hero-slider__arrow--next",
        prevEl: ".bl-hero-slider__arrow--prev",
      },
    });
  }
})();
