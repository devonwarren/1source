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