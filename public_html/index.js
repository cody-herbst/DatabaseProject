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
