import re
from django.shortcuts import render


def home(request):
    return render(request, 'task/home.html')

def suppliesDeliver(request):
    return render(request, 'task/supplies-delivery.html')

def addSupply(request):
    return render(request, 'task/add-supply.html')