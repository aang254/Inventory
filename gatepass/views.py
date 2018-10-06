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
    if(request.POST['passNo'] == " "):
        data = request.POST['lotNo']
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
    else:
        data = request.POST['passNo']
        print(data)
        search_qs = gate_pass.objects.filter(passNo=data)
        fat = str(search_qs[0])
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)





def submit(request):
    gatepassNo = request.POST['txtgatepass']
    date = request.POST['txtdate']
    driver = request.POST['txtdriver']
    eway = request.POST['txteway']
    vehicle = request.POST['txtvehicle']
    data = []
    for j in range(6):
        lot = 'Lot'+str(j)
        if(request.POST[lot] != " "):
            val = {"gatepass": str(gatepassNo),
                    "eway": eway,
                    "date": date,
                    "driver_name": driver,
                    "vehicleNo": vehicle,
                    "Lot" : request.POST[lot],
                    "Party" :request.POST['Party'+str(j)],
                    "Commodity" : request.POST['Commodity'+str(j)],
                    "GSTIN" : request.POST['GSTIN'+str(j)],
                    "Begs" : request.POST['Begs'+str(j)],
                    "Boxes" : request.POST['Boxes'+str(j)],
                  }
            data.append(val)
    generate_gatepass.generate(data)
    print(data)
    for item in data:
        format_str = '%d/%m/%Y'  # The format
        datetime_obj = datetime.datetime.strptime(item['date'], format_str)
        gate_pass.objects.create(passNo=item['gatepass'],date=datetime_obj.date(),driver_name=item['driver_name'],
                                 Auto_No=item['vehicleNo'],lot=item['Lot'],
                                 Name=item['Party'],commodity=item['Commodity'],gstin=item['GSTIN'],
                                 bill_no=item['eway'],bags=item['Begs'],boxes=item['Boxes'])

    return redirect ("/gatepass/add/")



def view(request):

    results = []
    gatepass_list = gate_pass.objects.all()
    for gatepass in gatepass_list:
        json_data = {}
        gatepass = str(gatepass).split(",")
        json_data['GatePass'] = gatepass[0]
        json_data['Lot'] = gatepass[1]
        json_data['Date'] = gatepass[2]
        json_data['Name'] = gatepass[3]
        json_data['Commodity'] = gatepass[4]
        json_data['Bags'] = gatepass[5]
        json_data['Boxes'] = gatepass[6]
        results.append(json_data)
    return render(request, "view_gatepass.html", {'item_data': results})

@csrf_exempt
def edit(request):
    if (request.method == "POST"):
        print("request is post")
        passNo = request.POST['txtgatepass']
        results = []
        object = gate_pass.objects.filter(passNo=passNo)
        print(object)
        gatepass = str(object[0]).split(",")
        print(gatepass)
        GatePass = gatepass[0]
        Date = str(gatepass[2]).split("-")
        Date = Date[2]+"/"+Date[1]+"/"+Date[0]
        print(Date)
        Driver = gatepass[8]
        AutoNo = gatepass[7]
        WayNo = gatepass[9]
        ttl_begs = 0
        ttl_box = 0
        for gatepass in object:
            json_data = {}
            gatepass = str(gatepass).split(",")
            json_data['Lot'] = gatepass[1]
            json_data['Name'] = gatepass[3]
            json_data['Commodity'] = gatepass[4]
            json_data['Bags'] = gatepass[5]
            json_data['Boxes'] = gatepass[6]
            json_data['gstin'] = gatepass[10]
            ttl_begs = ttl_begs + int(gatepass[5])
            ttl_box = ttl_box + int(gatepass[6])
            results.append(json_data)
        print(results)
        return render (request,'edit.html',{'range': range(len(results),6),'pass_details': results, 'GatePass': GatePass, 'Date': Date,
                                            'Driver': Driver, 'AutoNo': AutoNo,'WayNo': WayNo,'beg':ttl_begs,'box':ttl_box})

    else:
        print("request is not post")
        return redirect("/")



@csrf_exempt
def submit_edit(request):
    gatepassNo = request.POST['txtgatepass']
    date = request.POST['txtdate']
    driver = request.POST['txtdriver']
    eway = request.POST['txteway']
    vehicle = request.POST['txtvehicle']
    data = []
    for j in range(6):
        lot = 'Lot'+str(j)
        if(request.POST[lot] != " "):
            val = {"gatepass": str(gatepassNo),
                    "eway": eway,
                    "date": date,
                    "driver_name": driver,
                    "vehicleNo": vehicle,
                    "Lot" : request.POST[lot],
                    "Party" :request.POST['Party'+str(j)],
                    "Commodity" : request.POST['Commodity'+str(j)],
                    "GSTIN" : request.POST['GSTIN'+str(j)],
                    "Begs" : request.POST['Begs'+str(j)],
                    "Boxes" : request.POST['Boxes'+str(j)],
                  }
            data.append(val)
    #generate_gatepass.generate(data)
    print(data)
    gate_pass.objects.filter(passNo=gatepassNo).delete()
    for item in data:
        format_str = '%d/%m/%Y'  # The format
        datetime_obj = datetime.datetime.strptime(item['date'], format_str)
        gate_pass.objects.create(passNo=item['gatepass'],date=datetime_obj.date(),driver_name=item['driver_name'],
                                 Auto_No=item['vehicleNo'],lot=item['Lot'],
                                 Name=item['Party'],commodity=item['Commodity'],gstin=item['GSTIN'],
                                 bill_no=item['eway'],bags=item['Begs'],boxes=item['Boxes'])

    return redirect ("/gatepass/view/")


def delete(request,question_id):
    gate_pass.objects.filter(passNo=question_id).delete()
    return redirect ("/gatepass/view/")

