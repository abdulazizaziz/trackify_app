let buttons = document.querySelectorAll('.button-extend');
for (let item of buttons) {
  item.addEventListener('click', () => {
    let nestedTr = item.parentElement.parentElement;
    let nestedData = nestedTr.nextElementSibling;
    nestedTr.classList.toggle('active');

    if (nestedData.classList.contains('nested-data'))
      nestedData.classList.toggle('active');
  });
}
