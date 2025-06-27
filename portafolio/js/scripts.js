$(document).ready(function () {
  $('.btn-primary').click(function (e) {
    e.preventDefault();
    window.open('https://github.com/Tomasoun/ciberseguridad', '_blank');
  });

  const images = [
    "img/Coursera GZKGK7UEQB3C1.png",
    "img/Coursera R1.png",
    "img/ROCHA - 96111327 - PROGRAMACIÓN PYTHON1.png",
  ];
  let currentIndex = 0;

  const $modal = $('#modal');
  const $modalImg = $('#modal-img');
  const $thumbs = $('.thumb');

  $thumbs.on('click', function () {
    currentIndex = $thumbs.index(this);
    $modalImg.attr('src', images[currentIndex]);
    $modal.fadeIn(300);
  });

  $('.close').click(function () {
    $modal.fadeOut(300);
  });

  $('.next').click(function () {
    currentIndex = (currentIndex + 1) % images.length;
    $modalImg.attr('src', images[currentIndex]);
  });

  $('.prev').click(function () {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    $modalImg.attr('src', images[currentIndex]);
  });

  $modal.on('click', function (e) {
    if ($(e.target).is('#modal')) {
      $modal.fadeOut(300);
    }
  });
});

