var pickedup;
	$(document).ready(function() {
			$( document ).on( "click", "#dataTable tbody tr" ,function( event ) {

				  // get back to where it was before if it was selected :
				  if (pickedup != null) {
					  pickedup.css( "background-color", "#ffccff" );
				  }

				  $("#Lot").val($(this).find("td").eq(0).html());
				  $("#Party").val($(this).find("td").eq(1).html());
				  $("#Commodity").val($(this).find("td").eq(2).html());
				  $("#GSTIN").val($(this).find("td").eq(3).html());
				  $("#Begs").val($(this).find("td").eq(4).html());
				  $("#Boxes").val($(this).find("td").eq(5).html());

				  pickedup = $( this );
			});

            $(document).keypress(function( event ) {
			    if (event.which == 13){
					   var id = $(event.target).attr("id")
					   alert(id);
					   if(id == "Boxes"){
				       var name = $("#Lot").val();
					   var position = $("#Party").val();
					   var office = $("#Commodity").val();
					   var age = $("#GSTIN").val();
					   var date = $("#Begs").val();
					   var salary = $("#Boxes").val();
					if (pickedup != null) {
					   	pickedup.find("td").eq(0).html(name);
						pickedup.find("td").eq(1).html(position);
						pickedup.find("td").eq(2).html(office);
						pickedup.find("td").eq(3).html(age);
						pickedup.find("td").eq(4).html(date);
						pickedup.find("td").eq(5).html(salary);
						pickedup = null;

					}
					else{
					   var row = "<tr><td>" + name + "</td><td>" + position + "</td><td>" + office + "</td><td>" + age + "</td><td>" + date + "</td><td>" + salary + "</td></tr>";
					   $( "#dataTable tbody" ).append(row);
                       $("#Lot").focus();
					}

					$("#Lot").val(" ");
					$("#Party").val(" ");
					$("#Commodity").val(" ");
					$("#GSTIN").val(" ");
					$("#Begs").val(" ");
					$("#Boxes").val(" ");

					   }

					if(id == "Lot"){
					   alert("you reached lot");
					   var lotNo = $("#Lot").val();
					   alert(lotNo);
					   $.ajax({
					type: "POST",
					url: "/gatepass/get_details/",
					data: {'mydata': lotNo },
					success: function(msg){
						$("#Party").val(msg[0].Name);
						$("#Commodity").val(msg[0].Comodity);
						$("#GSTIN").val(msg[0].gstin);
						$("#Begs").val(msg[0].bags);
						$("#Boxes").val(msg[0].boxes);
                        $("#Boxes").focus();
					}
				});

				}


					return false;
				}



            })






		});



$(document).ready(function() {
			$( document ).on( "click", "#btnsubmit" ,function( event ) {

				var TableData;
				TableData = storeTblValues()
				TableData = JSON.stringify(TableData);

				function storeTblValues()
				{
				var TableData = new Array();

				$('#dataTable tbody tr').each(function(row, tr){
					TableData[row]={
						"gatepass": $("#txtgatepass").val(),
						"eway": $("#txteway").val(),
						"date": $("#txtdate").val(),
						"Lot" : $(tr).find('td:eq(0)').text()
						, "Party" :$(tr).find('td:eq(1)').text()
						, "Commodity" : $(tr).find('td:eq(2)').text()
						, "GSTIN" : $(tr).find('td:eq(3)').text()
						, "Begs" : $(tr).find('td:eq(4)').text()
						, "Boxes" : $(tr).find('td:eq(5)').text()
					}
				});
				return TableData;
                }

				alert(TableData);

				$.ajax({
					type: "POST",
					url: "/gatepass/submit_gatepass/",
					data: {'mydata': TableData },
					success: function(msg){
						alert(TableData)
					}
				});


			});
});