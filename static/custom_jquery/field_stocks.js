$(document).ready(function() {
	$(document).keypress(function( event ) {
		//console.log(event);
		//console.log(event.which);
			    if (event.which == 9 || event.which == 13){
					var id = $(event.target).attr("id");
					if(id == "txtlot"){
						$("#txtdate").focus();
                        return false;						
					}
					if(id == "txtdate"){
						var d        = $('#txtdate').val();   // as an example
						d = d.replace(/\./g,'/');
						var userDate = d.split('/');
						var yy = userDate[2]
						if(yy.length == 2){
							var year  = (yy < 90) ? '20' + yy : '19' + yy;
						}
						else{
							var year = yy;
						}
						
						var newdate = userDate[0] + '/' + userDate[1] + '/' + year; //1990-01-25
						$('#txtdate').val(newdate);
						$("#txtparty").focus();
						return false;
					}
					
					if(id == "txtparty"){
							$("#txtcommodity").focus();
							return false;
						}
					
						if(id == "txtcommodity"){
							$("#txtbegs").focus();
							return false;
						}
						if(id == "txtbegs"){
							$("#txtbox").focus();
							return false;
						}
						if(id == "txtbox"){
							$("#txtremark").focus();
							return false;
						}
						if(id == "txtremark"){
							return false;
						}
						
				
				}
	});
});