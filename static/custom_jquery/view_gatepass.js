var table = document.getElementById("dataTable"),rIndex,cIndex;
var form = document.getElementById("form_gatepass");
var txt_field = document.getElementById("txtgatepass");


for(var i = 1; i< (table.rows.length - 1); i++)
{
	for(var j=0; j< table.rows[i].cells.length;j++)
	{
		table.rows[i].cells[j].ondblclick = function()
		{
			//rIndex = this.parentElement.rowIndex;
            //console.log(rIndex);
            //console.log(txt_field);
            this.parentElement.style.background = "blue";
            txt_field.value = this.parentElement.cells[1].getElementsByTagName("input")[0].value;
            console.log(txt_field);
            form.submit();
            
		};
	}
}