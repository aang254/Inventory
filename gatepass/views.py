from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

def gatepass(request):
    return render (request,'gate_pass.html')



def showdata(request):
    return render (request, 'show_data.html')


def test_form(request):
    return render (request, 'form_testing.html')

@csrf_exempt
def submit(request):
   data = request.POST['mydata']
   print(data)
   return HttpResponse ("<p> Hello </p>")
