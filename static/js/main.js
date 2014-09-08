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

function fullHeightHero() {
  $('#hero').css('height', window.innerHeight + 'px');
  var targetCenter = Math.round((window.innerHeight - $('#logo h1').height()) / 2);
  $('#logo').css('top', targetCenter);
}

function homepageTagFades(currentIdx) {
  if (!currentIdx) {
    currentIdx = 0;
  }
  var current = $('div.tagline')[currentIdx];
  var delay = 500;
  var opacity = .5;
  if ($(current).hasClass('longfade')) {
    delay = 2000;
    opacity = 1;
  }
  $(current).fadeTo(1000, opacity, function() {
    $(this).delay(delay).fadeTo(1000, 0, function() {
      if ($('div.tagline')[currentIdx+1]) {
        homepageTagFades(currentIdx+1);  
      } else {
        homepageTagFades(0);
      }
    });
  });
}

$(window).load(function() {
  fullHeightHero();
});

$(window).resize(function() { 
  fullHeightHero();
  scrollEvent();
});

$(window).on('orientationchange', function() {
  fullHeightHero();
  scrollEvent();
});


function homepageDetailLoad(subsection) {
  // scroll to section top
  if ($('#subsec-' + subsection).length > 0) {
    $(window).scrollTop($('#subsec-' + subsection).offset().top);
  }

  var section = $('#subsection-' + subsection).parent().parent();
  // change content

  $(section).find('div.active').fadeOut(function() {
    $(this).removeClass('active').parent().find('div#subsection-' + subsection).fadeIn().addClass('active');
  });

  // change link active
  $(section).find('li.active').removeClass('active');
  $(section).find('li#subsection-select-' + subsection).addClass('active');
}

$(document).ready(function() {

  $(window).scroll(function() {
    window.requestAnimationFrame(scrollEvent);
  });

  $('ul#fullmenu a').click(function() {
    if ($('ul#fullmenu').hasClass('open')) {
      toggleMobileMenu();
    }
  });

  if ($('body').hasClass('homepage')) {
    if (window.location.hash) {
      homepageDetailLoad(window.location.hash.replace('#subsec-',''));
    }

    $('li.subsection-link a').click(function() {
      idx = this.href.indexOf('#');
      if (idx != -1) {
        homepageDetailLoad(this.href.substring(idx).replace('#subsec-',''));  
      }
    });
  }

  scrollEvent();

  window.setTimeout(homepageTagFades, 2000);
});