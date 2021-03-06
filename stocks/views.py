from django.shortcuts import render
from .models import Stocks
from django.db.models import Max
from party.models import party_Ledger
from commodity.models import Commodity
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .print_stock import print_stock
import datetime
import os
# Create your views here.
@login_required
def add(request):
    no = Stocks.objects.all().aggregate(Max('lot'))
    numb = no['lot__max']
    if numb == None:
        lot = 1
    else:
        lot = numb + 1

    today = datetime.datetime.now()
    today = today.strftime("%d/%m/%Y")
    party = party_Ledger.objects.all()
    commodity = Commodity.objects.all()
    party_name,comm_list = [],[]
    for p in party:
        party_name.append(str(p).split('*')[1])
    for c in commodity:
        comm_list.append(str(c).split('*')[1])
    return render(request,"add.html",{'partyName':party_name,'comm_data':comm_list,'lot':lot,'date': today})

@login_required
def party_name(request):
    partys = party_Ledger.objects.all()
    results = []
    for party in partys:
        json_data = {}
        party = str(party)
        party = party.split('*')[1]
        json_data['value'] = party
        results.append(json_data)
    return render(request,"party_name.html",{'party_name': results})

@login_required
def display(request):
    if request.method == 'POST':
        partyName = request.POST.get('txtparty', '')
        party = party_Ledger.objects.filter(Name=partyName)
        data = Stocks.objects.filter(Name=party[0])
        results = []
        ttl_begs = 0
        ttl_boxes = 0
        for party in data:
            json_data = {}
            party = (str(party)).split('*')
            json_data['lot'] = party[0]
            json_data['Name'] = party[3]
            json_data['Commodity'] = party[-4]
            json_data['begs'] = party[-3]
            json_data['boxes'] = party[-2]
            ttl_begs = ttl_begs + int(json_data['begs'])
            ttl_boxes = ttl_boxes + int(json_data['boxes'])
            results.append(json_data)
        return render(request, "stock_data.html", {'party_name': partyName, 'party_data': results, 'box': ttl_boxes, 'beg': ttl_begs})
    else:
        return redirect('/stock/view/')

@login_required
def delete(request,question_id,name):
    Stocks.objects.filter(lot=question_id).delete()
    party = party_Ledger.objects.filter(Name=name)
    data = Stocks.objects.filter(Name=party[0])

    results = []
    ttl_begs = 0
    ttl_boxes = 0
    for party in data:
        json_data = {}
        party = (str(party)).split('*')
        json_data['lot'] = party[0]
        json_data['Name'] = party[3]
        json_data['Commodity'] = party[-4]
        json_data['begs'] = party[-3]
        json_data['boxes'] = party[-2]
        ttl_begs = ttl_begs + int(json_data['begs'])
        ttl_boxes = ttl_boxes + int(json_data['boxes'])
        results.append(json_data)

    return render(request, "stock_data.html", {'party_name': name, 'party_data': results, 'box': ttl_boxes, 'beg': ttl_begs})



@login_required
def submit(request):
    if(request.method == "POST"):
        lot = request.POST['txtlot']
        date = request.POST['txtdate']
        format_str = '%d/%m/%Y'  # The format
        datetime_obj = datetime.datetime.strptime(date, format_str)    
        party = request.POST['txtparty']
        name = party_Ledger.objects.filter(Name=party)
        commodity = request.POST['txtcommodity']
        comd = Commodity.objects.filter(name=commodity)
        begs = request.POST['txtbegs']
        box = request.POST['txtbox']
        remark = request.POST['txtremark']
        Stocks.objects.create(lot=lot,date=datetime_obj.date(),Name=name[0],commodity=comd[0],
                               begs=begs,boxes=box,remarks=remark,rem_beg=begs,rem_box=box )
        return redirect ("/stock/add/")
    else:
        return redirect ("/stock/add/")


@login_required
def edit(request,lot_id):
    stock = Stocks.objects.filter(lot=lot_id)
    data = str(stock[0]).split('*')
    print(data)
    json_data = {}
    json_data['lot'] = data[0]
    Date = str(data[1]).split("-")
    Date = Date[2]+"/"+Date[1]+"/"+Date[0]
    json_data['Date'] = Date
    json_data['Name'] = data[3]
    json_data['Commodity'] = data[-4]
    json_data['begs'] = data[-3]
    json_data['boxes'] = data[-2]
    json_data['remarks'] = data[-1]
    party = party_Ledger.objects.exclude(Name=data[2])
    commodity = Commodity.objects.exclude(name=data[4])
    party_name = []
    for p in party:
        party_name.append(str(p).split('*')[0])
    return render(request,"edit.html",{'stock': json_data,'partyName':party_name,'comm_data':commodity})

@login_required
def update(request):
    if request.method == 'POST':
        lot = request.POST['txtlot']
        date = request.POST['txtdate']
        format_str = '%d/%m/%Y'  # The format
        datetime_obj = datetime.datetime.strptime(date, format_str)    
        party = request.POST['txtparty']
        name = party_Ledger.objects.filter(Name=party)
        commodity = request.POST['txtcommodity']
        comd = Commodity.objects.filter(name=commodity)
        begs = request.POST['txtbegs']
        box = request.POST['txtbox']
        remark = request.POST['txtremark']
        Stocks.objects.filter(lot=lot).update(lot=lot,date=datetime_obj.date(),Name=name[0],commodity=comd[0],
                               begs=begs,boxes=box,remarks=remark,rem_beg=begs,rem_box=box )


        data = Stocks.objects.filter(Name=name[0])

        results = []
        ttl_begs = 0
        ttl_boxes = 0
        for party in data:
            json_data = {}
            party = (str(party)).split('*')
            json_data['lot'] = party[0]
            json_data['Name'] = party[3]
            json_data['Commodity'] = party[-4]
            json_data['begs'] = party[-3]
            json_data['boxes'] = party[-2]
            ttl_begs = ttl_begs + int(json_data['begs'])
            ttl_boxes = ttl_boxes + int(json_data['boxes'])
            results.append(json_data)

        return render(request, "stock_data.html", {'party_name': str(name).split('*')[1], 'party_data': results, 'box': ttl_boxes, 'beg': ttl_begs})
    else:
        return redirect('/')

def print_receipt(request,lotID):
    file_name = print_stock(str(lotID))
    #Print the Register
    file_path = os.path.abspath(file_name)
    os.startfile(file_path, "print")
    return redirect('/stock/view/')