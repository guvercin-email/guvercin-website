/* guvercin.email — the only script on this site.
   Nothing here is required for the page to work; it only improves it. */
(function () {
  "use strict";

  var RELEASES = "https://github.com/herdem-herdem/guvercin-desktop/releases";

  /* ------------------------------------------------------------ platform -- */
  function detect() {
    var d = navigator.userAgentData;
    var p = (d && d.platform) || navigator.platform || "";
    var ua = navigator.userAgent || "";
    var s = (p + " " + ua).toLowerCase();
    if (s.indexOf("android") > -1) return null;
    if (s.indexOf("win") > -1) return "windows";
    if (s.indexOf("mac") > -1 || s.indexOf("iphone") > -1 || s.indexOf("ipad") > -1) {
      // Apple Silicon Macs cannot be told apart reliably; offer the common case
      // and leave both builds one click away on download.html.
      return "macos";
    }
    if (s.indexOf("linux") > -1 || s.indexOf("x11") > -1) return "linux";
    return null;
  }

  /* The few strings this script writes itself, in the two site languages. */
  var LANG = document.documentElement.lang === "tr" ? "tr" : "en";
  var T = {
    en: {
      macos: "Download for macOS — Apple Silicon",
      windows: "Download for Windows",
      linux: "Download for Linux",
      recommended: "recommended for you",
      copied: "copied"
    },
    tr: {
      macos: "macOS için indir — Apple Silicon",
      windows: "Windows için indir",
      linux: "Linux için indir",
      recommended: "senin için önerilen",
      copied: "kopyalandı"
    }
  }[LANG];

  var os = detect();

  if (os) {
    var buttons = document.querySelectorAll("[data-os-button]");
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].textContent = T[os];
    }
    var card = document.querySelector('[data-os-card="' + os + '"]');
    if (card) {
      card.classList.add("card--highlight");
      var slot = card.querySelector("[data-os-pill]");
      if (slot) {
        var pill = document.createElement("span");
        pill.className = "pill pill--yellow";
        pill.textContent = T.recommended;
        slot.appendChild(pill);
      }
    }
  }

  /* --------------------------------------------------------------- theme -- */
  var toggle = document.querySelector(".theme-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var current = document.documentElement.getAttribute("data-theme");
      var next = current === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      toggle.setAttribute("aria-pressed", next === "dark" ? "true" : "false");
      try {
        localStorage.setItem("guvercin-theme", next);
      } catch (e) {
        /* private mode: the choice simply does not persist */
      }
    });
    toggle.setAttribute(
      "aria-pressed",
      document.documentElement.getAttribute("data-theme") === "dark" ? "true" : "false"
    );
  }

  /* ------------------------------------------------------- mobile menu --- */
  var navToggle = document.querySelector(".nav-toggle");
  var panel = document.getElementById("mobile-menu");
  if (navToggle && panel) {
    var open = false;

    var focusables = function () {
      return panel.querySelectorAll("a[href], button:not([disabled])");
    };

    var setOpen = function (state) {
      open = state;
      panel.hidden = !state;
      navToggle.setAttribute("aria-expanded", state ? "true" : "false");
      document.body.style.overflow = state ? "hidden" : "";
      if (state) {
        var f = focusables();
        if (f.length) f[0].focus();
      } else {
        navToggle.focus();
      }
    };

    navToggle.addEventListener("click", function () {
      setOpen(!open);
    });

    document.addEventListener("keydown", function (e) {
      if (!open) return;
      if (e.key === "Escape") {
        setOpen(false);
        return;
      }
      if (e.key !== "Tab") return;
      var f = focusables();
      if (!f.length) return;
      var first = f[0];
      var last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    });

    panel.addEventListener("click", function (e) {
      if (e.target === panel) setOpen(false);
    });

    window.addEventListener("resize", function () {
      if (open && window.innerWidth > 900) setOpen(false);
    });
  }

  /* ------------------------------------------------------------- reveal -- */
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var items = document.querySelectorAll(".reveal");
  if (!reduce && "IntersectionObserver" in window && items.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry, n) {
          if (!entry.isIntersecting) return;
          var el = entry.target;
          var delay = (parseInt(el.getAttribute("data-delay"), 10) || n) * 60;
          setTimeout(function () {
            el.classList.add("is-visible");
          }, Math.min(delay, 300));
          io.unobserve(el);
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.05 }
    );
    for (var j = 0; j < items.length; j++) io.observe(items[j]);
  } else {
    for (var k = 0; k < items.length; k++) items[k].classList.add("is-visible");
  }

  /* --------------------------------------------------------------- copy -- */
  var copyButtons = document.querySelectorAll(".copy-btn");
  for (var m = 0; m < copyButtons.length; m++) {
    (function (btn) {
      btn.hidden = false;
      btn.addEventListener("click", function () {
        var pre = btn.parentNode.querySelector("pre");
        if (!pre) return;
        var text = pre.textContent;
        var done = function () {
          var was = btn.textContent;
          btn.textContent = T.copied;
          setTimeout(function () {
            btn.textContent = was;
          }, 1600);
        };
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(done, function () {});
        } else {
          var ta = document.createElement("textarea");
          ta.value = text;
          document.body.appendChild(ta);
          ta.select();
          try {
            document.execCommand("copy");
            done();
          } catch (e) {
            /* nothing to do — the text is selectable by hand */
          }
          document.body.removeChild(ta);
        }
      });
    })(copyButtons[m]);
  }

  /* ------------------------------------------------------------ language -- */
  /* The picker navigates; picking a language also records the choice, so the
     redirect in the page head stops guessing from then on. */
  var langSelect = document.getElementById("lang-select");
  if (langSelect) {
    langSelect.addEventListener("change", function () {
      var opt = langSelect.options[langSelect.selectedIndex];
      if (!opt || !opt.value) return;
      try {
        localStorage.setItem("guvercin-lang", opt.getAttribute("data-lang"));
      } catch (e) {
        /* private mode: the choice holds for this page load only */
      }
      window.location.href = opt.value;
    });
  }

  /* Keep the releases URL honest even if a button loses its href somehow. */
  var dl = document.querySelectorAll("[data-release-link]");
  for (var n2 = 0; n2 < dl.length; n2++) {
    if (!dl[n2].getAttribute("href")) dl[n2].setAttribute("href", RELEASES);
  }
})();
