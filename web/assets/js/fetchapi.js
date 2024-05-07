// get all
function fetchMenuItems() {
  fetch('http://localhost:8000/foodies/')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      const menuList = document.getElementById('menu-list');

      data.forEach(item => {
        const listItem = document.createElement('li');
        listItem.classList.add('promo-item');
        listItem.innerHTML = `
          <div class="promo-card">
            <h3 class="h3 card-title">${item.Name}</h3>
            <p class="card-text">${item.Address}</p>
            <p class="card-text">${item.Phone}</p>
            <img src="${item.Image}" width="300" height="300" loading="lazy" alt="${item.Name}" class="w-100 card-banner">
          </div>
        `;
        menuList.appendChild(listItem);
      });
    })
    .catch(error => console.error('Error fetching menu items:', error));
}
window.onload = fetchMenuItems;

// search
function fetchMenuItemsByTerm(search_term) {
  fetch(`http://localhost:8000/foodies/${search_term}`)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      const menuList = document.getElementById('menu-list');

      menuList.innerHTML = '';

      data.forEach(item => {
        const listItem = document.createElement('li');
        listItem.classList.add('promo-item');
        listItem.innerHTML = `
          <div class="promo-card">
            <h3 class="h3 card-title">${item.Name}</h3>
            <p class="card-text">${item.Address}</p>
            <p class="card-text">${item.Phone}</p>
            <img src="${item.Image}" width="300" height="300" loading="lazy" alt="${item.Name}" class="w-100 card-banner">
          </div>
        `;
        menuList.appendChild(listItem);
      });
    })
    .catch(error => console.error('Error fetching menu items:', error));
}

window.onload = function () {
  fetchMenuItems('');
}

searchBtn = document.querySelector('[data-search-submit-btn]');
searchBtn.addEventListener('click', function () {
  const searchTerm = document.querySelector('.search-input').value;
  fetchMenuItemsByTerm(searchTerm);
});
