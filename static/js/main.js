$(function() {
  $('a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top
        }, 400);
        return false;
      }
    }
  });
});

$(document).ready(function() {

  $(window).scroll(function() {
    var top = $(this).scrollTop();
    height = $('#hero').height();

    if (top >= height) {
        $('nav#main').addClass('sticky');
    }

    if (top < height && $('nav').hasClass('sticky')) {
        $('nav#main').removeClass('sticky');
    }
  });

});