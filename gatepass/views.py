from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from gatepass.models import gate_pass
from stocks.models import Stocks
from django.db.models import Max
from party.models import party_Ledger
import datetime
import json

def gatepass(request):
    no = gate_pass.objects.all().aggregate(Max('passNo'))
    numb = no['passNo__max']
    if numb == None:
        passNo = 1
    else:
        passNo = numb + 1

    today = datetime.datetime.now()
    today = today.strftime("%d-%m-%Y")
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



def test_form(request):
    return render (request, 'form_testing.html')


@csrf_exempt
def submit(request):
    data = request.POST['mydata']
    print(data)
    return HttpResponse ("<p> Hello </p>")
