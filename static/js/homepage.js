function fullHeightHero() {
	jQuery('#hero').css('height', window.innerHeight + 'px');
}

jQuery(window).load(function() {
	fullHeightHero();
});

jQuery(window).resize(function() {
	fullHeightHero();
});