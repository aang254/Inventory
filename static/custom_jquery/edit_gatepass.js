//pickedup.cells[0].getElementsByTagName("input")[0].value = 12;

var table = document.getElementById("dataTable"),rIndex,cIndex;
var pickedup;
var k = 3;
var tab = document.getElementsByTagName('table')[0];
var filled = tab.getElementsByTagName('tr')[k];
var ttl_beg = 0;
var ttl_box = 0;

for(var i = 0; i< table.rows.length; i++)
{
	for(var j=0; j< table.rows[i].cells.length;j++)
	{
		table.rows[i].cells[j].ondblclick = function()
		{
			rIndex = this.parentElement.rowIndex;
			console.log(rIndex);
			if(pickedup != null)
			{
				pickedup.style.background = "";
			}
			this.parentElement.style.background = "blue";
			pickedup = this.parentElement;
			$("#Lot").val(pickedup.cells[0].getElementsByTagName("input")[0].value);
			$("#Party").val(pickedup.cells[1].getElementsByTagName("input")[0].value);
			$("#Commodity").val(pickedup.cells[2].getElementsByTagName("input")[0].value);
			$("#GSTIN").val(pickedup.cells[3].getElementsByTagName("input")[0].value);
			$("#Begs").val(pickedup.cells[4].getElementsByTagName("input")[0].value);
			$("#Boxes").val(pickedup.cells[5].getElementsByTagName("input")[0].value);
			$("#Lot").focus();
		};
	}
}


function count_col()
{
	var beg=0;
	var box=0;
	for (var i=3; i < 9; i++){
		var b_count = tab.getElementsByTagName('tr')[i].cells[4].getElementsByTagName("input")[0].value;
		var bx_count = tab.getElementsByTagName('tr')[i].cells[5].getElementsByTagName("input")[0].value;
		console.log(b_count);
		console.log(bx_count);
		if(b_count == " "){
			b_count = 0;
			bx_count = 0;
		}
		beg = parseInt(beg) + parseInt(b_count);
		box = parseInt(box) + parseInt(bx_count);
		
	}
	var total = new Array();
	total = {
		'beg': beg,
		'box': box
	}
	return total
	
}
	


$(document).ready(function() {
	$(document).keypress(function( event ) {
		//console.log(event);
		//console.log(event.which);
			    if (event.which == 9 || event.which == 13){
					var id = $(event.target).attr("id");
					if(id == "Lot"){
					   var lotNo = $("#Lot").val();
					   if(event.preventDefault) {
						   event.preventDefault();
						}
					   if(lotNo != ""){
						   $.ajax({
							   type: "POST",
							   url: "/gatepass/get_details/",
							   //data: {'mydata': lotNo },
							   data: {'passNo': " ", 'lotNo': lotNo },
					           success: function(msg){
								   $("#Party").val(msg[0].Name);
								   $("#Commodity").val(msg[0].Comodity);
								   $("#GSTIN").val(msg[0].gstin);
								   $("#Begs").val(msg[0].bags);
								   $("#Boxes").val(msg[0].boxes);
								   $("#Begs").focus();
								},
								error: function(XMLHttpRequest, textStatus, errorThrown) {
									 alert("Lot not found");
									 $("#Lot").val(" ");
									 $("#Party").val(" ");
									 $("#Commodity").val(" ");
									 $("#GSTIN").val(" ");
									 $("#Begs").val(" ");
									 $("#Boxes").val(" ");
									 $("#Lot").focus();
								  }
							});
							return false;
						}
						else{
							alert("Please enter a Lot");
							return false;	
						}
                        return false;						
					}
					
					if(id == "Begs"){
							$("#Boxes").focus();
							return false;
						}
						
						
					if(id == "Boxes"){
						if(pickedup != null)
						{
							pickedup.cells[0].getElementsByTagName("input")[0].value = $("#Lot").val();
							pickedup.cells[1].getElementsByTagName("input")[0].value = $("#Party").val();
							pickedup.cells[2].getElementsByTagName("input")[0].value = $("#Commodity").val();
							pickedup.cells[3].getElementsByTagName("input")[0].value = $("#GSTIN").val();
							pickedup.cells[4].getElementsByTagName("input")[0].value = $("#Begs").val();
							pickedup.cells[5].getElementsByTagName("input")[0].value = $("#Boxes").val();
							pickedup.style.background = "";
							pickedup = null;
							var count = count_col();
							document.getElementById("lbl_ttlbegs").innerText = count['beg'];
							document.getElementById("lbl_ttlboxes").innerText = count['box'];
							$("#Lot").val(" ");
							$("#Party").val(" ");
							$("#Commodity").val(" ");
							$("#GSTIN").val(" ");
							$("#Begs").val(" ");
							$("#Boxes").val(" ");
							$("#Lot").focus();
							return false;
						}
						else
						{
							filled.cells[0].getElementsByTagName("input")[0].value = $("#Lot").val();
							filled.cells[1].getElementsByTagName("input")[0].value = $("#Party").val();
							filled.cells[2].getElementsByTagName("input")[0].value = $("#Commodity").val();
							filled.cells[3].getElementsByTagName("input")[0].value = $("#GSTIN").val();
							filled.cells[4].getElementsByTagName("input")[0].value = $("#Begs").val();
							filled.cells[5].getElementsByTagName("input")[0].value = $("#Boxes").val();
							k = k+1;
							if(k <= 8){
								filled = tab.getElementsByTagName('tr')[k];
							}
							else{
								alert("Entry can't be added.All Gatepass fields are field. Please submit the form");
								k = 3;
								filled = tab.getElementsByTagName('tr')[k];
							}
							var count = count_col();
							document.getElementById("lbl_ttlbegs").innerText = count['beg'];
							document.getElementById("lbl_ttlboxes").innerText = count['box'];
							$("#Lot").val(" ");
							$("#Party").val(" ");
							$("#Commodity").val(" ");
							$("#GSTIN").val(" ");
							$("#Begs").val(" ");
							$("#Boxes").val(" ");
							$("#Lot").focus();
							
							return false; 
						}
						}
				
					if(id == "txtgatepass"){
						    $("#txtdate").focus();
							return false;
						}
					if(id == "txtdate"){
							$("#txtdriver").focus();
							return false;
						}
					if(id == "txtdriver"){
							$("#txteway").focus();
							return false;
						}
					if(id == "txteway"){
							$("#txtvehicle").focus();
							return false;
						}
					if(id == "txtvehicle"){
							$("#Lot").focus();
							return false;
						}				
				
				}
	});
});



