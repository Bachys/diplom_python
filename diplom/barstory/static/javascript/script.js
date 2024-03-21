document.getElementById("submenu").addEventListener("click", function (event) {
  let submenu = document.getElementById("submenu");
  if (event.target === submenu) {
    submenu.style.display = "none";
  }
});
