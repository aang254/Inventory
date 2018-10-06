from django.shortcuts import render
from .forms import partyForm

def add(request):
    form = partyForm
    print(form)
    print()
    return render(request,'party.html',{'form': form})
