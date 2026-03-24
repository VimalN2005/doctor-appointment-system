document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("appointment-form");
  if (!form) return;

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    alert("Demo only: connect this form to Django view or API.");
    form.reset();
  });
});
