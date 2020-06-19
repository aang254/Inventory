from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

#@login_required
def add(request):
    return render (request,'create_bill.html')