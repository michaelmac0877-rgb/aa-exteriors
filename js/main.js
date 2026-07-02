/* A&A Exteriors — site interactions */
(function () {
  "use strict";

  /* ---- Mobile nav toggle ------------------------------------------------ */
  var toggle = document.querySelector(".nav__toggle");
  var links = document.getElementById("navLinks");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    links.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        links.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ---- Highlight current page in nav ------------------------------------ */
  var here = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav__links a").forEach(function (a) {
    var href = a.getAttribute("href");
    if (href === here || (here === "index.html" && href === "index.html")) {
      a.classList.add("is-active");
    }
  });

  /* ---- Reveal on scroll -------------------------------------------------- */
  var revealables = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealables.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    revealables.forEach(function (el) { io.observe(el); });
  } else {
    revealables.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---- Current year in footer ------------------------------------------- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ---- Estimate form: AJAX submit to Formspree -------------------------- */
  var form = document.getElementById("estimateForm");
  if (form) {
    var msg = document.getElementById("formMsg");
    form.addEventListener("submit", function (ev) {
      // If the form still has the placeholder endpoint, let the user know.
      var action = form.getAttribute("action") || "";
      if (action.indexOf("YOUR_FORM_ID") !== -1) {
        ev.preventDefault();
        showMsg("err", "This form isn’t connected yet. Add your Formspree form ID in estimate.html (see README).");
        return;
      }

      ev.preventDefault();
      var btn = form.querySelector("[type=submit]");
      var original = btn ? btn.textContent : "";
      if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }

      fetch(action, {
        method: "POST",
        body: new FormData(form),
        headers: { Accept: "application/json" }
      })
        .then(function (res) {
          if (res.ok) {
            form.reset();
            showMsg("ok", "Thank you! Your request has been received. A member of our team will reach out shortly to schedule your free estimate.");
          } else {
            return res.json().then(function (d) {
              var err = (d && d.errors && d.errors.map(function (e) { return e.message; }).join(", ")) || "Something went wrong.";
              showMsg("err", err + " You can also call us at 469-496-7500.");
            });
          }
        })
        .catch(function () {
          showMsg("err", "Network error — please try again, or call us at 469-496-7500.");
        })
        .finally(function () {
          if (btn) { btn.disabled = false; btn.textContent = original; }
        });
    });

    function showMsg(type, text) {
      if (!msg) return;
      msg.className = "form-msg " + type;
      msg.textContent = text;
      msg.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  }
})();
