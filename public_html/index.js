function requestReturn() {

    $.ajax({
        url: 'http://codydatabaseproject.com/query',
        type: 'post',
        dataType: 'html',
        data: $('form#formID').serialize(),
        success: function(data) {
		   $('.returnRow').remove();
                   $('#returnTable').append(data);
		   return false;
                 }
    });

    return false;
}



function tabOneClick(){
	$('#tab2').hide();
	$('#tab1').show();
}

function tabTwoClick(){
	$('#tab1').hide();
	$('#tab2').show();
}

function aggregationDataChart(){

	// Load the Visualization API and the piechart package.
	google.load('visualization', '1.0', {'packages':['corechart']});

	drawChart();
}


// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function drawChart() {
	$.ajax({
        url: 'http://codydatabaseproject.com/aggregation',
        type: 'get',
        dataType: 'json',
        success: function(returnData) {
		     // Create the data table.
		     var data = new google.visualization.DataTable();
		     data.addColumn('string', 'Location');
		     data.addColumn('number', 'TimesUsed');

		     for (i in returnData)
		     {
  			data.addRow([returnData[i].building + " " + returnData[i].room_number, parseInt(returnData[i].count)]) 
		     }

                     // Set chart options
	             var options = {'title':'Most utilized rooms is CIS',
		         'width':800,
		         'height':800};

		     // Instantiate and draw our chart, passing in some options.
	             var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
	             chart.draw(data, options);
                 }
    	});
}

