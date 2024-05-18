document.addEventListener("DOMContentLoaded", function() {
  if (!localStorage.getItem("ageVerified")) {
      document.getElementById("overlay").style.display = "block";
  }
  document.getElementById("confirmBtn").addEventListener("click", function() {
    localStorage.setItem("ageVerified", "true");
    document.getElementById("overlay").style.display = "none";

  });
});
