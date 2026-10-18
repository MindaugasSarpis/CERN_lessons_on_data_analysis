// Diagrams on every workbook page, and the step view of seminar pages.
//
// Step view: one step at a time, full screen, for the
// person at the front reading the page on a tablet. A step is one numbered
// item of a section, its Check line, or its Task. Opens with the "Steps"
// button or with #steps in the address; arrows, space, swipe or the buttons
// move; Escape closes. The position is remembered per page (where storage
// works).
(function () {
  "use strict";

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  function flattenTabs(root) {
    root.querySelectorAll(".tabbed-set").forEach(function (set) {
      var labels = set.querySelectorAll(".tabbed-labels > label");
      var blocks = set.querySelectorAll(".tabbed-content > .tabbed-block");
      var out = document.createElement("div");
      out.className = "steps-tabs";
      blocks.forEach(function (block, i) {
        var label = document.createElement("div");
        label.className = "steps-tab-label";
        label.textContent = labels[i] ? labels[i].textContent : "";
        out.appendChild(label);
        while (block.firstChild) out.appendChild(block.firstChild);
      });
      set.replaceWith(out);
    });
    root.querySelectorAll("[id]").forEach(function (el) { el.removeAttribute("id"); });
    return root;
  }

  // Diagrams: a ```mermaid block becomes <pre class="diagram"> (mkdocs.yml)
  // and is drawn here, on every page, with its source kept in
  // data-source so that the step view can draw it again.
  var MERMAID = "https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.min.js";
  var diagramCount = 0;
  var mermaidReady = null;

  function loadMermaid() {
    if (!mermaidReady) {
      mermaidReady = new Promise(function (resolve, reject) {
        var s = document.createElement("script");
        s.src = MERMAID;
        s.onload = function () {
          window.mermaid.initialize({ startOnLoad: false, theme: "dark", fontFamily: "Inter, sans-serif" });
          resolve(window.mermaid);
        };
        s.onerror = reject;
        document.head.appendChild(s);
      });
    }
    return mermaidReady;
  }

  function draw(div) {
    loadMermaid().then(function (mermaid) {
      return mermaid.render("diagram-" + (diagramCount++), div.dataset.source);
    }).then(function (out) { div.innerHTML = out.svg; }).catch(function () {
      div.textContent = div.dataset.source;
    });
  }

  function drawDiagrams() {
    document.querySelectorAll("pre.diagram").forEach(function (pre) {
      var div = document.createElement("div");
      div.className = "diagram";
      div.dataset.source = pre.textContent;
      pre.replaceWith(div);
      draw(div);
    });
  }

  function clone(el) {
    var copy = el.cloneNode(true);
    copy.querySelectorAll ? copy.querySelectorAll("div.diagram").forEach(function (d) {
      d.innerHTML = "";
      draw(d);
    }) : null;
    if (copy.classList && copy.classList.contains("diagram")) { copy.innerHTML = ""; draw(copy); }
    return flattenTabs(copy);
  }

  // A step keeps its source elements and is copied when shown, so that
  // diagrams drawn after the page loaded are in the copy.
  function Body(make) { this.make = make; }

  function buildSteps(article) {
    var steps = [];
    var part = "";
    var section = null;   // {title, meta, anchor}
    var pending = null;   // last Task step, to attach its Answer
    var intro = document.createElement("div");
    var inIntro = true;

    Array.prototype.forEach.call(article.children, function (el) {
      var tag = el.tagName;
      if (inIntro && tag === "HR") { inIntro = false; return; }
      if (tag === "H2" && !inIntro) {
        part = el.textContent.replace(/¶$/, "").trim();
        section = null;
        return;
      }
      if (inIntro) {
        if (tag !== "HR" && !el.classList.contains("md-source-file")) intro.appendChild(clone(el));
        return;
      }
      if (tag === "H3") {
        section = {
          title: el.textContent.replace(/¶$/, "").trim(),
          meta: "",
          anchor: el.id,
          n: 0
        };
        pending = null;
        return;
      }
      if (!section || tag === "HR") return;
      // The sentence of purpose right under a section's heading (its clock
      // is an HTML comment, not shown) is the section's subtitle.
      var first = section.n === 0;
      section.n = 1;
      if (tag === "P" && first && !/^\s*Check:/.test(el.textContent) && el.textContent.length < 300) {
        section.meta = el.textContent.trim();
        return;
      }
      if (tag === "OL") {
        Array.prototype.forEach.call(el.children, function (li, i) {
          var body = new Body(function () {
            var box = document.createElement("ol");
            box.start = i + 1;
            box.appendChild(clone(li));
            return box;
          });
          steps.push({ part: part, section: section, kind: "Step " + (i + 1) + " of " + el.children.length, body: body });
        });
        pending = null;
        return;
      }
      var isAnswer = tag === "DETAILS" && /answer/i.test(el.textContent.slice(0, 40));
      if (isAnswer && pending) {
        pending.els.push(el);
        return;
      }
      var kind = "Note";
      if (/^\s*Check:/.test(el.textContent)) kind = "Check";
      else if (el.classList.contains("question")) kind = "Task";
      else if (el.classList.contains("warning")) kind = "Watch for";
      var els = [el];
      var step = { part: part, section: section, kind: kind, els: els, body: new Body(function () {
        var box = document.createElement("div");
        els.forEach(function (e) { box.appendChild(clone(e)); });
        return box;
      }) };
      steps.push(step);
      pending = kind === "Task" ? step : null;
    });

    steps.unshift({ part: "", section: { title: "Start", meta: "", anchor: "" }, kind: "Overview",
      body: new Body(function () { return intro.cloneNode(true); }) });
    return steps;
  }

  ready(function () {
    drawDiagrams();
    if (!/\/seminars\/seminar_\d+/.test(location.pathname)) return;
    var article = document.querySelector("article.md-content__inner");
    if (!article) return;
    var steps = buildSteps(article);
    if (steps.length < 3) return;
    var key = "steps:" + location.pathname;
    var index = 0;

    var view = document.createElement("div");
    view.className = "steps-view";
    view.setAttribute("role", "dialog");
    view.setAttribute("aria-label", "Steps");
    view.hidden = true;
    view.innerHTML =
      '<header class="steps-head"><div class="steps-where"><div class="steps-section"></div>' +
      '<div class="steps-meta"></div></div><button class="steps-close" aria-label="Close">✕</button></header>' +
      '<div class="steps-kind"></div><main class="steps-body md-typeset"></main>' +
      '<footer class="steps-foot"><button class="steps-prev">← Back</button>' +
      '<span class="steps-count"></span><button class="steps-next">Next →</button></footer>';
    document.body.appendChild(view);
    var $ = function (s) { return view.querySelector(s); };

    function show(i) {
      index = Math.max(0, Math.min(steps.length - 1, i));
      var s = steps[index];
      $(".steps-section").textContent = s.section.title;
      $(".steps-meta").textContent = s.section.meta || s.part;
      $(".steps-kind").textContent = s.kind;
      $(".steps-kind").dataset.kind = s.kind;
      var body = $(".steps-body");
      body.innerHTML = "";
      body.appendChild(s.body.make());
      body.scrollTop = 0;
      $(".steps-count").textContent = (index + 1) + " / " + steps.length;
      $(".steps-prev").disabled = index === 0;
      $(".steps-next").disabled = index === steps.length - 1;
      try { localStorage.setItem(key, String(index)); } catch (e) { /* storage blocked */ }
    }

    function open(i) {
      view.hidden = false;
      document.documentElement.classList.add("steps-open");
      show(i);
      if (location.hash !== "#steps") history.replaceState(null, "", "#steps");
    }

    function close() {
      view.hidden = true;
      document.documentElement.classList.remove("steps-open");
      var anchor = steps[index].section.anchor;
      history.replaceState(null, "", anchor ? "#" + anchor : location.pathname);
      if (anchor) {
        var target = document.getElementById(anchor);
        if (target) target.scrollIntoView();
      }
    }

    function firstStepOf(anchor) {
      for (var i = 0; i < steps.length; i++) if (steps[i].section.anchor === anchor) return i;
      return -1;
    }

    $(".steps-next").addEventListener("click", function () { show(index + 1); });
    $(".steps-prev").addEventListener("click", function () { show(index - 1); });
    $(".steps-close").addEventListener("click", close);
    // Links on the start screen jump to the first step of their section.
    $(".steps-body").addEventListener("click", function (ev) {
      var a = ev.target.closest("a[href^='#']");
      if (!a) return;
      var i = firstStepOf(a.getAttribute("href").slice(1));
      if (i >= 0) { ev.preventDefault(); show(i); }
    });
    document.addEventListener("keydown", function (ev) {
      if (view.hidden) return;
      if (ev.key === "ArrowRight" || ev.key === "PageDown" || (ev.key === " " && !ev.shiftKey)) { ev.preventDefault(); show(index + 1); }
      else if (ev.key === "ArrowLeft" || ev.key === "PageUp" || (ev.key === " " && ev.shiftKey)) { ev.preventDefault(); show(index - 1); }
      else if (ev.key === "Escape") close();
    });
    var x0 = null, y0 = null;
    view.addEventListener("touchstart", function (ev) {
      x0 = ev.touches[0].clientX; y0 = ev.touches[0].clientY;
    }, { passive: true });
    view.addEventListener("touchend", function (ev) {
      if (x0 === null) return;
      var dx = ev.changedTouches[0].clientX - x0, dy = ev.changedTouches[0].clientY - y0;
      x0 = null;
      if (Math.abs(dx) > 60 && Math.abs(dx) > 2 * Math.abs(dy)) show(index + (dx < 0 ? 1 : -1));
    }, { passive: true });

    var button = document.createElement("button");
    button.className = "steps-open-button";
    button.textContent = "▶ Steps";
    button.title = "Show this page one step at a time";
    button.addEventListener("click", function () {
      // Start at the section in view, else where the view was left.
      var start = 0;
      var heads = article.querySelectorAll("h3[id]");
      for (var i = 0; i < heads.length; i++) {
        if (heads[i].getBoundingClientRect().top < window.innerHeight / 3) {
          var j = firstStepOf(heads[i].id);
          if (j >= 0) start = j;
        }
      }
      if (start === 0) {
        try { start = parseInt(localStorage.getItem(key) || "0", 10) || 0; } catch (e) { start = 0; }
      }
      open(start);
    });
    document.body.appendChild(button);

    if (location.hash === "#steps") {
      var saved = 0;
      try { saved = parseInt(localStorage.getItem(key) || "0", 10) || 0; } catch (e) { saved = 0; }
      open(saved);
    }
  });
})();
