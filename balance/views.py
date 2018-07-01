from django.shortcuts import render
from stocks.models import Stocks
from gatepass.models import gate_pass
from party.models import party_Ledger
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def display(request):
    partys = party_Ledger.objects.all()
    results = []
    for party in partys:
        json_data = {}
        party = str(party)
        party = party.split(',')[0]
        json_data['value'] = party
        results.append(json_data)
    return render(request,"balance.html",{'party_name': results})


@csrf_exempt
def get_data(request):
    partyName = request.POST.get('txtparty', '')
    party = party_Ledger.objects.filter(Name=partyName)
    data = Stocks.objects.filter(Name=party[0])
    results = []
    for party in data:
        json_data = {}
        party = (str(party)).split(',')
        json_data['lot'] = party[0]
        json_data['Name'] = party[2]
        json_data['Commodity'] = party[4]
        json_data['begs'] = party[5]
        json_data['boxes'] = party[6]
        begs_out = gate_pass.objects.filter(lot=party[0]).aggregate(Sum('bags'))
        begs_out = begs_out['bags__sum']
        boxes_out = gate_pass.objects.filter(lot=party[0]).aggregate(Sum('boxes'))
        boxes_out = boxes_out['boxes__sum']
        if(begs_out != None or boxes_out != None):
            json_data['rem_beg'] = int(party[5]) - int(begs_out)
            json_data['rem_box'] = int(party[6]) - int(boxes_out)

        else:
            json_data['rem_beg'] = int(party[5]) - int(0)
            json_data['rem_box'] = int(party[6]) - int(0)
        results.append(json_data)

    return render(request, "party_balance.html", {'party_name': partyName, 'party_data': results})