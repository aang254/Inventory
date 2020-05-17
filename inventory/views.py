from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission

@login_required

def homepage(request):
    permissions = Permission.objects.filter(user=request.user)
    print(permissions)
    return render(request, 'home.html')
