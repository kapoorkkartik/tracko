$(document).ready(function(){
	var myTable = $('#report-table').DataTable({
		dom: 'Bfrtip',
		buttons: [
			'excelHtml5',
			'pdfHtml5',
			'copyHtml5',
			'csvHtml5',

		]
	});

	yadcf.init(myTable,[
		{column_number: 6, filter_type:"range_date",datepicker_type:"jquery-ui"},
		{column_number: 7, data:["Yes","No"],filter_default_label:"Select"},

		]);

	$( function() {
    $.datepicker.setDefaults({
      changeMonth: true,
      changeYear: true,
    });
  } );

});
