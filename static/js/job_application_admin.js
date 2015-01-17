if (!$) {
	$ = django.jQuery;
}

function check_clearance_options() {
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
		if ($('#id_race').val() == '7') {
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

function check_military_options() {
    if ($('#id_veteran')) {
        if ($('#id_veteran').is(':checked')) {
        	$('#id_military_service').show();
            $('div.military_service').show();
        } else {
        	$('#id_military_service').hide();
            $('div.military_service').hide();
        }
    }
}

function check_status_options() {
	if ($('#id_status')) {
		if ($('#id_status').val() == 'R') {
            $('div.rejected_reason').show();
            $('div.rejected_explaination').show();
            $('div.hired_date').hide();
		} else if ($('#id_status').val() == 'H') {
            $('div.hired_date').show();
        } else {
			$('div.rejected_reason').hide();
			$('div.rejected_explaination').hide();
            $('div.hired_date').hide();
		}
	}
}

function check_interviewed_options() {
    if ($('#id_interviewed')) {
        if ($('#id_interviewed').is(':checked')) {
            $('div.interview_date').show();
        } else {
            $('div.interview_date').hide();
        }
    }
}

$(document).ready(function() {
	check_status_options();
	$('#id_status').change(check_status_options);

	check_clearance_options();
	$('#id_clearance').change(check_clearance_options);	

	check_race_options();
	$('#id_race').change(check_race_options);	

	check_referred_options();
	$('#id_referred').change(check_referred_options);	

    check_military_options();
    $('#id_veteran').change(check_military_options);      

    check_interviewed_options();
    $('#id_interviewed').change(check_interviewed_options);      
});
