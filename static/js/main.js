function fullHeightHero() {
  $('#hero').css('height', window.innerHeight + 'px');
  var targetCenter = Math.round((window.innerHeight - $('#logo h1').height()) / 2);
  $('#logo').css('top', targetCenter);
}

fullHeightHero(); // run this as soon as possible

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
      for (idx=0; idx<anchors.length; idx++) {
        var offset = $(anchors[idx]).offset();
        if (top >= offset.top - 10 && $('#nav-'+anchors[idx].id).length > 0) {
          active = anchors[idx].id;
        }
      }

      var navlinks = $('nav a');
      for (idx=0; idx<navlinks.length; idx++) {
        val = navlinks[idx];
        if (val.id != 'nav-'+active) {
          $(val).removeClass('active');
        } else {
          $(val).addClass('active');
        }
      }
    }
  }
}

function toggleMobileMenu() {
  $('ul#fullmenu').toggleClass('open');
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

$(window).resize(function() { 
  fullHeightHero();
  scrollEvent();
  setTimeout(bgimageCycle(), 4000);
});

$(window).on('orientationchange', function() {
  fullHeightHero();
  scrollEvent();
});

function bgimageCycle(currentIdx) {
  var delay = 4000;
  if (!currentIdx) {
    currentIdx = 0;
  }

  var heroes = $('.bgimage-container .bgimage')
  var current = heroes[currentIdx];
  if (heroes[currentIdx+1]) {
    var nextIdx = currentIdx + 1;
    var next = heroes[nextIdx];
  } else {
    var nextIdx = 0;
    var next = heroes[0];
  }
  if ($(next).css('display') != 'none') {

    for (var x=0; x<heroes.length; x++) {
      $(heroes[x]).css('z-index', -2);
    }
    $(current).css('z-index', -1);
    $(next).css('z-index', 0).css('opacity', 0).fadeTo(4000, 1.0, function() {
      setTimeout(function() {
        bgimageCycle(nextIdx); 
      }, delay);
    });
  }
}

function homepageDetailLoad(subsection) {
  // scroll to section top
  if ($('#subsec-' + subsection).length > 0) {
    $('html,body').animate({ scrollTop: $('#subsec-' + subsection).offset().top }, 400);
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
    setTimeout(bgimageCycle(), 4000);

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