function toggleButton() {
  let element = document.getElementById('container');
  if (element.style.display === 'none') {
      element.style.display = 'block';
  } else {
      element.style.display = 'none';
  }
}