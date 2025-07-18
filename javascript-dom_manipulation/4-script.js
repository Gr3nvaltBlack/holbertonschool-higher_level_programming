const addItem = document.getElementById('add_item');

addItem.addEventListener('click', function () {
  const Ultt = document.querySelector('.my_list');
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  Ultt.appendChild(newItem);
});
