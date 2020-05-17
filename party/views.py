from django.shortcuts import render
from django.shortcuts import redirect
from party.models import party_Ledger
from django.db.models import Max
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib.auth.decorators import permission_required


@login_required
def add(request):
    action = 'launch'
    if(request.method == "POST"):
        id = request.POST['txtid']
        name = request.POST['txtname']   
        gstin = request.POST['txtgstin']
        contact = request.POST['txtcontact']
        address = request.POST['txtaddr']
        action = request.POST['txtaction']
    
    if(action == 'edit'):
        party_Ledger.objects.filter(id=id).update(Name=name,gstin=gstin,Contact=contact,Address=address)
        return redirect('/party/view')
    elif action == 'add':
        party_Ledger.objects.create(id=id,Name=name,gstin=gstin,Contact=contact,Address=address)
    
    no = party_Ledger.objects.all().aggregate(Max('id'))
    numb = no['id__max']
    if numb == None:
        party = 1
    else:
        party = numb + 1
    return render(request,'party.html',{'partyID': party, 'action': 'add'})

@login_required
@permission_required('party.can_add_party')
def display(request):

    results = []
    party_list = party_Ledger.objects.all()
    for party in party_list:
        json_data = {}
        party = (str(party)).split('*')
        json_data['party_id'] = party[0]
        json_data['name'] = party[1]
        json_data['address'] = party[2]
        json_data['gstin'] = party[3]
        json_data['contact'] = party[4]
        results.append(json_data)
    return render(request, "view_party.html", {'item_data': results})

@login_required
def delete(request,question_id):
    party_Ledger.objects.filter(id=question_id).delete()
    return redirect ("/party/view/")

@login_required
def edit(request,question_id):
    party = party_Ledger.objects.filter(id=question_id)
    party = (str(party[0])).split('*')
    return render(request,'party.html',{'partyID': question_id, 'name': party[1], 'addr':party[2],'gstin': party[3], 'phone': party[4],'action': 'edit'})
