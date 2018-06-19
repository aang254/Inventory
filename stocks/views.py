from django.shortcuts import render
from .models import Stocks
from django.db.models import Max
# Create your views here.

def display(request):
    lot = Stocks.objects.all()
    return render(request,'stocks.html')