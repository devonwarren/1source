function fullHeightHero() {
	$('#hero').css('height', window.innerHeight + 'px');
}

jQuery(window).load(function() {
	fullHeightHero();
});

jQuery(window).resize(function() { 
	fullHeightHero();
});

function homepageDetailLoad(section_id, subsection_id) {
	// change content
	$('#section-' + section_id).find('div.active').fadeOut(function() {
		$(this).removeClass('active').parent().find('div#subsection-' + subsection_id).fadeIn().addClass('active');
	});

	// change link active
	$('#aside-' + section_id).find('li.active').removeClass('active');
	$('#aside-' + section_id).find('li#subsection-select-' + subsection_id).addClass('active');
}

$(document).ready(function() {

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