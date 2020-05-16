from django.shortcuts import render,redirect
from stocks.models import Stocks
from gatepass.models import gate_pass
from party.models import party_Ledger
from commodity.models import Commodity
from django.db.models import Sum,Q
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def display(request):
    partys = party_Ledger.objects.all()
    results = []
    for party in partys:
        json_data = {}
        party = str(party)
        party = party.split('*')[1]
        json_data['value'] = party
        results.append(json_data)
    return render(request,"balance.html",{'party_name': results})


@csrf_exempt
def display_com(request):
    partys = party_Ledger.objects.all()
    results = []
    for party in partys:
        json_data = {}
        party = str(party)
        party = party.split('*')[1]
        json_data['value'] = party
        results.append(json_data)
    return render(request,"balance_commodity.html",{'party_name': results})



@csrf_exempt
def get_data(request):
    if request.method == "POST":
        partyName = request.POST.get('txtparty', '')
        party = party_Ledger.objects.filter(Name=partyName)
        print(party)
        data = Stocks.objects.filter(Name=party[0])
        print(data)
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
            begs_out = gate_pass.objects.filter(lot=party[0]).aggregate(Sum('bags'))
            begs_out = begs_out['bags__sum']
            boxes_out = gate_pass.objects.filter(lot=party[0]).aggregate(Sum('boxes'))
            boxes_out = boxes_out['boxes__sum']
            if(begs_out != None or boxes_out != None):
                json_data['rem_beg'] = int(party[-3]) - int(begs_out)
                json_data['rem_box'] = int(party[-2]) - int(boxes_out)

            else:
                json_data['rem_beg'] = int(party[-3]) - int(0)
                json_data['rem_box'] = int(party[-2]) - int(0)

            ttl_begs = ttl_begs + json_data['rem_beg']
            ttl_boxes = ttl_boxes + json_data['rem_box']
            results.append(json_data)

        return render(request, "party_balance.html", {'party_name': partyName, 'party_data': results, 'box': ttl_boxes, 'beg': ttl_begs})
    else:
        return redirect('/balance/')




@csrf_exempt
def get_commodity_data(request):
    if request.method == "POST":
        partyName = request.POST.get('txtparty', '')
        party = party_Ledger.objects.filter(Name=partyName)
        party_stocks = Stocks.objects.filter(Name=party[0])
        print(party_stocks)
        if len(party_stocks) == 0:
            return render(request, "party_balance_commodity.html")
        commodity_list = []
        for item in party_stocks:
            commodity_tmp = (str(item)).split('*')[-4]
            if (commodity_tmp not in commodity_list):
                commodity_list.append(commodity_tmp)

        results = []
        ttl_begs = 0
        ttl_boxes = 0
        ttl_Begs_in = 0
        ttl_Boxes_in = 0
        ttl_begs_out = 0
        ttl_boxes_out = 0
        for commodity in commodity_list:
            commodity = str(commodity)
            json_data = {}
            json_data['Name'] = partyName
            json_data['Commodity'] = commodity
            commodity = Commodity.objects.filter(name=commodity)
            begs = Stocks.objects.filter(Q(Name=party[0]) & Q(commodity=commodity[0])).aggregate(Sum('begs'))
            begs = begs['begs__sum']
            box = Stocks.objects.filter(Q(Name=party[0]) & Q(commodity=commodity[0])).aggregate(Sum('boxes'))
            box = box['boxes__sum']
            begs_out = gate_pass.objects.filter(Q(Name=party[0]) & Q(commodity=commodity[0])).aggregate(Sum('bags'))
            begs_out = begs_out['bags__sum']
            boxes_out = gate_pass.objects.filter(Q(Name=party[0]) & Q(commodity=commodity[0])).aggregate(Sum('boxes'))
            boxes_out = boxes_out['boxes__sum']
            if (begs != None or box != None):
                if (begs_out != None or boxes_out != None):
                    json_data['Begs_in'] = begs
                    json_data['Boxes_in'] = box
                    json_data['begs_out'] = begs_out
                    json_data['boxes_out'] = boxes_out
                    json_data['rem_beg'] = int(begs) - int(begs_out)
                    json_data['rem_box'] = int(box) - int(boxes_out)

                else:
                    json_data['Begs_in'] = begs
                    json_data['Boxes_in'] = box
                    json_data['begs_out'] = 0
                    json_data['boxes_out'] = 0
                    json_data['rem_beg'] = int(begs) - int(0)
                    json_data['rem_box'] = int(box) - int(0)
            else:
                json_data['Begs_in'] = 0
                json_data['Boxes_in'] = 0
                json_data['begs_out'] = 0
                json_data['boxes_out'] = 0
                json_data['rem_beg'] = 0
                json_data['rem_box'] = 0

            print(json_data)

            ttl_begs_rem = ttl_begs + json_data['rem_beg']
            ttl_boxes_rem = ttl_boxes + json_data['rem_box']
            ttl_Begs_in = ttl_Begs_in + json_data['Begs_in']
            ttl_Boxes_in = ttl_Boxes_in + json_data['Boxes_in']
            ttl_begs_out = ttl_begs_out + json_data['begs_out']
            ttl_boxes_out = ttl_boxes_out + json_data['boxes_out']
            results.append(json_data)
        return render(request, "party_balance_commodity.html", {'party_name': partyName, 'party_data': results,
                                                                'Begs_in': ttl_Begs_in, 'Boxes_in': ttl_Boxes_in,
                                                                'begs_out': ttl_begs_out, 'boxes_out':ttl_boxes_out,
                                                                'box_rem': ttl_boxes_rem, 'beg_rem': ttl_begs_rem})
    else:
        return redirect('/balance/get_comm_bal')




@csrf_exempt
def get_commodity_balance(request):

    results = []
    ttl_begs = 0
    ttl_boxes = 0
    ttl_Begs_in = 0
    ttl_Boxes_in = 0
    ttl_begs_out = 0
    ttl_boxes_out = 0
    commodity_list = Commodity.objects.all()
    for commodity in commodity_list:
        json_data = {}
        json_data['Commodity'] = str(commodity).split("*")[1]
        begs = Stocks.objects.filter(Q(commodity=commodity)).aggregate(Sum('begs'))
        begs = begs['begs__sum']
        box = Stocks.objects.filter(Q(commodity=commodity)).aggregate(Sum('boxes'))
        box = box['boxes__sum']
        begs_out = gate_pass.objects.filter(Q(commodity=commodity)).aggregate(Sum('bags'))
        begs_out = begs_out['bags__sum']
        boxes_out = gate_pass.objects.filter(Q(commodity=commodity)).aggregate(Sum('boxes'))
        boxes_out = boxes_out['boxes__sum']
        if (begs != None or box != None):
            if (begs_out != None or boxes_out != None):
                json_data['Begs_in'] = begs
                json_data['Boxes_in'] = box
                json_data['begs_out'] = begs_out
                json_data['boxes_out'] = boxes_out
                json_data['rem_beg'] = int(begs) - int(begs_out)
                json_data['rem_box'] = int(box) - int(boxes_out)

            else:
                json_data['Begs_in'] = begs
                json_data['Boxes_in'] = box
                json_data['begs_out'] = 0
                json_data['boxes_out'] = 0
                json_data['rem_beg'] = int(begs) - int(0)
                json_data['rem_box'] = int(box) - int(0)
        else:
            json_data['Begs_in'] = 0
            json_data['Boxes_in'] = 0
            json_data['begs_out'] = 0
            json_data['boxes_out'] = 0
            json_data['rem_beg'] = 0
            json_data['rem_box'] = 0

        print(json_data)

        ttl_begs_rem = ttl_begs + json_data['rem_beg']
        ttl_boxes_rem = ttl_boxes + json_data['rem_box']
        ttl_Begs_in = ttl_Begs_in + json_data['Begs_in']
        ttl_Boxes_in = ttl_Boxes_in + json_data['Boxes_in']
        ttl_begs_out = ttl_begs_out + json_data['begs_out']
        ttl_boxes_out = ttl_boxes_out + json_data['boxes_out']
        results.append(json_data)
    return render(request, "comm_balance.html", {'party_data': results,
                                                            'Begs_in': ttl_Begs_in, 'Boxes_in': ttl_Boxes_in,
                                                            'begs_out': ttl_begs_out, 'boxes_out':ttl_boxes_out,
                                                            'box_rem': ttl_boxes_rem, 'beg_rem': ttl_begs_rem})
























