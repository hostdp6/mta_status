// Gets a CSRF cookie so POSTs can be processed by Django
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Updates the status column of the monitors table
// meant to be run on a recurring interval 
// e.g. settimeout(updateMonitorStatus(), 10000)
function updateMonitorStatus(id){
	$.ajax({
		url: "/monitor/",
		type: "GET",
		dataType: "json",
		acceptType: "application/json",
		contentType: "application/json; charset=utf-8",
		data: {
			"id": id
		},
		success: function(data){
			data = JSON.parse(data)
			//console.log(data)
		}
	})
	$.ajax({
		url: "/monitor/status/",
		type: "GET",
		dataType: "json",
		acceptType: "application/json",
		contentType: "application/json; charset=utf-8",
		data: {
			"id": id
		},
		success: function(data){
			data = JSON.parse(data)
		}
	})
	return true
}

$(document).ready(function(){

});
