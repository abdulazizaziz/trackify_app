let nested = document.querySelectorAll('.nested');
for (let item of nested) {
  item.children[0].addEventListener('click', () => {
    item.classList.toggle('active');
  });
}
$(document).ready(function () {
  $('.form-select2').select2();
});
