from .forms import *
from .models import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse, HttpResponseRedirect, response
from django.contrib import messages
import datetime
import xlwt

def home(request):
    return render(request, 'task/home.html')


#--------- LOGIN --------------------
def deptLogin(request):
    if request.method == "POST":
        username = request.POST.get('logusername')
        # department = request.POST.get('logdept')
        email = request.POST.get('email')
        password = request.POST.get('logpassword')
        # print(username + ' ' + department + ' ' + email + ' ' + password + ' ')
        user = authenticate(request, username=username, email=email,  password=password)

        if user is not None and user.is_active and user.is_department:
            login(request, user)
            # messages.success(request, 'Hello ' + deptuser + '!')
            return redirect('inventorysystem-depRequestSupply')
        else:
            messages.info(request, 'Invalid credentials. Please try again.')

    return render(request, 'task/department-login.html')

def userLogin(request):
    if request.method == "POST":
        adminuser = request.POST.get('logname')
        adminpass = request.POST.get('logpass')
        user = authenticate(request, username=adminuser, password=adminpass)

        if user is not None and user.is_superuser:
            login(request, user)
            messages.success(request, 'Hello ' + adminuser + '!')
            return redirect('inventorysystem-home')
        else:
            messages.info(request, 'Invalid credentials. Please try again.')

    return render(request, 'task/admin-login.html')


def deptRegister(request):
    form = DeptRegisterForm()
    
    if request.method == "POST":
        form = DeptRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('inventorysystem-deptRegister')
        else:
            messages.warning(request, form.errors)
    context = {
        'form': form,
    }
    return render(request, 'task/department-register.html', context)


#------------------- DELIVERY SUPPLIES -----------------------------
def suppliesDeliver(request):
    info = deliverysupply.objects.all()
    info1 = supplymainstorage.objects.all()
    form = deliverySupplyForm()
    if request.method == 'POST':
        form = deliverySupplyForm(request.POST)
        description = request.POST.get('delivery_supply_description')
        unit = request.POST.get('delivery_supply_unit')
        quantity = request.POST.get('delivery_supply_quantity')

        if supplymainstorage.objects.filter(Description = description).exists() == False:
            if int(quantity) > 0:
                    delivery_record = deliverysupply()
                    delivery_record.delivery_supply_description = description
                    delivery_record.delivery_supply_unit = unit
                    delivery_record.delivery_supply_quantity = quantity
                    delivery_record.delivery_supply_remaining = quantity
                    delivery_record.save()
                    storageupdate = supplymainstorage()
                    storageupdate.Description = description
                    storageupdate.Unit = unit
                    storageupdate.Quantity = quantity
                    storageupdate.save()
                    mapping = storagemapping()
                    mapping.Category = "Supply"
                    mapping.ItemName = description
                    mapping.RackNo = 0
                    mapping.LayerNo = 0
                    mapping.CabinetNo = 0
                    mapping.ShelfNo = 0
                    mapping.save()
                    messages.success(request, 'Record created for ' + description)
                    return redirect('inventorysystem-suppliesDeliver')
            else:
                    messages.info(request, "invalid quantity")
                    return redirect('inventorysystem-suppliesDeliver')

        elif supplymainstorage.objects.filter(Description = description).exists() == True:
            messages.info(request, 'Description: '  + description + ' already exist ')
            return redirect('inventorysystem-suppliesDeliver')        
    
    context = {
        'form': form,
        'info': info,
        'info1': info1,
    }

    return render(request, 'task/supplies-delivery.html', context)

def updateSuppliesDeliver(request, pk):
    data = supplymainstorage.objects.get(supplymainstorage_id=pk)
    form = updateDeliverySupplyForm(request.POST or None, instance=data)
    if request.method == 'POST':
        if int(request.POST.get('RequestQuantity')) > 0:
            
                getdata1 = supplymainstorage.objects.get(supplymainstorage_id=pk).supplymainstorage_id
                getdata2 = supplymainstorage.objects.get(supplymainstorage_id= getdata1).Description
                update_record = deliverysupply()
                update_record.delivery_supply_description = getdata2
                update_record.delivery_supply_unit = supplymainstorage.objects.get(supplymainstorage_id= getdata1).Unit
                getdata3 = supplymainstorage.objects.get(supplymainstorage_id=pk).supplymainstorage_id
                getdata4 = supplymainstorage.objects.get(supplymainstorage_id= getdata3)
                adding = int(getdata4.Quantity) + int(request.POST.get('RequestQuantity'))
                update_record.delivery_supply_quantity = request.POST.get('RequestQuantity')
                update_record.delivery_supply_remaining = adding
                update_record.save()

                update_delivery = supplymainstorage()
                update_delivery.supplymainstorage_id = getdata1
                update_delivery.Description = getdata2
                update_delivery.Unit = supplymainstorage.objects.get(supplymainstorage_id= getdata1).Unit
                getdata5 = supplymainstorage.objects.get(supplymainstorage_id=pk).supplymainstorage_id
                getdata6 = supplymainstorage.objects.get(supplymainstorage_id= getdata5)
                adding1 = int(getdata6.Quantity) + int(request.POST.get('RequestQuantity'))
                update_delivery.Quantity = adding1
                getdata7 = supplymainstorage.objects.get(supplymainstorage_id=pk).supplymainstorage_id
                getdata8 = supplymainstorage.objects.get(supplymainstorage_id= getdata7)
                supplymainstorage.objects.filter(Description = getdata8.Description).filter(Unit = getdata8.Unit).delete()
                update_delivery.save()
                getdata9 = supplymainstorage.objects.get(supplymainstorage_id=pk).supplymainstorage_id
                getdata10 = supplymainstorage.objects.get(supplymainstorage_id= getdata9).Description

                messages.success(request, 'Record updated for: ' + getdata10)
                return redirect('inventorysystem-suppliesDeliver')

        else:
            messages.info(request, "invalid quantity")

    context = {
        'data': data,
        'form': form,
    }

    return render(request, 'task/update-supply-delivery.html', context)

#------------------- STATUS LIMIT SUPPLIES -----------------------------
def statusLimit(request):
    info = supplymainstorage.objects.all()
    info1 = limitrecords.objects.all()
    if request.method == 'POST':
        description = request.POST.get('non-existing_description')
        unit = request.POST.get('non-existing_unit')
        quantity = request.POST.get('non-existing_quantity')
        department = request.POST.get('non-existing_department')

        if supplymainstorage.objects.filter(Description = description).filter(Unit = unit).exists() == True:
            if int(request.POST.get('non-existing_quantity')) > 0:
                    if limitrecords.objects.filter(limit_description = description).filter(limit_department = department).filter(limit_unit = unit).exists() == False:
                            limit = limitrecords()
                            limit.limit_description = description
                            limit.limit_unit = unit
                            limit.limit_quantity = quantity
                            limit.limit_department = department
                            limit.save()        
                            messages.success(request, 'Record created for ' + description)

                    elif limitrecords.objects.filter(limit_description = description).filter(limit_department = department).filter(limit_unit = unit).exists() == True:
                            messages.info(request, "Item name: " +  description + " with a unit: " + unit + " is existing in the department: " + department)
            else:
                messages.info(request, "invalid quantity")
        elif  supplymainstorage.objects.filter(Description = description).filter(Unit = unit).exists() == False:
            messages.info(request, "No Existing item name: " +  description +  " with a unit: " + unit + " in supply mainstorage")


    context = {
        'info': info,
        'info1': info1,
    }
    return render(request, 'task/status-limit.html', context)

def updateStatus(request, pk):
    data = limitrecords.objects.get(limit_id=pk)
    form = statusForm(request.POST or None, instance=data)
    if request.method == 'POST':
        getdata2 = limitrecords.objects.get(limit_id=pk).limit_id
        getdata3 = limitrecords.objects.get(limit_id = getdata2)
        if int(request.POST.get('limit_addquantity')) > 0:
            update_record = limitrecords()
            update_record.limit_id = getdata2
            update_record.limit_description = getdata3.limit_description
            update_record.limit_unit = getdata3.limit_unit
            update_record.limit_department = getdata3.limit_department
            getdata = limitrecords.objects.get(limit_id=pk).limit_id
            getdata1 = limitrecords.objects.get(limit_id=getdata)
            adding = int(getdata1.limit_quantity) + int(request.POST.get('limit_addquantity'))
            update_record.limit_quantity = adding
            getdatalimit = limitrecords.objects.get(limit_id=pk).limit_id
            limitrecords.objects.filter(limit_id = getdatalimit).delete()
            update_record.save()
            getdata4 = limitrecords.objects.get(limit_id=pk).limit_id
            getdata5 = limitrecords.objects.get(limit_id = getdata4).limit_description
            getdata6 = limitrecords.objects.get(limit_id = getdata4).limit_unit
            getdata7 = limitrecords.objects.get(limit_id = getdata4).limit_department

            messages.success(request, 'Record updated for Itemname: ' + getdata5 +  " with a unit: " + getdata6 + " into department: " + getdata7)
            return redirect('inventorysystem-statusLimit')
        else:
            messages.info(request, "invalid quantity")

    context = {
            'data': data,
            'form': form,
        }

    return render(request, 'task/update-status.html', context)


#------------------- ADMIN VIEW REQUEST SUPPLIES -----------------------------
def viewRequestSupply(request):
    info = requestsupply.objects.all()
    # info1 = supplymainstorage.objects.filter()
    context = {
        'info': info,
        # 'info1': info1,

    }
    return render(request, 'task/view-request-supplies.html', context)

def editRequestSupply(request, pk):
    data = requestsupply.objects.get(requestsupply_id=pk)
    form = requestSupplyForm(request.POST or None, instance=data)
    if request.method == 'POST':
        getdata = requestsupply.objects.get(requestsupply_id=pk).requestsupply_id
        getdata1 = requestsupply.objects.get(requestsupply_id = getdata)
        if int(supplymainstorage.objects.get(Description = getdata1.request_supply_description).Quantity) > int(getdata1.request_supply_quantity):
            accept = acceptSupplyRequests()
            accept.acceptSupplyRequests_id = getdata
            accept.arequest_supply_department = getdata1.request_supply_department
            accept.arequest_supply_description = getdata1.request_supply_description
            accept.arequest_supply_unit = getdata1.request_supply_unit
            accept.arequest_supply_quantity = getdata1.request_supply_quantity
            accept.arequest_supply_remaining = supplymainstorage.objects.get(Description = getdata1.request_supply_description).Quantity
            accept.arequest_supply_status = "Ready for pick-up"
            data1 = requestsupply.objects.get(requestsupply_id=pk).requestsupply_id
            requestsupply.objects.filter(requestsupply_id = data1).delete()       
            status = statusSupplyRequest()
            status.statusSupplyRequests_id = getdata
            status.status_supply_description = getdata1.request_supply_description
            status.status_supply_unit = getdata1.request_supply_unit
            status.status_supply_quantity = getdata1.request_supply_quantity
            status.status_supply_remaining = limitrecords.objects.get(limit_id = getdata).limit_quantity
            status.status_supply_department = getdata1.request_supply_department
            status.status_supply_status = "Ready for pick-up"  
            statusSupplyRequest.objects.filter(statusSupplyRequests_id = getdata).delete()  
            accept.save()
            status.save()
            messages.success(request, 'request accepted')
            return redirect('inventorysystem-viewRequestSupply')
        else:
            number = str(supplymainstorage.objects.get(Description = getdata1.request_supply_description).Quantity)
            messages.info(request, 'This item does not have enough stock in the main storage,'+ ' Mainstorage Remaining: ' + number)

    context = {
        'data': data,
        'form': form,

    }
    return render(request, 'task/edit-request-supplies.html', context)

#------------------- DEPARTMENT REQUEST SUPPLIES -----------------------------
def depRequestSupply(request):
    info1 = limitrecords.objects.all().filter(limit_department = request.user)
    info = statusSupplyRequest.objects.all().filter(status_supply_department = request.user)
    info2 = withdrawsupply.objects.all().filter(withdraw_supply_department = request.user)
    

    context = {
        'info1': info1,
        'info': info,
        'info2': info2,
    }   
    return render(request, 'task/dep-request-supply.html', context)

def editdepRequestSupply(request, pk):
    info1 = limitrecords.objects.get(limit_id=pk)
    form = depRequestSupplyForm(request.POST or None, instance=info1)
    if request.method == 'POST':
        requestingID = limitrecords.objects.get(limit_id=pk).limit_id
        requestingitem = limitrecords.objects.get(limit_id= requestingID).limit_description
        if statusSupplyRequest.objects.filter(status_supply_description = requestingitem).filter(status_supply_department = request.user).exists() == True:
                messages.info(request, 'You already have a request for this item.')
                return redirect('inventorysystem-depRequestSupply')

        elif int(request.POST.get('limit_quantity')) == 0:
                messages.info(request, 'Not enough quantity for this item.')
                return redirect('inventorysystem-depRequestSupply')

        elif int(request.POST.get('limit_addquantity')) <= 0:
                messages.info(request, 'Check the available quantity')
                return redirect('inventorysystem-depRequestSupply')

        elif statusSupplyRequest.objects.filter(statusSupplyRequests_id = requestingID).exists() == False:
                requestID = limitrecords.objects.get(limit_id=pk).limit_id
                requestqty = request.POST.get('limit_addquantity')
                if limitrecords.objects.filter(limit_id = requestID).exists() == True:
                    getdata3 = limitrecords.objects.get(limit_id = requestID)
                    requesting = requestsupply()
                    requesting.requestsupply_id = requestID
                    requesting.request_supply_description = getdata3.limit_description
                    requesting.request_supply_unit = getdata3.limit_unit
                    requesting.request_supply_quantity = requestqty
                    requesting.request_supply_remaining = getdata3.limit_quantity
                    requesting.request_supply_department = getdata3.limit_department
                    requesting.request_supply_status = "pending"
                    status = statusSupplyRequest()
                    status.statusSupplyRequests_id = requestID
                    status.status_supply_description = getdata3.limit_description
                    status.status_supply_unit = getdata3.limit_unit
                    status.status_supply_quantity = requestqty
                    status.status_supply_remaining = getdata3.limit_quantity
                    status.status_supply_department = getdata3.limit_department
                    status.status_supply_status = "pending"
                    requesting.save()
                    status.save()
                    getdata4 = limitrecords.objects.get(limit_id = requestID).limit_description

                    messages.success(request, 'Request Successful for itemname ' + getdata4)
                    return redirect('inventorysystem-depRequestSupply')


    context = {
        'info1': info1,
        'form': form,
    }
    return render(request, 'task/edit-dep-request-supply.html', context)

#------------------- WITHDRAW SUPPLIES -----------------------------
def suppliesWithdraw(request):
    info = acceptSupplyRequests.objects.all()
    info1 = withdrawsupply.objects.all()
    context = {
        'info': info,
        'info1': info1,
    }
    return render(request, 'task/supplies-withdraw.html', context)


def updateSupplyWithdraw(request, pk):
    data = acceptSupplyRequests.objects.get(acceptSupplyRequests_id=pk)
    form = withdrawStatusForm(request.POST or None, instance=data)
    if request.method == 'POST':
        getdata4 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id=pk).acceptSupplyRequests_id
        getdata5 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id = getdata4)

        update_storage = supplymainstorage()
        getdata = supplymainstorage.objects.get(Description = getdata5.arequest_supply_description)
        update_storage.Description = getdata5.arequest_supply_description
        update_storage.Unit = getdata5.arequest_supply_unit
        update_storage.supplymainstorage_id = getdata.supplymainstorage_id
        update_storage.Quantity = int(getdata.Quantity) - int(getdata5.arequest_supply_quantity)
        getdata6 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id=pk).acceptSupplyRequests_id
        getdata7 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id = getdata6).arequest_supply_description
        supplymainstorage.objects.filter(Description = getdata7).delete()
        update_storage.save()

        update_limit = limitrecords()
        getdata3 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id=pk).acceptSupplyRequests_id
        update_limit.limit_id = getdata3
        update_limit.limit_description = getdata5.arequest_supply_description
        update_limit.limit_unit = getdata5.arequest_supply_unit
        update_limit.limit_department = getdata5.arequest_supply_department
        getdata1 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id=pk).acceptSupplyRequests_id
        limitqty = limitrecords.objects.get(limit_id = getdata1).limit_quantity      
        update_limit.limit_quantity = int(limitqty) - int(getdata5.arequest_supply_quantity)
        getdata8 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id=pk).acceptSupplyRequests_id
        getdata9 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id = getdata8).arequest_supply_description
        getdata10 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id = getdata8).arequest_supply_description
        limitrecords.objects.filter(limit_description = getdata9).filter(limit_department = getdata10).delete()
        update_limit.save()

        accept = withdrawsupply()
        accept.withdraw_supply_department = getdata5.arequest_supply_department
        accept.withdraw_supply_description = getdata5.arequest_supply_description
        accept.withdraw_supply_unit = getdata5.arequest_supply_unit
        accept.withdraw_supply_quantity = getdata5.arequest_supply_quantity
        accept.withdraw_supply_remaining = supplymainstorage.objects.get(Description = getdata5.arequest_supply_description).Quantity
        data1 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id=pk).acceptSupplyRequests_id
        acceptSupplyRequests.objects.filter(acceptSupplyRequests_id = data1).delete()
        statusSupplyRequest.objects.filter(statusSupplyRequests_id = getdata1).delete()         
        accept.save()

        messages.success(request, 'successfully withdraw')
        return redirect('inventorysystem-suppliesWithdraw')

    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'task/update-supply-withdraw.html', context)

def suppliesWithdrawStatus(request, pk):
    data = acceptSupplyRequests.objects.get(withdrawsupply_id=pk)
    form = withdrawStatusForm(request.POST or None, instance=data)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('inventorysystem-suppliesWithdraw')

    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'task/supply-withdraw-update.html', context)

#------------------- DELIVERY EQUIPMENTS -----------------------------
def equipmentDeliver(request):
    info = equipmentmainstorage.objects.all()
    info1 = deliveryequipment.objects.all()
    form = deliveryEquipmentForm()
    if request.method == 'POST':
        form = deliveryEquipmentForm(request.POST)
        itemname = request.POST.get('delivery_equipment_itemname')
        description = request.POST.get('delivery_equipment_description')
        brand = request.POST.get('delivery_equipment_brand')
        quantity = request.POST.get('delivery_equipment_quantity')

        if equipmentmainstorage.objects.filter(ItemName = itemname).filter(Description = description).exists() == False:
            if int(quantity) > 0:
                if form.is_valid():
                    form.save()
                    storageupdate = equipmentmainstorage()
                    storageupdate.ItemName = itemname
                    storageupdate.Description = description
                    storageupdate.Brand = brand
                    storageupdate.Remaining = quantity
                    storageupdate.Quantity = quantity
                    storageupdate.save()
                    mapping = storagemapping()
                    mapping.Category = "Equipment"
                    mapping.ItemName = itemname
                    mapping.RackNo = 0
                    mapping.LayerNo = 0
                    mapping.CabinetNo = 0
                    mapping.ShelfNo = 0
                    
                    mapping.save()
                    messages.success(request, 'Record created for ' + itemname)
                    return redirect('inventorysystem-equipmentDeliver')
            else:
                    messages.info(request, "invalid quantity")
                    return redirect('inventorysystem-equipmentDeliver')

        elif equipmentmainstorage.objects.filter(ItemName = itemname).exists() == True:
            messages.info(request, 'Itemname: '  + itemname + ' already exist ')
            return redirect('inventorysystem-equipmentDeliver')     
    context = {
        'form': form,
        'info': info,
        'info1': info1,

    }
    return render(request, 'task/equipment-delivery.html', context)


def updateEquipmentDeliver(request, pk):
    data = equipmentmainstorage.objects.get(equipmentmainstorage_id=pk)
    form = updateEquipmentSupplyForm(request.POST or None, instance=data)
    if request.method == 'POST':
        if int(request.POST.get('Remaining')) > 0:
            itemname = request.POST.get('ItemName')
            update_record = deliveryequipment()
            update_record.delivery_equipment_itemname = request.POST.get('ItemName')
            update_record.delivery_equipment_brand = request.POST.get('Brand')
            update_record.delivery_equipment_description = request.POST.get('Description')
            getdata = equipmentmainstorage.objects.get(ItemName = itemname)
            adding = int(getdata.Quantity) + int(request.POST.get('Remaining'))
            update_record.delivery_equipment_remaining = adding
            update_record.delivery_equipment_quantity = request.POST.get('Remaining')
            update_record.save()
            update_delivery = equipmentmainstorage()
            update_delivery.equipmentmainstorage_id = equipmentmainstorage.objects.get(ItemName = itemname).equipmentmainstorage_id
            update_delivery.ItemName = request.POST.get('ItemName')
            update_delivery.Brand = request.POST.get('Brand')
            update_delivery.Description = request.POST.get('Description')
            getdata = equipmentmainstorage.objects.get(ItemName = itemname)
            adding = int(getdata.Quantity) + int(request.POST.get('Remaining'))
            update_delivery.Remaining = 0
            update_delivery.Quantity = adding
            equipmentmainstorage.objects.filter(ItemName = itemname).delete()
            update_delivery.save()


            messages.success(request, 'Record updated for: ' + itemname)
            return redirect('inventorysystem-equipmentDeliver')
        else:
            messages.info(request, "invalid quantity")

    context = {
            'data': data,
            'form': form,
        }

    return render(request, 'task/update-equipment-delivery.html', context)


#------------------- ADMIN VIEW REQUEST EQUIPMENTS -----------------------------
def viewRequestEquipment(request):
    info = requestequipment.objects.all()
    context = {
            'info': info,
        }

    return render(request, 'task/view-request-equipment.html', context)

def editRequestEquipment(request, pk):
    data = requestequipment.objects.get(requestequipment_id=pk)
    form = equipmentRequestForm(request.POST or None, instance=data)
    if request.method == 'POST':
        accept = acceptEquipmentRequests()
        getdata = requestequipment.objects.get(requestequipment_id=pk).requestequipment_id
        getdata1 = requestequipment.objects.get(requestequipment_id = getdata)
        accept.acceptEquipmentRequests_id = getdata
        accept.arequest_equipment_itemname = getdata1.request_equipment_itemname
        accept.arequest_equipment_department = getdata1.request_equipment_department
        accept.arequest_equipment_description = getdata1.request_equipment_description
        accept.arequest_equipment_brand = getdata1.request_equipment_brand
        accept.arequest_equipment_quantity = getdata1.request_equipment_quantity
        accept.arequest_equipment_status = "Ready for pick-up"
        accept.arequest_equipment_remaining = 0
        accept.arequest_equipment_property_no = 0
        data1 = requestequipment.objects.get(requestequipment_id=pk).requestequipment_id
        requestequipment.objects.filter(requestequipment_id = data1).delete()       
        status = statusEquipmentRequest()
        status.statusEquipmentRequests_id = getdata
        status.status_equipment_itemname = getdata1.request_equipment_itemname
        status.status_equipment_description = getdata1.request_equipment_description
        status.status_equipment_brand = getdata1.request_equipment_brand
        status.status_equipment_quantity = getdata1.request_equipment_quantity
        status.status_equipment_department = getdata1.request_equipment_department
        status.status_equipment_status = "Ready for pick-up"  
        status.status_equipment_remaining = 0  
        statusEquipmentRequest.objects.filter(statusEquipmentRequests_id = getdata).delete()  
        accept.save()
        status.save()
        messages.success(request, 'request accepted')
        return redirect('inventorysystem-viewRequestEquipment')

    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'task/edit-request-equipment.html', context)

#------------------- DEPARTMENT REQUEST EQUIPMENTS -----------------------------
def depRequestEquipment(request):
    info = equipmentmainstorage.objects.all()
    info1  = statusEquipmentRequest.objects.all().filter(status_equipment_department = request.user)
    info2 = withdrawequipment.objects.all().filter(withdraw_equipment_issued_to = request.user)

    if request.method == 'POST':
        if int(request.POST.get('non-existing_equipment_quantity')) > 0:
            if equipmentmainstorage.objects.filter(ItemName = request.POST.get('non-existing_equipment_itemname')).exists == False:
                requesting = requestequipment()
                requesting.request_equipment_itemname = request.POST.get('non-existing_equipment_itemname')
                requesting.request_equipment_quantity = request.POST.get('non-existing_equipment_quantity')
                requesting.request_equipment_department = str(request.user)
                requesting.request_equipment_status = "pending"
                status = statusEquipmentRequest()
                status.status_equipment_itemname = request.POST.get('non-existing_equipment_itemname')
                status.status_equipment_quantity = request.POST.get('non-existing_equipment_quantity')
                status.status_equipment_department = str(request.user)
                status.status_equipment_status = "pending"
                requesting.save()
                status.save()
                messages.success(request, "Successfully Requested")
                return redirect('inventorysystem-depRequestEquipment')
                
            elif equipmentmainstorage.objects.filter(ItemName = request.POST.get('non-existing_equipment_itemname')).exists == True:
                messages.info(request, "Existing Equipment")
                return redirect('inventorysystem-depRequestEquipment')
        else:
            messages.info(request, "invalid quantity")
    context = {
        'info': info,
        'info1': info1,
        'info2': info2,
    }
    return render(request, 'task/dep-request-equipment.html', context)

def editdepRequestEquipment(request, pk):
    data = equipmentmainstorage.objects.get(equipmentmainstorage_id=pk)
    form = depRequestEquipmentForm(request.POST or None, instance=data)
    if request.method == 'POST':
        requestID = equipmentmainstorage.objects.get(equipmentmainstorage_id=pk).equipmentmainstorage_id
        requestqty = request.POST.get('RequestQuantity')
        requestingID1 = equipmentmainstorage.objects.get(equipmentmainstorage_id=pk).equipmentmainstorage_id
        requestingitem1 = equipmentmainstorage.objects.get(equipmentmainstorage_id= requestingID1).ItemName
        if statusEquipmentRequest.objects.filter(status_equipment_itemname =  requestingitem1).exists() == True:
                messages.info(request, 'You already have a request for this equipment.')
                return redirect('inventorysystem-depRequestEquipment')

        elif int(request.POST.get('Quantity')) == 0:
                messages.info(request, 'Not enough quantity for this equipment.')
                return redirect('inventorysystem-depRequestEquipment')

        elif int(request.POST.get('RequestQuantity')) <= 0:
                messages.info(request, 'Check the available quantity')
                return redirect('inventorysystem-depRequestEquipment')

        elif equipmentmainstorage.objects.filter(equipmentmainstorage_id = requestID).exists() == True:
            getdata3 = equipmentmainstorage.objects.get(equipmentmainstorage_id = requestID)
            requesting = requestequipment()
            requesting.requestequipment_id = requestID
            requesting.request_equipment_itemname = getdata3.ItemName
            requesting.request_equipment_description = getdata3.Description
            requesting.request_equipment_brand = getdata3.Brand
            requesting.request_equipment_quantity = requestqty
            requesting.request_equipment_department = str(request.user)
            requesting.request_equipment_status = "pending"
            status = statusEquipmentRequest()
            status.statusEquipmentRequests_id = requestID
            status.status_equipment_itemname = getdata3.ItemName
            status.status_equipment_description = getdata3.Description
            status.status_equipment_brand = getdata3.Brand
            status.status_equipment_quantity = requestqty
            status.status_equipment_remaining = getdata3.Quantity
            status.status_equipment_department = str(request.user)
            status.status_equipment_status = "pending"
            requesting.save()
            status.save()

            messages.success(request, 'Requesting completed')
            return redirect('inventorysystem-depRequestEquipment')

    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'task/edit-dep-request-equipment.html', context)


#------------------- WITHDRAW EQUIPMENTS -----------------------------
def equipmentWithdraw(request):
    info = acceptEquipmentRequests.objects.all()
    info1 = withdrawequipment.objects.all()
    context = {
        'info': info,
        'info1': info1,
    }
    return render(request, 'task/equipment-withdraw.html', context)

def createqrequipmentWithdraw(request, pk):
    data = acceptEquipmentRequests.objects.get(acceptEquipmentRequests_id=pk)
    form = withdrawEquipmentForm(request.POST or None, instance=data)
    if request.method == 'POST':
        getdata4 = acceptEquipmentRequests.objects.get(acceptEquipmentRequests_id=pk).acceptEquipmentRequests_id
        getdata5 = acceptEquipmentRequests.objects.get(acceptEquipmentRequests_id = getdata4)

        update_storage = equipmentmainstorage()
        getdata = equipmentmainstorage.objects.get(ItemName = getdata5.arequest_equipment_itemname)
        update_storage.Description = getdata5.arequest_equipment_description
        update_storage.ItemName = getdata5.arequest_equipment_itemname        
        update_storage.equipmentmainstorage_id = getdata.equipmentmainstorage_id
        update_storage.Quantity = int(getdata.Quantity) - int(getdata5.arequest_equipment_quantity)
        getdata6 = acceptEquipmentRequests.objects.get(acceptEquipmentRequests_id=pk).acceptEquipmentRequests_id
        getdata7 = acceptEquipmentRequests.objects.get(acceptEquipmentRequests_id = getdata6).arequest_equipment_description
        supplymainstorage.objects.filter(Description = getdata7).delete()
        update_storage.save()

        accept = withdrawequipment()
        getdata2 = acceptEquipmentRequests.objects.get(acceptEquipmentRequests_id=pk).acceptEquipmentRequests_id
        accept.withdraw_equipment_property_no = request.POST.get('arequest_equipment_property_no')
        accept.withdraw_equipment_itemname = request.POST.get('arequest_equipment_itemname')
        accept.withdraw_equipment_description = request.POST.get('arequest_equipment_description')
        accept.withdraw_equipment_brand = request.POST.get('arequest_equipment_brand')
        accept.withdraw_equipment_yearacquired = request.POST.get('arequest_equipment_yearacquired')
        accept.withdraw_equipment_issued_to = request.POST.get('arequest_equipment_department')
        accept.withdraw_equipment_model_no = request.POST.get('arequest_equipment_serial_no')
        accept.withdraw_equipment_serial_no = request.POST.get('arequest_equipment_serial_no')
        accept.withdraw_equipment_certifiedcorrect = request.POST.get('arequest_equipment_certifiedcorrect')
        data1 = acceptEquipmentRequests.objects.get(acceptEquipmentRequests_id=pk).acceptEquipmentRequests_id
        acceptEquipmentRequests.objects.filter(acceptEquipmentRequests_id = data1).delete()
        statusEquipmentRequest.objects.filter(statusEquipmentRequests_id = getdata2).delete()         
        accept.save()


        messages.success(request, 'successfully withdraw')
        return redirect('inventorysystem-equipmentWithdraw')
    context = {
        'data': data,
        'form': form,
    }

    return render(request, 'task/createqr-equipment-withdraw.html', context)

#------------------- RETURN EQUIPMENTS -----------------------------
def equipmentReturn(request):
    info = returnequipment.objects.all()
    # print(request.POST.get('property'))

    if request.method == 'POST':
        data = request.POST.get('property')
        getdata = withdrawequipment.objects.get(withdraw_equipment_property_no = data)
        return1 = returnequipment()
        return1.return_equipment_property_no = getdata.withdraw_equipment_property_no
        return1.return_equipment_itemname = getdata.withdraw_equipment_itemname
        return1.return_equipment_description = getdata.withdraw_equipment_description
        return1.return_equipment_brand = getdata.withdraw_equipment_brand
        return1.return_equipment_yearacquired = getdata.withdraw_equipment_yearacquired
        return1.return_equipment_issued_to = getdata.withdraw_equipment_issued_to
        return1.return_equipment_model_no = getdata.withdraw_equipment_model_no
        return1.return_equipment_serial_no = getdata.withdraw_equipment_serial_no
        return1.return_equipment_certifiedcorrect = getdata.withdraw_equipment_certifiedcorrect
        return1.save()


    context = {
        'info': info
    }
    return render(request, 'task/equipment-return.html', context)


#------------------- STORAGE MAPPING -----------------------------
def storageMapping(request):
    info = storagemapping.objects.all()

    context = {
        'info': info
    }

    return render(request, 'task/storage-mapping.html', context)

def updateStoragemapping(request, pk):
    data = storagemapping.objects.get(storagemapping_id=pk)
    form = storageForm(request.POST or None, instance=data)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('inventorysystem-storageMapping')
    context = {
        'data': data,
        'form': form,
    }

    return render(request, 'task/update-storagemapping.html', context)


#------------------- EXPORT EXCEL FILE -----------------------------
def export_excel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Supply Inventory' + \
        str(datetime.datetime.now())+'.xls'
    wb =xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Supply Delivery')
    ws1 = wb.add_sheet('Equipment Delivery')
    row_num = 0
    row_num1 = 0
    supply_font = xlwt.XFStyle()
    equipment_font = xlwt.XFStyle()
    

#supply delivery
    supply_font.font.bold = True
    supplydelivery = ['Description', 'Unit',
                'Quantity', 'Remaining Quantity', 'Date']

    for col_num in range(len(supplydelivery)):
        ws.write(row_num,col_num, supplydelivery[col_num], supply_font)

    font_style = xlwt.XFStyle()

    rows = deliverysupply.objects.all().values_list(
        'delivery_supply_description', 'delivery_supply_unit',
                'delivery_supply_quantity', 'delivery_supply_remaining', 'current_date')

    for row in rows:
        row_num+= 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)


#equipment delivery
    equipment_font.font.bold = True
    equipmentdelivery = ['Itemname', 'Description', 'Brand', 'Serial No.',
                'Quantity', 'Remaining Quantity', 'Date']

    for col_num1 in range(len(equipmentdelivery)):
        ws1.write(row_num1,col_num1, equipmentdelivery[col_num1], equipment_font)

    font_style = xlwt.XFStyle()

    rows1 =deliveryequipment.objects.all().values_list(
        'delivery_equipment_itemname', 'delivery_equipment_description', 'delivery_equipment_brand', 'delivery_equipment_unit',
                'delivery_equipment_quantity', 'delivery_equipment_remaining', 'current_date')

    for row in rows1:
        row_num1+= 1

        for col_num1 in range(len(row)):
            ws1.write(row_num1, col_num1, str(row[col_num1]), font_style)

    wb.save(response)
    return response
