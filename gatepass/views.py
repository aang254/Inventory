from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from gatepass.models import gate_pass
from stocks.models import Stocks
from django.db.models import Max
from django.shortcuts import redirect
import datetime
import json
from . import vault,generate_gatepass


def gatepass(request):
    no = gate_pass.objects.all().aggregate(Max('passNo'))
    numb = no['passNo__max']
    if numb == None:
        passNo = 1
    else:
        passNo = numb + 1

    today = datetime.datetime.now()
    today = today.strftime("%d/%m/%Y")
    print(today)
    print(passNo)
    return render (request,'gate_pass.html',{'pass': passNo, 'date': today})


@csrf_exempt
def getdata(request):
    data = request.POST['mydata']
    print(data)
    search_qs = Stocks.objects.filter(lot=data)
    print(search_qs)
    fat = str(search_qs[0])
    fat = fat.split(',')
    results = []
    details = {}
    details['Name'] = fat[2]
    details['Comodity'] = fat[4]
    details['gstin'] = fat[3]
    details['bags'] = fat[5]
    details['boxes'] = fat[6]
    results.append(details)
    data = json.dumps(results)
    print(data)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)



@csrf_exempt
def submit(request):
    data = request.POST['mydata']
    data = json.loads(data)
    item = {}
    item['CompanyName'] = vault.company
    item['Address'] = vault.Address
    item['GSTIN'] = vault.GSTIN
    item['BillNo'] = data[0]['gatepass']
    item['date'] = data[0]['date']
    item['Vehicle'] = data[0]['vehicleNo']
    item['WayBill'] = data[0]['eway']
    item['driver'] = data[0]['driver_name']
    item['entries'] = data
    json_data = json.dumps(item)
    for item in data:
        format_str = '%d/%m/%Y'  # The format
        datetime_obj = datetime.datetime.strptime(item['date'], format_str)
        gate_pass.objects.create(passNo=item['gatepass'],date=datetime_obj.date(),driver_name=item['driver_name'],
                                 Auto_No=item['vehicleNo'],lot=item['Lot'],
                                 Name=item['Party'],commodity=item['Commodity'],gstin=item['GSTIN'],
                                 bill_no=item['eway'],bags=item['Begs'],boxes=item['Boxes'])

    generate_gatepass.generate(json_data)
    return redirect ("/gatepass/add/")




