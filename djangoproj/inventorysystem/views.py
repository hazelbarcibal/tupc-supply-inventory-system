from django.shortcuts import render


def home(request):
    return render(request, 'task/home.html')

def adminLogin(request):
    return render(request, 'task/login.html')

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

def viewRequestSupply(request):
    return render(request, 'task/view-request-supplies.html')

def viewRequestEquipment(request):
    return render(request, 'task/view-request-equipment.html')

def depRequestSupply(request):
    return render(request, 'task/dep-request-supply.html')

def depRequestEquipment(request):
    return render(request, 'task/dep-request-equipment.html')

def statusLimit(request):
    return render(request, 'task/status-limit.html')

def equipmentReturn(request):
    return render(request, 'task/equipment-return.html')

def storageMapping(request):
    return render(request, 'task/storage-mapping.html')
