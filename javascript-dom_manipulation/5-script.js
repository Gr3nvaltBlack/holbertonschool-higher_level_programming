const upElement = document.getElementById('update_header');

upElement.addEventListener('click', function () {
  const header = document.querySelector('header');
  header.textContent = 'New Header!!!';
});
