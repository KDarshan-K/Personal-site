(() => {
  const grid = document.getElementById("project-grid");
  if (!grid) return;

  const filters = Array.from(document.querySelectorAll("[data-filter]"));
  const cards = Array.from(grid.querySelectorAll("[data-category]"));
  const count = document.getElementById("project-count");
  const empty = document.getElementById("project-empty");

  function setFilter(filter) {
    let visible = 0;
    cards.forEach((card) => {
      const matches = filter === "all" || card.dataset.category === filter;
      card.hidden = !matches;
      if (matches) visible += 1;
    });
    filters.forEach((button) => {
      const active = button.dataset.filter === filter;
      button.classList.toggle("is-active", active);
      button.setAttribute("aria-pressed", String(active));
    });
    if (count) count.textContent = `${visible} ${visible === 1 ? "project" : "projects"}`;
    if (empty) empty.hidden = visible !== 0;
  }

  filters.forEach((button) => {
    button.addEventListener("click", () => setFilter(button.dataset.filter));
  });
})();
