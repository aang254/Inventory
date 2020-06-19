//pickedup.cells[0].getElementsByTagName("input")[0].value = 12;

var table = document.getElementById("Bill_Table"),rIndex,cIndex;
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
			$("#Item").val(pickedup.cells[0].getElementsByTagName("input")[0].value);
			$("#Quantity").val(pickedup.cells[1].getElementsByTagName("input")[0].value);
			$("#Price").val(pickedup.cells[2].getElementsByTagName("input")[0].value);
			$("#GST").val(pickedup.cells[3].getElementsByTagName("input")[0].value);
			$("#Total").val(pickedup.cells[4].getElementsByTagName("input")[0].value);
			$("#Item").focus();
		};
	}
}


function count_col()
{
	var beg=0;
	for (var i=3; i < 12; i++){
		var ttl = tab.getElementsByTagName('tr')[i].cells[4].getElementsByTagName("input")[0].value;
		if(ttl == " "){
			ttl = 0;
		}
		beg = parseInt(beg) + parseInt(ttl);
	}
	var total = new Array();
	total = {
		'beg': beg
	}
	return total
	
}
	


$(document).ready(function() {
	$(document).keypress(function( event ) {
		//console.log(event);
		//console.log(event.which);
			    if (event.which == 9 || event.which == 13){
                    var id = $(event.target).attr("id");
                    if(id == "Item"){
                        $("#Quantity").focus();
                        return false;
                    }
                    if(id == "Quantity"){
                        $("#Price").focus();
                        return false;
                    }
                    if(id == "Price"){
                        $("#GST").focus();
                        return false;
                    }

                    if(id == "GST"){
                        var qty = $("#Quantity").val();
                        var price = $("#Price").val();
                        var gst = $("#GST").val();
                        var ttl = parseInt(qty)*parseInt(price);
                        var ttl = ttl + (parseInt(gst)*ttl)/100;
                        $("#Total").val(ttl);
                        $("#Total").focus();
                        return false;
                    }
						
					if(id == "Total"){
						if(pickedup != null)
						{
							pickedup.cells[0].getElementsByTagName("input")[0].value = $("#Item").val();
							pickedup.cells[1].getElementsByTagName("input")[0].value = $("#Quantity").val();
							pickedup.cells[2].getElementsByTagName("input")[0].value = $("#Price").val();
							pickedup.cells[3].getElementsByTagName("input")[0].value = $("#GST").val();
							pickedup.cells[4].getElementsByTagName("input")[0].value = $("#Total").val();
							pickedup = null;
							var count = count_col();
							document.getElementById("lbl_ttl").innerText = count['beg'];
							$("#Item").val(" ");
							$("#Quantity").val("1");
							$("#Commodity").val("0");
							$("#Price").val("0");
							$("#GST").val("0");
                            $("#Total").val("0");
                            $("#Item").focus();
							return false;
						}
						else
						{
							filled.cells[0].getElementsByTagName("input")[0].value = $("#Item").val();
							filled.cells[1].getElementsByTagName("input")[0].value = $("#Quantity").val();
							filled.cells[2].getElementsByTagName("input")[0].value = $("#Price").val();
							filled.cells[3].getElementsByTagName("input")[0].value = $("#GST").val();
							filled.cells[4].getElementsByTagName("input")[0].value = $("#Total").val();
							k = k+1;
							if(k <= 12){
								filled = tab.getElementsByTagName('tr')[k];
							}
							else{
								alert("Entry can't be added.All Gatepass fields are field. Please submit the form");
								k = 10;
							}
							var count = count_col();
							document.getElementById("lbl_ttl").innerText = count['beg'];
							$("#Item").val(" ");
							$("#Quantity").val("1");
							$("#Commodity").val("0");
							$("#Price").val("0");
							$("#GST").val("0");
                            $("#Total").val("0");
                            $("#Item").focus();
							
							return false; 
						}
						}
				
					if(id == "txtdate"){						
                        $("#txtcustomer").focus();
							return false;
						}
					if(id == "txtcustomer"){
							$("#txtaddr").focus();
							return false;
						}
					if(id == "txtaddr"){
							$("#txtgstin").focus();
							return false;
						}
					if(id == "txtgstin"){
							$("#txtphone").focus();
							return false;
						}
					if(id == "txtphone"){
							$("#Item").focus();
							return false;
						}				
				
				}
	});
});



