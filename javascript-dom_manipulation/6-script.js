fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    console.log(data.name);
    document.getElementById('character').textContent = data.name;
  })
  .catch(error => {
    console.error('Error:', error);
  });
