function fullHeightHero() {
	$('#hero').css('height', window.innerHeight + 'px');
}

$(window).load(function() {
	fullHeightHero();
});

$(window).resize(function() { 
	fullHeightHero();
});

function homepageDetailLoad(subsection) {
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
 	if (window.location.hash) {
 		homepageDetailLoad(window.location.hash.replace('#subsec-',''));
  	}

 	$(window).scroll(function() {
	    var top = $(this).scrollTop();
	    var anchors = $('.anchor');
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
	});
});