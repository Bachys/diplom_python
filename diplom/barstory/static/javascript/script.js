function toggleButton() {
  let element = document.getElementById('container');
  if (element.style.display === 'none') {
      element.style.display = 'block';
  } else {
      element.style.display = 'none';
  }
}

// --------------------------- Модальное окно ----------------------------------

 // Проверяем, есть ли ключ в LocalStorage, который указывает, что пользователь уже видел модальное окно
 let modalShown = localStorage.getItem('modalShown');
 if (!modalShown) {
 // Если ключа нет, показываем модальное окно и сохраняем информацию об этом в LocalStorage
 document.getElementById("myModal").style.display = "block";
 localStorage.setItem('modalShown', 'true');
 }
// Когда DOM полностью загружен, найти все элементы с классом modal и показать их

document.addEventListener('DOMContentLoaded', function() {
let modal = document.getElementById("myModal");

  // Теперь мы проверяем, было ли модальное окно показано ранее

if (!localStorage.getItem('modalShown')) {
modal.style.display = "block";
}

});

// Когда пользователь кликает на кнопку закрытия, скрыть модальное окно
let close = document.getElementsByClassName("close")[0];
close.onclick = function() {
 let modal = document.getElementById("myModal");
 modal.style.display = "none";
}

// Когда пользователь кликает вне модального окна, скрыть его
window.onclick = function(event) {
 if (event.target == modal) {
   let modal = document.getElementById("myModal");
   modal.style.display = "none";
 }
}


//  ----------------------------------- Карусель ----------------------------

let slideIndex = 0;
showSlides();

function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    slides[slideIndex-1].style.display = "block";
    setTimeout(showSlides, 4000); // Change image every 2 seconds
}