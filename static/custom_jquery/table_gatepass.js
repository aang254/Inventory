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
					   var lotNo = $("#Lot").val();
					if(lotNo != ""){
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
                        $("#Begs").focus();

					}
				});

				}
				else {
					alert("Please enter a Lot");
				}
					}

                if(id == "Begs"){
					if($("#Begs").val() != "" ){
				        $("#Boxes").focus();
					}

				else{
				$("#Begs").val(0);
				$("#Boxes").focus();
				}

				}
				if(id == "txtgatepass"){
					if($("#txtgatepass").val() != "" ){
						if($.isNumeric( $('#txtgatepass').val())){
							$("#txtdate").focus();
						}
						else{alert("Enter only numeric value");}

					}
				else{alert("GatePass Field can't be empty");}
				}
				if(id == "txtdate"){
					if($("#txtdate").val() != "" ){
					  var T_date = $("#txtdate").val()
					  if(T_date.indexOf('.') >=0){
					     //var options = {year: 'numeric', month: 'numeric', day: 'numeric' };
					     var parts = ($("#txtdate").val()).split(".");
					     var yy       = parts[2];
                         var newdate  = (yy < 90) ? '20' + yy : '19' + yy;
					     date = new Date(newdate, parts[1] - 1, parts[0]);
					     var datestring = ("0" + date.getDate()).slice(-2) + "/" + ("0"+(date.getMonth()+1)).slice(-2) + "/" +
                         date.getFullYear();
					     $("#txtdate").val(datestring);
					     $("#txtdriver").focus();
					   }
					   else if(T_date.indexOf('/') >=0){
					       $("#txtdriver").focus();
					   }
					   else{
					      alert("Please enter date in dd/mm/yyyy format");
					   }

					}

				else{alert("Date Field can't be empty");}

				}
				if(id == "txtdriver"){
				   $("#txteway").focus();
				}
				if(id == "txteway"){
				   $("#txtvehicle").focus();
				}
				if(id == "txtvehicle"){
				   $("#Lot").focus();
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
						 "driver_name": $("#txtdriver").val(),
						 "vehicleNo": $("#txtvehicle").val(),
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

				$.ajax({
					type: "POST",
					url: "/gatepass/submit_gatepass/",
					data: {'mydata': TableData }
				});


			});
});
