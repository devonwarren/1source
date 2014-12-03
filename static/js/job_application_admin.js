if (!$) {
	$ = django.jQuery;
}

function check_clearance_options() {
	console.log('ss');
	if ($('#id_clearance')) {
		if ($('#id_clearance').is(':checked')) {
			$('#id_clearance_type').show();
			$('div.clearance_type').show();
		} else {
			$('#id_clearance_type').hide();
			$('div.clearance_type').hide();
		}
	}
}

function check_race_options() {
	if ($('#id_race')) {
		if ($('#id_race').val() == 'O') {
			$('div.race_other').show();
		} else {
			$('div.race_other').hide();
		}
	}
}

function check_referred_options() {
	if ($('#id_referred')) {
		if ($('#id_referred').val() == 'O') {
			$('div.referred_other').show();
		} else {
			$('div.referred_other').hide();
		}
	}
}

function check_rejection_options() {
	if ($('#id_status')) {
		if ($('#id_status').val() == 'R') {
			$('div.rejected_reason').show();
			$('div.rejected_explaination').show();
		} else {
			$('div.rejected_reason').hide();
			$('div.rejected_explaination').hide();
		}
	}
}

$(document).ready(function() {
	check_rejection_options();
	$('#id_status').change(check_rejection_options);

	check_clearance_options();
	$('#id_clearance').change(check_clearance_options);	

	check_race_options();
	$('#id_race').change(check_race_options);	

	check_referred_options();
	$('#id_referred').change(check_referred_options);	
});