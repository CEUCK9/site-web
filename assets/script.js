/* Interactions du site CEUC : menu mobile, sous-menus tactiles, lightbox. */
(function () {
  "use strict";

  /* ---------------------------------------------------------- Menu mobile */
  var burger = document.querySelector(".burger");
  var nav = document.getElementById("nav-principal");

  if (burger && nav) {
    burger.addEventListener("click", function () {
      var open = burger.getAttribute("aria-expanded") === "true";
      burger.setAttribute("aria-expanded", String(!open));
      burger.setAttribute("aria-label", open ? "Ouvrir le menu" : "Fermer le menu");
      nav.classList.toggle("is-open", !open);
      document.body.style.overflow = !open ? "hidden" : "";
    });

    // Sur mobile, le premier tap sur un parent ouvre le sous-menu au lieu de naviguer.
    nav.querySelectorAll(".nav__item--has-sub > a").forEach(function (link) {
      link.addEventListener("click", function (ev) {
        if (window.matchMedia("(min-width: 1201px)").matches) return;
        var item = link.parentElement;
        if (!item.classList.contains("is-open")) {
          ev.preventDefault();
          nav.querySelectorAll(".nav__item--has-sub.is-open").forEach(function (o) {
            if (o !== item) o.classList.remove("is-open");
          });
          item.classList.add("is-open");
        }
      });
    });

    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" && nav.classList.contains("is-open")) burger.click();
    });
  }

  /* ------------------------------------------------------------- Lightbox */
  var links = Array.prototype.slice.call(document.querySelectorAll(".gal__link"));
  if (links.length) {
    var current = 0;
    var box = document.createElement("div");
    box.className = "lb";
    box.setAttribute("role", "dialog");
    box.setAttribute("aria-modal", "true");
    box.setAttribute("aria-label", "Visionneuse de photos");
    box.innerHTML =
      '<button class="lb__close" type="button" aria-label="Fermer">&times;</button>' +
      '<button class="lb__nav lb__nav--prev" type="button" aria-label="Photo précédente">&#8249;</button>' +
      '<button class="lb__nav lb__nav--next" type="button" aria-label="Photo suivante">&#8250;</button>' +
      '<div><img class="lb__img" alt=""><p class="lb__cap"></p></div>';
    document.body.appendChild(box);

    var img = box.querySelector(".lb__img");
    var cap = box.querySelector(".lb__cap");
    var lastFocus = null;

    function show(i) {
      current = (i + links.length) % links.length;
      var link = links[current];
      var thumb = link.querySelector("img");
      img.src = link.getAttribute("href");
      img.alt = thumb ? thumb.alt : "";
      cap.textContent = thumb ? thumb.alt : "";
    }

    function open(i) {
      lastFocus = document.activeElement;
      show(i);
      box.classList.add("is-open");
      document.body.style.overflow = "hidden";
      box.querySelector(".lb__close").focus();
    }

    function close() {
      box.classList.remove("is-open");
      document.body.style.overflow = "";
      if (lastFocus) lastFocus.focus();
    }

    links.forEach(function (link, i) {
      link.addEventListener("click", function (ev) {
        ev.preventDefault();
        open(i);
      });
    });

    box.querySelector(".lb__close").addEventListener("click", close);
    box.querySelector(".lb__nav--prev").addEventListener("click", function () { show(current - 1); });
    box.querySelector(".lb__nav--next").addEventListener("click", function () { show(current + 1); });
    box.addEventListener("click", function (ev) { if (ev.target === box) close(); });

    document.addEventListener("keydown", function (ev) {
      if (!box.classList.contains("is-open")) return;
      if (ev.key === "Escape") close();
      if (ev.key === "ArrowLeft") show(current - 1);
      if (ev.key === "ArrowRight") show(current + 1);
    });
  }

  /* ------------------------------------------------- Année du copyright */
  var annee = document.getElementById("annee");
  if (annee) annee.textContent = new Date().getFullYear();
})();
