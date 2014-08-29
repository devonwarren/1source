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

  	$('ul.subsection-links a').click(function() {
  		idx = this.href.indexOf('#');
  		if (idx != -1) {
  			homepageDetailLoad(this.href.substring(idx).replace('#subsec-',''));	
  		}
  	});
});