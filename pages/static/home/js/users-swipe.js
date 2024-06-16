document.addEventListener('DOMContentLoaded', function () {
  var swiper = new Swiper('.swiper-container', {
    slidesPerView: 4,
    spaceBetween: 30,
    loop: true,
    loopAdditionalSlides: 4,
    breakpoints: {
      640: {
        slidesPerView: 2,
        spaceBetween: 40,
      },
      768: {
        slidesPerView: 3,
        spaceBetween: 50,
      },
      1024: {
        slidesPerView: 4,
        spaceBetween: 60,
      },
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    autoplay: {
      delay: 800,
    },
    speed: 1000,
    effect: 'slide',
  });
});
