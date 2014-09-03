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

function scrollEvent() {
  var top = $(this).scrollTop();
  var heroHeight = $('#hero').height();
  var navHeight = $('nav#main').height();
  var targetHeight = heroHeight - navHeight;
  var is_sticky = $('nav#main').hasClass('sticky');

  if (heroHeight > 0) {

    // sticky navigation ftw
    if (top >= targetHeight && !is_sticky) {
      $('nav#main').addClass('sticky');
    } else if (top < targetHeight && is_sticky) {
      $('nav#main').removeClass('sticky');
    }
    

    // set active nav items if applicable
    if (is_sticky) {
      var anchors = $('.section-anchor');
      var active = '';
      anchors.each(function(ind, val) {
        var offset = $(val).offset();
        if (top >= offset.top - 10 && $('#nav-'+val.id).length > 0) {
          active = val.id;
        }
      });

      $('nav a').each(function(ind, val) {
        if (val.id != 'nav-'+active) {
          $(val).removeClass('active');
        } else {
          $(val).addClass('active');
        }
      });
    }
  }
}

function toggleMobileMenu() {
  $('ul#fullmenu').toggleClass('open');
}

$(document).ready(function() {

  $(window).scroll(function() {
    window.requestAnimationFrame(scrollEvent);
  });

});