from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from commodity.models import Commodity
from django.db.models import Max
from django.shortcuts import redirect
# Create your views here.

# View all entered commodity
def display(request):
    results = []
    Commodity_list = Commodity.objects.all()
    for commodity in Commodity_list:
        json_data = {}
        commodity = (str(commodity)).split('*')
        json_data['CommodityNo'] = commodity[0]
        json_data['commodity'] = commodity[1]
        results.append(json_data)
    return render(request, "view_commodity.html", {'item_data': results})

#Delete a commodity
def delete(request,question_id):
    Commodity.objects.filter(CommodityNo=question_id).delete()
    return redirect ("/commodity/view/")

#Create commodity form
def commodity_add(request):
    no = Commodity.objects.all().aggregate(Max('CommodityNo'))
    numb = no['CommodityNo__max']
    if numb == None:
        passNo = 1
    else:
        passNo = numb + 1
    return render (request,'commodity.html',{'commodityNO': passNo})

def submit(request):
    CommodityNO = request.POST['CommodityNo']
    commodity = request.POST['txtcommodity']
    Commodity.objects.create(CommodityNo=CommodityNO,name=commodity)
    return redirect ("/commodity/add/")