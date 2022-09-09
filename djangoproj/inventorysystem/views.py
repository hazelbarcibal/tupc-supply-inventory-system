from django.shortcuts import render, redirect
from .forms import deliverysupply
from .forms import deliverySupplyForm


def home(request):
    return render(request, 'task/home.html')

def adminLogin(request):
    return render(request, 'task/login.html')

def deptRegister(request):
    return render(request, 'task/department-register.html')

def suppliesDeliver(request):
    info = deliverysupply.objects.all()[:5]
    form = deliverySupplyForm()
    if request.method == 'POST':
        form = deliverySupplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventorysystem-suppliesDeliver')
    
    context = {
        'form': form,
        'info': info,
    }

    return render(request, 'task/supplies-delivery.html', context)

def addItem(request):
    return render(request, 'task/add-new-item.html')

def equipmentDeliver(request):
    return render(request, 'task/equipment-delivery.html')

#def addEquipment(request):
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
