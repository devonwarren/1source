var pauseHero = false;

function fullHeightHero() {
  $('#hero').css('height', window.innerHeight + 'px');
  var targetCenter = Math.round((window.innerHeight - $('#logo h1').height()) / 2.1);
  $('#logo').css('top', targetCenter);
}

fullHeightHero(); // run this as soon as possible

function fixBgImageHomepage() {
  // only run if on mobile
  var sections = $('.section-bgimage');

  for (i=0; i<sections.length; i++) {
    var section = $(sections[i]);
    var height = 0;
    if ($('#isMobile').css('display') == 'block') {
      height = $($(section).find('section.summary')[0]).outerHeight() - 10;
    }
    $(section).css('background-position', 'center ' + height + 'px')
  }
}


fixBgImageHomepage();


$(function() {
  $('a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        var position = target.length
        if ($('header.not-fullscreen').length) {
          position = $(target).position().top - $('header').height() - 15;
          $('html,body').animate({scrollTop: position}, 400);
        } else {
          $(target).velocity("scroll", 400);
        }

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
      pauseHero = true;
      $('nav#main').addClass('sticky');
    } else if (top < targetHeight && is_sticky) {
      pauseHero = false;
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
  var delay = 700;
  var opacity = .5;
  if ($(current).hasClass('longfade')) {
    delay = 2400;
    opacity = 1;
  }
  $(current).velocity({opacity:opacity}, {display:'block', duration:1000, complete:function() {
    $(this).delay(delay).velocity({opacity:0}, {display:'block', duration:1000, complete:function() {
      if ($('div.tagline')[currentIdx+1]) {
        homepageTagFades(currentIdx+1);  
      } else {
        homepageTagFades(0);
      }
    }});
  }});
}

$(window).resize(function() { 
  fullHeightHero();
  scrollEvent();
  fixBgImageHomepage();
});

$(window).on('orientationchange', function() {
  fullHeightHero();
  scrollEvent();
  fixBgImageHomepage();
});

function bgimageCycle(currentIdx) {
  var delay = 6000;
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
  if ($(next).is(':visible') && !pauseHero) {
    for (var x=0; x<heroes.length; x++) {
      $(heroes[x]).css('z-index', -2);
    }
    $(current).css('z-index', -1);
    $(next).css('z-index', 0).css('opacity', 0).velocity({opacity:1.0}, {duration:4000, complete:function() {
      setTimeout(function() {
        bgimageCycle(nextIdx); 
      }, delay);
    }});
  } else {
    setTimeout(function() {
        bgimageCycle(currentIdx); 
      }, delay);
  } 
}

function homepageDetailLoad(subsection) {
  // scroll to section top
  if ($('#subsec-' + subsection).length > 0) {
    $('#subsec-' + subsection).velocity("scroll", 400);
  }

  var section = $('#subsection-' + subsection).parent().parent();
  // change content

  $(section).find('div.active').velocity("fadeOut", function() {
    $(this).removeClass('active').parent().find('div#subsection-' + subsection).velocity("fadeIn").addClass('active');
  });

  // change link active
  $(section).find('li.active').removeClass('active');
  $(section).find('li#subsection-select-' + subsection).addClass('active');
}

$(document).ready(function() {

  $(window).scroll(function() {
    if (!window.requestAnimationFrame) {
      scrollEvent();
    } else {
      window.requestAnimationFrame(scrollEvent);
    }
  });

  $('ul#fullmenu a').click(function() {
    if ($('ul#fullmenu').hasClass('open')) {
      toggleMobileMenu();
    }
  });

  if ($('body').hasClass('homepage')) {
    bgimageCycle();

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