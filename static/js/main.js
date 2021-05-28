// Intro carousel
var heroCarousel = $("#heroCarousel");

heroCarousel.on('slid.bs.carousel', function(e) {
  $(this).find('h2').addClass('animate__animated animate__fadeInDown');
  $(this).find('p, .btn-get-started').addClass('animate__animated animate__fadeInUp');
});
// Testimonials carousel (uses the Owl Carousel library)
$(".testimonials-carousel").owlCarousel({
  autoplay: true,
  dots: true,
  loop: true,
  items: 1
});
function togNav() {
  var nav = document.getElementById("sidebarid");
  if (nav.style.width == '200px') {
    nav.style.width = '0';
    nav.style.opacity = 0;
  } else {
    nav.style.width = "200px";
    nav.style.opacity = 1;
  }
}
