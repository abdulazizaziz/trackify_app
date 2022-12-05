let viewScreenButtons = document.querySelectorAll('.view-screen');
let swiperClose = document.querySelector('.swiper-close');
let swiperjs = document.querySelector('.swiperjs');
for (let item of viewScreenButtons) {
  item.addEventListener('click', () => {
    swiperjs.classList.add('active');
  });
}
swiperClose.addEventListener('click', () => {
  swiperjs.classList.remove('active');
});
