let openfilters = document.querySelector('.openfilters');
let closefilters = document.querySelector('.closefilters');
let view_filters = document.querySelector('.view_filters');
openfilters.addEventListener('click', () => {
  view_filters.style.transform = 'translateX(0)';
});
closefilters.addEventListener('click', () => {
  view_filters.style.transform = 'translateX(100%)';
});
