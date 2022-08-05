import re
from django.shortcuts import render


def home(request):
    return render(request, 'task/home.html')

def suppliesDeliver(request):
    return render(request, 'task/supplies-delivery.html')

def addSupply(request):
    return render(request, 'task/add-supply.html')

def equipmentDeliver(request):
    return render(request, 'task/equipment-delivery.html')

def addEquipment(request):
    return render(request, 'task/add-equipment.html')

def suppliesWithdraw(request):
    return render(request, 'task/supplies-withdraw.html')

def equipmentWithdraw(request):
    return render(request, 'task/equipment-withdraw.html')

def statusLimit(request):
    return render(request, 'task/status-limit.html')
