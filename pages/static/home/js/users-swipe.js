document.addEventListener('DOMContentLoaded', function () {
  console.log("DOM fully loaded and parsed");

  var swiperContainer = document.querySelector('.swiper-container');
  if (!swiperContainer) {
    console.error("Swiper container not found");
    return;
  }

  console.log("Initializing Swiper");
  var swiper = new Swiper('.swiper-container', {
    slidesPerView: 1,
    spaceBetween: 10,
    breakpoints: {
      640: {
        slidesPerView: 2,
        spaceBetween: 20,
      },
      768: {
        slidesPerView: 3,
        spaceBetween: 30,
      },
      1024: {
        slidesPerView: 4,
        spaceBetween: 40,
      },
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  });

  console.log("Swiper initialized", swiper);
});
