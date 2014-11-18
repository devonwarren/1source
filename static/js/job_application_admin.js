$ = django.jQuery;

function check_rejection_options() {
	if ($('#id_status').val() == 'R') {
		$('div.rejected_reason').show();
		$('div.rejected_explaination').show();
	} else {
		$('div.rejected_reason').hide();
		$('div.rejected_explaination').hide();
	}
}

$(document).ready(function() {
	check_rejection_options();
	$('#id_status').change(check_rejection_options);
});