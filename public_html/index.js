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

	// Set a callback to run when the Google Visualization API is loaded.
	google.setOnLoadCallback(drawChart);
}


// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function drawChart() {

	// Create the data table.
	var data = new google.visualization.DataTable();
	data.addColumn('string', 'Topping');
	data.addColumn('number', 'Slices');
	data.addRows([
	  ['Mushrooms', 3],
	  ['Onions', 1],
	  ['Olives', 1],
	  ['Zucchini', 1],
	  ['Pepperoni', 2]
	]);

	// Set chart options
	var options = {'title':'How Much Pizza I Ate Last Night',
		       'width':400,
		       'height':300};

	// Instantiate and draw our chart, passing in some options.
	var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
	chart.draw(data, options);
}

