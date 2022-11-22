from .forms import *
from .models import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse, HttpResponseRedirect, response
from django.contrib import messages
import datetime
import xlwt

from django.core.mail import send_mail
from django.conf import settings

from django.template.loader import render_to_string
from weasyprint import HTML 
import tempfile

def home(request):
    return render(request, 'task/home.html')

def index(request):
    return render(request, 'task/index.html')   

#--------- LOGIN --------------------
def usersLogin(request):
    if request.method == "POST":
        username1 = request.POST.get('logname')
        password1 = request.POST.get('logpass1')

        username2 = request.POST.get('logusername')
        email = request.POST.get('email')
        password2 = request.POST.get('logpass2')

        user1 = authenticate(request, username=username1, password=password1)
        user2 = authenticate(request, username=username2, email=email,  password=password2)

        if (user1 is not None and user1.is_superuser) or \
        (user1 is not None and user1.is_admin) or \
        (user1 is not None and user1.is_staff):
            login(request, user1)
            messages.success(request, 'Hello ' + username1 + '!')
            return redirect('inventorysystem-home')
        else:
            messages.info(request, 'Invalid credentials. Please try again.') 

        if user2 is not None and user2.is_active:
            login(request, user2)
            messages.success(request, 'Hello ' + username2 + '!')
            return redirect('inventorysystem-depRequestSupply')
        else:
            messages.info(request, 'Invalid credentials. Please try again.')  

    return render(request, 'task/usersLogin.html')


def deptRegister(request):
    form = DeptRegisterForm()

    if request.method == "POST":
        form = DeptRegisterForm(request.POST)
        if form.is_valid():
            dept = request.POST.get('department')

            
            if dept == '':
                messages.info(request, 'Please add a department office.')

            elif CustomUser.objects.filter(department = dept).exists() == True:
                messages.info(request, 'There is already an existing account for ' + dept)

            else:
                form.save()
                messages.success(request, 'Account was created for ' + dept)
                return redirect('inventorysystem-deptRegister')
        else:
            messages.warning(request, form.errors)

    context = {
        'form': form,
    }

    return render(request, 'task/department-register.html', context)


def adminRegister(request):
    form = AdminRegisterForm()
    if request.method == "POST":
        form = DeptRegisterForm(request.POST)
        if form.is_valid():
            getRole = request.POST.get('adminRole')
            username = request.POST.get('username')  

            if getRole == 'admin':
                form.instance.is_admin = True
                form.instance.is_staff = True
 
                form.save()
                messages.success(request, 'Account was created for ' + username)
                return redirect('inventorysystem-adminRegister')
        else:
            messages.warning(request, form.errors)

    context = {
        'form': form,
    }
    return render(request, 'task/admin-register.html', context)


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
        update_description = request.POST.get('supplymainstorage_description')
        add_quantity = request.POST.get('supplymainstorage_RequestQuantity')
        update_unit = request.POST.get('supplymainstorage_unit')

        if 'delivery_new' in request.POST:
            if supplymainstorage.objects.filter(supplymainstorage_description = description).exists() == False:
                if int(quantity) > 0:
                        delivery_record = deliverysupply()
                        delivery_record.delivery_supply_description = description
                        delivery_record.delivery_supply_unit = unit
                        delivery_record.delivery_supply_quantity = quantity
                        delivery_record.delivery_supply_remaining = quantity
                        delivery_record.save()
                        storageupdate = supplymainstorage()
                        storageupdate.supplymainstorage_description = description
                        storageupdate.supplymainstorage_unit = unit
                        storageupdate.supplymainstorage_quantity = quantity
                        storageupdate.save()
                        mapping = supply_storagemapping()
                        mapping.supplyItemName = description
                        mapping.supplyRackNo = 0
                        mapping.supplyLayerNo = 0
                        mapping.supplyCabinetNo = 0
                        mapping.supplyShelfNo = 0
                        mapping.save()
                        messages.success(request, 'Record created for ' + description)
                        return redirect('inventorysystem-suppliesDeliver')
                else:
                        messages.info(request, "invalid quantity")
                        return redirect('inventorysystem-suppliesDeliver')

            elif supplymainstorage.objects.filter(supplymainstorage_description = description).exists() == True:
                messages.info(request, 'Description: '  + description + ' already exist ')
                
                return redirect('inventorysystem-suppliesDeliver')

        elif 'delivery_update' in request.POST:

            if int(add_quantity) > 0:

                getdata1 = supplymainstorage.objects.get(supplymainstorage_description = update_description)
            
                update_record = deliverysupply()
                update_record.delivery_supply_description = getdata1.supplymainstorage_description
                update_record.delivery_supply_unit = getdata1.supplymainstorage_unit
                adding = int(getdata1.supplymainstorage_quantity) + int(add_quantity)
                update_record.delivery_supply_quantity = add_quantity
                update_record.delivery_supply_remaining = adding
                update_record.save()

                update_delivery = supplymainstorage()
                update_delivery.supplymainstorage_id = getdata1.supplymainstorage_id
                update_delivery.supplymainstorage_description = update_description
                update_delivery.supplymainstorage_unit = update_unit
                adding1 = int(getdata1.supplymainstorage_quantity) + int(add_quantity)
                update_delivery.supplymainstorage_quantity = adding1
                supplymainstorage.objects.filter(supplymainstorage_description = update_description).filter(supplymainstorage_unit = update_unit).delete()
                update_delivery.save()

                messages.success(request, 'Record updated for: ' + str(getdata1.supplymainstorage_description))
                return redirect('inventorysystem-suppliesDeliver')

        else:
            messages.info(request, "invalid quantity")

    
    context = {
        'form': form,
        'info': info,
        'info1': info1,
    }

    return render(request, 'task/supplies-delivery.html', context)


#------------------- STATUS LIMIT SUPPLIES -----------------------------
def statusLimit(request):
    info = supplymainstorage.objects.all()
    info1 = limitrecords.objects.all()
    if request.method == 'POST':
        description = request.POST.get('non-existing_description')
        unit = request.POST.get('non-existing_unit')
        quantity = request.POST.get('non-existing_quantity')
        department = request.POST.get('non-existing_department')
        update_limit_department = request.POST.get('limit_department')
        update_limit_description = request.POST.get('limit_description')
        update_limit_unit = request.POST.get('limit_unit')
        update_limit_quantity = request.POST.get('limit_quantity')
        update_limit_addquantity = request.POST.get('limit_addquantity')

        if 'new_limit' in request.POST:

            if supplymainstorage.objects.filter(supplymainstorage_description = description).filter(supplymainstorage_unit = unit).exists() == True:
                if int(request.POST.get('non-existing_quantity')) > 0:
                    if CustomUser.objects.filter(department = department).exists() == True:

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

                    elif CustomUser.objects.filter(department = department).exists() == False:
                        messages.info(request, "no available account for this department")

                else:
                    messages.info(request, "invalid quantity")
                    
            elif  supplymainstorage.objects.filter(supplymainstorage_description = description).filter(supplymainstorage_unit = unit).exists() == False:
                messages.info(request, "No Existing item name: " +  description +  " with a unit: " + unit + " in supply mainstorage")

        if 'update_limit' in request.POST:
            
            getdata = limitrecords.objects.get(limit_description = update_limit_description)
            if int(update_limit_addquantity) > 0:
                update_record = limitrecords()
                update_record.limit_id = getdata.limit_id
                update_record.limit_description = update_limit_description
                update_record.limit_unit = update_limit_unit
                update_record.limit_department = update_limit_department
                adding = int(getdata.limit_quantity) + int(update_limit_addquantity)
                update_record.limit_quantity = adding
                limitrecords.objects.filter(limit_id = getdata.limit_id).delete()
                update_record.save()


                messages.success(request, 'Record updated for Itemname: ' + update_limit_description +  " with a unit: " + update_limit_unit + " into department: " + update_limit_department)
                return redirect('inventorysystem-statusLimit')
            else:
                messages.info(request, "invalid quantity")


    context = {
        'info': info,
        'info1': info1,
    }
    return render(request, 'task/status-limit.html', context)


#------------------- ADMIN VIEW REQUEST SUPPLIES -----------------------------
def viewRequestSupply(request):
    info = requestsupply.objects.all()
    # info1 = supplymainstorage.objects.filter()
    
    if request.method == 'POST':
        request_id = request.POST.get('requestsupply_id')
        request_department = request.POST.get('request_supply_department')
        request_unit = request.POST.get('request_supply_unit')
        request_description = request.POST.get('request_supply_description')
        request_quantity = request.POST.get('request_supply_quantity')
        request_accept_quantity = request.POST.get('request_supply_acceptquantity')
        getdata1 = requestsupply.objects.get(requestsupply_id = request_id).requestsupply_id
        getdata2 = requestsupply.objects.get(requestsupply_id = request_id)
        getdata3 = supplymainstorage.objects.get(supplymainstorage_description = request_description).supplymainstorage_quantity

        if int(request_accept_quantity) > int(request_quantity):

                messages.info(request, 'Your accepted quantity is greater than with the requested quantity')
                return redirect('inventorysystem-viewRequestSupply')


        elif int(request_accept_quantity) > int(getdata3):

                messages.info(request, 'Not enough quantity for this item.')
                return redirect('inventorysystem-viewRequestSupply')       

        elif int(supplymainstorage.objects.get(supplymainstorage_description = getdata2.request_supply_description).supplymainstorage_quantity) > int(request_accept_quantity) or int(supplymainstorage.objects.get(supplymainstorage_description = getdata2.request_supply_description).supplymainstorage_quantity) == int(request_accept_quantity):
            accept = acceptSupplyRequests()
            accept.acceptSupplyRequests_id = request_id
            accept.arequest_supply_department = request_department
            accept.arequest_supply_description = request_description
            accept.arequest_supply_unit = request_unit
            accept.arequest_supply_quantity = request_accept_quantity
            accept.arequest_supply_status = "Ready for pick-up"
            # data1 = requestsupply.objects.get(requestsupply_id=pk).requestsupply_id
            # subject = "Supply Department"
            # message = "Your Item is ready for pick up"
            # get1 = requestsupply.objects.get(requestsupply_id=pk).requestsupply_id
            # get2 = str(requestsupply.objects.get(requestsupply_id = getdata).request_supply_department)
            # depinfo = str(requestsupply.objects.get(requestsupply_id = getdata1).request_supply_department)
            # print(depinfo)
            # recipient = str(CustomUser.objects.get(department= get2).email)
            # # email field ng bawat department
            # send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            requestsupply.objects.filter(requestsupply_id = getdata1).delete()       
            status = statusSupplyRequest()
            status.statusSupplyRequests_id = request_id
            status.status_supply_description = request_description
            status.status_supply_unit = request_unit
            status.status_supply_quantity = request_quantity
            status.status_supply_remaining = limitrecords.objects.get(limit_id = getdata1).limit_quantity
            status.status_supply_acceptquantity = request_accept_quantity
            status.status_supply_department = request_department
            status.status_supply_status = "Ready for pick-up"  
            statusSupplyRequest.objects.filter(statusSupplyRequests_id = getdata1).delete()  
            messages.success(request, 'request accepted')
            accept.save()
            status.save()
          
            return redirect('inventorysystem-viewRequestSupply')


        else:
            number = str(supplymainstorage.objects.get(supplymainstorage_description = getdata2.request_supply_description).supplymainstorage_quantity)
            messages.info(request, 'This item does not have enough stock in the main storage,'+ ' Mainstorage Remaining: ' + number)
    context = {
        'info': info,
        # 'info1': info1,

    }
    return render(request, 'task/view-request-supplies.html', context)

#------------------- DEPARTMENT REQUEST SUPPLIES -----------------------------
def depRequestSupply(request):
    info1 = limitrecords.objects.all().filter(limit_department = request.user)
    info = statusSupplyRequest.objects.all().filter(status_supply_department = request.user)
    info2 = withdrawsupply.objects.all().filter(withdraw_supply_department = request.user)
    if request.method == 'POST':
        request_id = request.POST.get('limit_id')
        request_description = request.POST.get('request_description')
        request_unit = request.POST.get('request_unit')
        request_quantity = request.POST.get('request_quantity')
        request_addquantity = request.POST.get('request_addquantity')
        # requestingID = limitrecords.objects.get(limit_description = request_description).limit_id
        
        if statusSupplyRequest.objects.filter(status_supply_description = request.POST.get('request_description')).filter(status_supply_department = request.user).exists() == True:
            
                messages.info(request, 'You already have a request for this item.')
                return redirect('inventorysystem-depRequestSupply')

        elif int(request_addquantity) == 0:
                messages.info(request, 'Not enough quantity for this item.')
                return redirect('inventorysystem-depRequestSupply')

        elif int(request_addquantity) > int(request_quantity):
                messages.info(request, 'Not enough quantity for this item.')
                return redirect('inventorysystem-depRequestSupply')

        elif int(request_addquantity) <= 0:
                messages.info(request, 'Check the available quantity')
                return redirect('inventorysystem-depRequestSupply')

        elif statusSupplyRequest.objects.filter(status_supply_description = request.POST.get('request_description')).filter(status_supply_department = request.user).exists() == False:
    
                # if limitrecords.objects.filter(limit_id = requestingID).exists() == True:
                #     getdata3 = limitrecords.objects.get(limit_id = requestingID)
                    requesting = requestsupply()
                    requesting.requestsupply_id = request_id
                    requesting.request_supply_description = request_description
                    requesting.request_supply_unit = request_unit
                    requesting.request_supply_quantity = request_addquantity
                    requesting.request_supply_remaining = request_quantity
                    requesting.request_supply_department = str(request.user)
                    requesting.request_supply_status = "pending"
                    status = statusSupplyRequest()
                    status.status_supply_description = request_description
                    status.status_supply_unit = request_unit
                    status.status_supply_quantity = request_addquantity
                    status.status_supply_remaining = request_quantity
                    status.status_supply_department = request.user
                    status.status_supply_status = "pending"
                    requesting.save()
                    status.save()

                    messages.success(request, 'Request Successful for itemname ')
                    # # subject = str(limitrecords.objects.get(limit_id = requestingID).limit_department)
                    # # message = "New Request"
                    # # depinfo = str(CustomUser.objects.get(is_superuser=True).email)
                    # # # limitrecords.objects.get(limit_id = requestID).limit_department
                    # # # str(CustomUser.objects.get(department= depinfo).email)
                    # # print(depinfo)
                    # # recipient = depinfo
                    # # # email ni sir gascon 
                    # # send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
                    return redirect('inventorysystem-depRequestSupply')

    context = {
        'info1': info1,
        'info': info,
        'info2': info2,
    }   
    return render(request, 'task/dep-request-supply.html', context)


#------------------- WITHDRAW SUPPLIES -----------------------------
def suppliesWithdraw(request):
    info = acceptSupplyRequests.objects.all()
    info1 = withdrawsupply.objects.all()

    if request.method == 'POST':
        getdata = request.POST.get('acceptSupplyRequests_id')
        withdraw_department = request.POST.get('arequest_supply_department')
        withdraw_description = request.POST.get('arequest_supply_description')
        withdraw_unit = request.POST.get('arequest_supply_unit')
        withdraw_quantity = request.POST.get('arequest_supply_quantity')
        getdata1 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id = getdata).acceptSupplyRequests_id

        update_storage = supplymainstorage()
        getdata2 = supplymainstorage.objects.get(supplymainstorage_description = withdraw_description)
        update_storage.supplymainstorage_description = withdraw_description
        update_storage.supplymainstorage_unit = withdraw_unit
        update_storage.supplymainstorage_id = getdata2.supplymainstorage_id
        update_storage.supplymainstorage_quantity = int(getdata2.supplymainstorage_quantity) - int(withdraw_quantity)
        supplymainstorage.objects.filter(supplymainstorage_description = withdraw_description).delete()
        update_storage.save()

        update_limit = limitrecords()
        update_limit.limit_id = getdata
        update_limit.limit_description = withdraw_description
        update_limit.limit_unit = withdraw_unit
        update_limit.limit_department = withdraw_department
        limitqty = limitrecords.objects.get(limit_id = getdata1).limit_quantity      
        update_limit.limit_quantity = int(limitqty) - int(withdraw_quantity)
        # limitrecords.objects.filter(limit_description = withdraw_description).filter(limit_department = withdraw_department).delete()
        update_limit.save()

        accept = withdrawsupply()
        accept.withdraw_supply_department = withdraw_department
        accept.withdraw_supply_description = withdraw_description
        accept.withdraw_supply_unit = withdraw_unit
        accept.withdraw_supply_quantity = withdraw_quantity
        accept.withdraw_supply_remaining = supplymainstorage.objects.get(supplymainstorage_description = withdraw_description).supplymainstorage_quantity
        acceptSupplyRequests.objects.filter(acceptSupplyRequests_id = getdata1).delete()
        statusSupplyRequest.objects.filter(statusSupplyRequests_id = getdata1).delete()         
        accept.save()

        messages.success(request, 'successfully withdraw')
        return redirect('inventorysystem-suppliesWithdraw')
    context = {
        'info': info,
        'info1': info1,
    }
    return render(request, 'task/supplies-withdraw.html', context)


#------------------- DELIVERY EQUIPMENTS -----------------------------
def equipmentDeliver(request):
    info = equipmentmainstorage.objects.all()
    info1 = deliveryequipment.objects.all()
    info2 = requestequipment.objects.all()
    form = deliveryEquipmentForm()
    if request.method == 'POST':
        form = deliveryEquipmentForm(request.POST)
        itemname = request.POST.get('delivery_equipment_itemname')
        description = request.POST.get('delivery_equipment_description')
        brand = request.POST.get('delivery_equipment_brand')
        quantity = request.POST.get('delivery_equipment_quantity')
        update_itemname = request.POST.get('equipmentmainstorage_itemName')
        update_description = request.POST.get('equipmentmainstorage_description')
        update_brand = request.POST.get('equipmentmainstorage_brand')
        update_quantity = request.POST.get('equipmentmainstorage_RequestQuantity')

    
        if 'delivery_equipment_new' in request.POST:

            if requestequipment.objects.filter(request_equipment_itemname = itemname).exists() == False:

                if equipmentmainstorage.objects.filter(equipmentmainstorage_itemName = itemname).filter(equipmentmainstorage_description = description).exists() == False:
                    if int(quantity) > 0:
                        delivery_record = deliveryequipment()
                        delivery_record.delivery_equipment_itemname = itemname
                        delivery_record.delivery_equipment_description = description
                        delivery_record.delivery_equipment_brand = brand
                        delivery_record.delivery_equipment_quantity = quantity
                        delivery_record.delivery_equipment_remaining = quantity
                        delivery_record.save()
                        storageupdate = equipmentmainstorage()
                        storageupdate.equipmentmainstorage_itemName = itemname
                        storageupdate.equipmentmainstorage_description = description
                        storageupdate.equipmentmainstorage_brand = brand
                        storageupdate.equipmentmainstorage_remaining = quantity
                        storageupdate.equipmentmainstorage_quantity = quantity
                        storageupdate.save()
                        mapping = equipment_storagemapping()
                        mapping.equipmentItemName = itemname
                        mapping.equipmentLocation = "Supply Office"
                        mapping.save()
                        messages.success(request, 'Record created for ' + itemname)
                        return redirect('inventorysystem-equipmentDeliver')
                    else:
                            messages.info(request, "invalid quantity")
                            return redirect('inventorysystem-equipmentDeliver')

                elif equipmentmainstorage.objects.filter(equipmentmainstorage_itemName = itemname).exists() == True:
                    messages.info(request, 'Itemname: '  + itemname + ' already exist ')
                    return redirect('inventorysystem-equipmentDeliver')    

            elif requestequipment.objects.filter(request_equipment_itemname = itemname).exists() == True:
                 messages.info(request, 'Equipment: '  + itemname + ' have a pending request from department')
                 return redirect('inventorysystem-equipmentDeliver')

        elif 'delivery_equipment_update' in request.POST:

            getdata = equipmentmainstorage.objects.get(equipmentmainstorage_itemName = update_itemname)
            if int(update_quantity) > 0:
                update_record = deliveryequipment()
                update_record.delivery_equipment_itemname = update_itemname
                update_record.delivery_equipment_brand = update_brand
                update_record.delivery_equipment_description = update_description
                adding = int(getdata.equipmentmainstorage_quantity) + int(update_quantity)
                update_record.delivery_equipment_remaining = adding
                update_record.delivery_equipment_quantity = update_quantity
                update_record.save()

                update_delivery = equipmentmainstorage()
                update_delivery.equipmentmainstorage_id = getdata.equipmentmainstorage_id
                update_delivery.equipmentmainstorage_itemName = update_itemname
                update_delivery.equipmentmainstorage_brand = update_brand
                update_delivery.equipmentmainstorage_description = update_description
                adding = int(getdata.equipmentmainstorage_quantity) + int(update_quantity)
                update_delivery.equipmentmainstorage_quantity = adding
                equipmentmainstorage.objects.filter(equipmentmainstorage_itemName = update_itemname).delete()
                update_delivery.save()


                messages.success(request, 'Record updated for: ' + str(update_itemname))
                return redirect('inventorysystem-equipmentDeliver')
            else:
                messages.info(request, "invalid quantity") 

        elif 'delivery_dep' in request.POST:

            request_id = request.POST.get('requestequipment_id')
            request_department = request.POST.get('request_equipment_department')
            request_itemname = request.POST.get('request_equipment_itemname')
            request_quantity = request.POST.get('request_equipment_quantity')
            request_description = request.POST.get('request_equipment_description')
            request_brand = request.POST.get('request_equipment_brand')
            request_acceptquantity = request.POST.get('request_equipment_acceptquantity')
            getdata = requestequipment.objects.get(requestequipment_id=request_id).requestequipment_id

            if request_acceptquantity > request_quantity:

                messages.info(request, 'request quantity is less than to accept quantity')
                return redirect('inventorysystem-equipmentDeliver')
            
            elif request_acceptquantity < request_quantity:

                accept = acceptEquipmentRequests()
                accept.acceptEquipmentRequests_id = getdata
                accept.arequest_equipment_itemname = request_itemname
                accept.arequest_equipment_issued_to = request_department
                accept.arequest_equipment_description = request_description
                accept.arequest_equipment_brand = request_brand
                accept.arequest_equipment_quantity = request_acceptquantity
                accept.arequest_equipment_status = "Ready for pick-up"
                accept.arequest_equipment_remaining = 0
                accept.arequest_equipment_property_no = 0
                requestequipment.objects.filter(requestequipment_id = getdata).delete()       
                status = statusEquipmentRequest()
                status.statusEquipmentRequests_id = getdata
                status.status_equipment_itemname = request_itemname
                status.status_equipment_description = request_description
                status.status_equipment_brand = request_brand
                status.status_equipment_quantity = request_quantity
                status.status_equipment_acceptquantity = request_acceptquantity
                status.status_equipment_department = request_department
                status.status_equipment_status = "Ready for pick-up"  
                status.status_equipment_remaining = 0  
                statusEquipmentRequest.objects.filter(statusEquipmentRequests_id = getdata).delete()  
                accept.save()
                status.save()
                messages.success(request, 'request accepted')
                return redirect('inventorysystem-equipmentDeliver')



    context = {
        'form': form,
        'info': info,
        'info1': info1,
        'info2': info2,

    }
    return render(request, 'task/equipment-delivery.html', context)



#------------------- ADMIN VIEW REQUEST EQUIPMENTS -----------------------------
def viewDeliveryRecords(request):
    info = equipmentmainstorage.objects.all()
    context = {
            'info': info,
        }
    return render(request, 'task/view-delivery-records.html', context) 

# def viewRequestEquipment(request):
#     info = requestequipment.objects.all()
#     if request.method == 'POST':
        # request_id = request.POST.get('requestequipment_id')
        # request_department = request.POST.get('request_equipment_department')
        # request_itemname = request.POST.get('request_equipment_itemname')
        # request_quantity = request.POST.get('request_equipment_quantity')
        # request_description = request.POST.get('request_equipment_description')
        # request_brand = request.POST.get('request_equipment_brand')
        # request_acceptquantity = request.POST.get('request_equipment_acceptquantity')
        # getdata = requestequipment.objects.get(requestequipment_id=request_id).requestequipment_id

        # if request_acceptquantity > request_quantity:

        #     messages.info(request, 'request quantity is less than to accept quantity')
        #     return redirect('inventorysystem-viewRequestEquipment')
        
        # elif request_acceptquantity < request_quantity:

        #     accept = acceptEquipmentRequests()
        #     accept.acceptEquipmentRequests_id = getdata
        #     accept.arequest_equipment_itemname = request_itemname
        #     accept.arequest_equipment_issued_to = request_department
        #     accept.arequest_equipment_description = request_description
        #     accept.arequest_equipment_brand = request_brand
        #     accept.arequest_equipment_quantity = request_acceptquantity
        #     accept.arequest_equipment_status = "Ready for pick-up"
        #     accept.arequest_equipment_remaining = 0
        #     accept.arequest_equipment_property_no = 0
        #     requestequipment.objects.filter(requestequipment_id = getdata).delete()       
        #     status = statusEquipmentRequest()
        #     status.statusEquipmentRequests_id = getdata
        #     status.status_equipment_itemname = request_itemname
        #     status.status_equipment_description = request_description
        #     status.status_equipment_brand = request_brand
        #     status.status_equipment_quantity = request_quantity
        #     status.status_equipment_acceptquantity = request_acceptquantity
        #     status.status_equipment_department = request_department
        #     status.status_equipment_status = "Ready for pick-up"  
        #     status.status_equipment_remaining = 0  
        #     statusEquipmentRequest.objects.filter(statusEquipmentRequests_id = getdata).delete()  
        #     accept.save()
        #     status.save()
        #     messages.success(request, 'request accepted')
#             return redirect('inventorysystem-viewRequestEquipment')

#     context = {
#             'info': info,
#         }

#     return render(request, 'task/view-request-equipment.html', context)


#------------------- DEPARTMENT REQUEST EQUIPMENTS -----------------------------
def depRequestEquipment(request):
    info = equipmentmainstorage.objects.all()
    info1  = statusEquipmentRequest.objects.all().filter(status_equipment_department = request.user)
    info2 = withdrawequipment.objects.all().filter(withdraw_equipment_issued_to = request.user)

    if request.method == 'POST':
        if int(request.POST.get('non_existing_equipment_quantity')) > 0:
            if statusEquipmentRequest.objects.filter(status_equipment_itemname = request.POST.get('non_existing_equipment_itemname')).filter(status_equipment_department = request.user).exists() == False:
                requesting = requestequipment()
                requesting.request_equipment_itemname = request.POST.get('non_existing_equipment_itemname')
                requesting.request_equipment_quantity = request.POST.get('non_existing_equipment_quantity')
                requesting.request_equipment_department = str(request.user)
                requesting.request_equipment_status = "pending"
                status = statusEquipmentRequest()
                status.status_equipment_itemname = request.POST.get('non_existing_equipment_itemname')
                status.status_equipment_quantity = request.POST.get('non_existing_equipment_quantity')
                status.status_equipment_department = str(request.user)
                status.status_equipment_status = "pending"
                requesting.save()
                status.save()
                messages.success(request, "Successfully Requested")
                return redirect('inventorysystem-depRequestEquipment')

            elif statusEquipmentRequest.objects.filter(status_equipment_itemname = request.POST.get('non_existing_equipment_itemname')).filter(status_equipment_department = request.user).exists() == True:
                messages.info(request, 'You already have a request for this item.')
                return redirect('inventorysystem-depRequestEquipment')
                
        else:
            messages.info(request, "invalid quantity")
    context = {
        'info': info,
        'info1': info1,
        'info2': info2,
    }
    return render(request, 'task/dep-request-equipment.html', context)


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
 
        if equipmentmainstorage.objects.filter(equipmentmainstorage_description = request.POST.get('arequest_equipment_description')).exists() == False:

            accept = withdrawequipment()
            getdata2 = acceptEquipmentRequests.objects.get(acceptEquipmentRequests_id=pk).acceptEquipmentRequests_id
            accept.withdraw_equipment_property_no = request.POST.get('arequest_equipment_property_no')
            accept.withdraw_equipment_itemname = request.POST.get('arequest_equipment_itemname')
            accept.withdraw_equipment_description = request.POST.get('arequest_equipment_description')
            accept.withdraw_equipment_brand = request.POST.get('arequest_equipment_brand')
            accept.withdraw_equipment_yearacquired = request.POST.get('arequest_equipment_yearacquired')
            accept.withdraw_equipment_issued_to = request.POST.get('arequest_equipment_issued_to')
            accept.withdraw_equipment_model_no = request.POST.get('arequest_equipment_model_no')
            accept.withdraw_equipment_serial_no = request.POST.get('arequest_equipment_serial_no')
            accept.withdraw_equipment_certifiedcorrect = request.POST.get('arequest_equipment_certifiedcorrect')
            data1 = acceptEquipmentRequests.objects.get(acceptEquipmentRequests_id=pk).acceptEquipmentRequests_id

            if int(acceptEquipmentRequests.objects.get(acceptEquipmentRequests_id = data1).arequest_equipment_quantity) == 1:
                acceptEquipmentRequests.objects.filter(acceptEquipmentRequests_id = data1).delete()
                statusEquipmentRequest.objects.filter(statusEquipmentRequests_id = getdata2).delete()         
                accept.save()
                messages.success(request, 'successfully withdraw')
                return redirect('inventorysystem-equipmentWithdraw')


            elif int(acceptEquipmentRequests.objects.get(acceptEquipmentRequests_id = data1).arequest_equipment_quantity) > 1:

                not_delete = acceptEquipmentRequests()
                not_delete.acceptEquipmentRequests_id = getdata4
                not_delete.arequest_equipment_itemname = getdata5.arequest_equipment_itemname
                not_delete.arequest_equipment_description = getdata5.arequest_equipment_description
                not_delete.arequest_equipment_brand = getdata5.arequest_equipment_brand
                not_delete.arequest_equipment_quantity = int(getdata5.arequest_equipment_quantity) - 1
                not_delete.arequest_equipment_status = getdata5.arequest_equipment_status
                not_delete.arequest_equipment_issued_to = getdata5.arequest_equipment_issued_to
                not_delete.current_date = getdata5.current_date
                not_delete.save()
                accept.save()
                statusEquipmentRequest.objects.filter(statusEquipmentRequests_id = getdata2).delete() 
                messages.success(request, 'successfully withdraw')
                return redirect('inventorysystem-equipmentWithdraw')

        elif equipmentmainstorage.objects.filter(equipmentmainstorage_description = request.POST.get('arequest_equipment_description')).exists() == True:

            update_storage = equipmentmainstorage()
            getdata = equipmentmainstorage.objects.get(equipmentmainstorage_itemName = getdata5.arequest_equipment_itemname)
            update_storage.equipmentmainstorage_description = getdata5.arequest_equipment_description
            update_storage.equipmentmainstorage_itemName = getdata5.arequest_equipment_itemname        
            update_storage.equipmentmainstorage_id = getdata.equipmentmainstorage_id
            update_storage.equipmentmainstorage_quantity = int(getdata.equipmentmainstorage_quantity) - int(getdata5.arequest_equipment_quantity)
            getdata6 = acceptEquipmentRequests.objects.get(acceptEquipmentRequests_id=pk).acceptEquipmentRequests_id
            getdata7 = acceptEquipmentRequests.objects.get(acceptEquipmentRequests_id = getdata6).arequest_equipment_description
            equipmentmainstorage.objects.filter(equipmentmainstorage_description = getdata7).delete()
            update_storage.save()

            accept = withdrawequipment()
            getdata2 = acceptEquipmentRequests.objects.get(acceptEquipmentRequests_id=pk).acceptEquipmentRequests_id
            accept.withdraw_equipment_property_no = request.POST.get('arequest_equipment_property_no')
            accept.withdraw_equipment_itemname = request.POST.get('arequest_equipment_itemname')
            accept.withdraw_equipment_description = request.POST.get('arequest_equipment_description')
            accept.withdraw_equipment_brand = request.POST.get('arequest_equipment_brand')
            accept.withdraw_equipment_yearacquired = request.POST.get('arequest_equipment_yearacquired')
            accept.withdraw_equipment_issued_to = request.POST.get('arequest_equipment_issued_to')
            accept.withdraw_equipment_model_no = request.POST.get('arequest_equipment_model_no')
            accept.withdraw_equipment_serial_no = request.POST.get('arequest_equipment_serial_no')
            accept.withdraw_equipment_certifiedcorrect = request.POST.get('arequest_equipment_certifiedcorrect')
            data1 = acceptEquipmentRequests.objects.get(acceptEquipmentRequests_id=pk).acceptEquipmentRequests_id
            acceptEquipmentRequests.objects.filter(acceptEquipmentRequests_id = data1).delete()
            statusEquipmentRequest.objects.filter(statusEquipmentRequests_id = getdata2).delete()         
            accept.save()

            if int(acceptEquipmentRequests.objects.get(acceptEquipmentRequests_id = data1).arequest_equipment_quantity) == 1:
                acceptEquipmentRequests.objects.filter(acceptEquipmentRequests_id = data1).delete()
                statusEquipmentRequest.objects.filter(statusEquipmentRequests_id = getdata2).delete()         
                accept.save()
                messages.success(request, 'successfully withdraw')
                return redirect('inventorysystem-equipmentWithdraw')


            elif int(acceptEquipmentRequests.objects.get(acceptEquipmentRequests_id = data1).arequest_equipment_quantity) > 1:

                not_delete = acceptEquipmentRequests()
                not_delete.acceptEquipmentRequests_id = getdata4
                not_delete.arequest_equipment_itemname = getdata5.arequest_equipment_itemname
                not_delete.arequest_equipment_description = getdata5.arequest_equipment_description
                not_delete.arequest_equipment_brand = getdata5.arequest_equipment_brand
                not_delete.arequest_equipment_quantity = int(getdata5.arequest_equipment_quantity) - 1
                not_delete.arequest_equipment_status = getdata5.arequest_equipment_status
                not_delete.arequest_equipment_issued_to = getdata5.arequest_equipment_issued_to
                not_delete.current_date = getdata5.current_date
                not_delete.save()
                accept.save()
                statusEquipmentRequest.objects.filter(statusEquipmentRequests_id = getdata2).delete() 
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
    info = supply_storagemapping.objects.all()
    info1 = equipment_storagemapping.objects.all()

    if request.method == 'POST':

        if 'storagesupply_update' in request.POST:
            locsave = supply_storagemapping()
            locsave.supplyStoragemapping_id = request.POST.get('supplyStoragemapping_id')
            locsave.supplyItemName = request.POST.get('supplyItemName')
            locsave.supplyRackNo = request.POST.get('supplyRackNo')
            locsave.supplyLayerNo = request.POST.get('supplyLayerNo')
            locsave.supplyCabinetNo = request.POST.get('supplyCabinetNo')
            locsave.supplyShelfNo = request.POST.get('supplyShelfNo')
            locsave.save()
            messages.success(request, 'successfully update storage mapping')
            return redirect('inventorysystem-storageMapping')


    context = {
        'info': info,
        'info1': info1
    }

    return render(request, 'task/storage-mapping.html', context)


#------------------- EXPORT EXCEL FILE -----------------------------
def export_excel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Supply Inventory' + '.xls'
    wb =xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Supply Delivery')
    ws1 = wb.add_sheet('Equipment Delivery')
    ws2 = wb.add_sheet('Supply Withdraw')
    ws3 = wb.add_sheet('Equipment Withdraw')
    ws4 = wb.add_sheet('Returned Equipment')
    row_num = 0
    row_num1 = 0
    row_num2 = 0
    row_num3 = 0
    row_num4 = 0
    supply_font = xlwt.XFStyle()
    equipment_font = xlwt.XFStyle()
    wsupply_font = xlwt.XFStyle()
    wequipment_font = xlwt.XFStyle()
    equipreturn_font = xlwt.XFStyle()
    

#supply delivery
    supply_font.font.bold = True
    supplydelivery = ['Description', 'Unit', 'Quantity', 'Remaining Quantity', 'Date and Time']

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
    equipmentdelivery = ['Itemname', 'Description', 'Brand',
                'Quantity', 'Remaining Quantity', 'Date and Time']

    for col_num1 in range(len(equipmentdelivery)):
        ws1.write(row_num1,col_num1, equipmentdelivery[col_num1], equipment_font)

    font_style = xlwt.XFStyle()

    rows1 =deliveryequipment.objects.all().values_list(
        'delivery_equipment_itemname', 'delivery_equipment_description', 'delivery_equipment_brand',
                'delivery_equipment_quantity', 'delivery_equipment_remaining', 'current_date')

    for row in rows1:
        row_num1+= 1

        for col_num1 in range(len(row)):
            ws1.write(row_num1, col_num1, str(row[col_num1]), font_style)

#supply withdraw
    wsupply_font.font.bold = True
    supplywithdraw = ['Department', 'Description', 'Unit', 'Withdrawn Quantity', 'Date and Time']

    for col_num2 in range(len(supplywithdraw)):
        ws2.write(row_num2,col_num2, supplywithdraw[col_num2], wsupply_font)

    font_style = xlwt.XFStyle()

    rows2 = withdrawsupply.objects.all().values_list( 'withdraw_supply_department',
        'withdraw_supply_description', 'withdraw_supply_unit', 'withdraw_supply_quantity', 'current_date')

    for row in rows2:
        row_num2+= 1

        for col_num2 in range(len(row)):
            ws2.write(row_num2, col_num2, str(row[col_num2]), font_style)

#equipment withdraw
    wequipment_font.font.bold = True
    equipmentwithdraw = ['Property No.', 'Item Name', 'Description', 
                'Brand', 'Year Acquired', 'Issued to', 'Model No.', 'SerialNo.',
                'Certified Correct', 'Date and Time']

    for col_num3 in range(len(equipmentwithdraw)):
        ws3.write(row_num3,col_num3, equipmentwithdraw[col_num3], wequipment_font)

    font_style = xlwt.XFStyle()

    rows3 = withdrawequipment.objects.all().values_list(
        'withdraw_equipment_property_no', 'withdraw_equipment_itemname', 
        'withdraw_equipment_description', 'withdraw_equipment_brand', 'withdraw_equipment_yearacquired',
        'withdraw_equipment_issued_to', 'withdraw_equipment_model_no', 'withdraw_equipment_serial_no', 
        'withdraw_equipment_certifiedcorrect', 'current_date')

    for row in rows3:
        row_num3+= 1

        for col_num3 in range(len(row)):
            ws3.write(row_num3, col_num3, str(row[col_num3]), font_style)

#return equipment
    equipreturn_font.font.bold = True
    equipreturn = ['Property No.', 'Item Name', 'Description', 
                'Brand', 'Year Acquired', 'Issued to', 'Model No.', 'SerialNo.',
                'Certified Correct', 'Date Returned']

    for col_num4 in range(len(equipreturn)):
        ws4.write(row_num4,col_num4, equipreturn[col_num4], equipreturn_font)

    font_style = xlwt.XFStyle()

    rows4 = returnequipment.objects.all().values_list(
        'return_equipment_property_no', 'return_equipment_itemname', 
        'return_equipment_description', 'return_equipment_brand', 'return_equipment_yearacquired',
        'return_equipment_issued_to', 'return_equipment_model_no', 'return_equipment_serial_no', 
        'return_equipment_certifiedcorrect', 'return_date')

    for row in rows4:
        row_num4+= 1

        for col_num4 in range(len(row)):
            ws4.write(row_num4, col_num4, str(row[col_num4]), font_style)

    wb.save(response)
    return response


#------------------- EXPORT PDF FILE -----------------------------
def export_pdf_suppydelivery(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename=Supply Inventory' + \
        str(datetime.datetime.now())+'.pdf'
    supply = deliverysupply.objects.all()
    response['Content-Transfer-Enconding'] = 'binary'


    html_string = render_to_string('task/pdf-output-supplydelivery.html' ,{'Supplydelivery': supply})
    html = HTML(string=html_string)
    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=False) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    
    return response

def export_pdf_suppywithdraw(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename=Supply Inventory' + \
        str(datetime.datetime.now())+'.pdf'
    supply = withdrawsupply.objects.all()
    response['Content-Transfer-Enconding'] = 'binary'


    html_string = render_to_string('task/pdf-output-supplywithdraw.html' ,{'Supplywithdraw': supply})
    html = HTML(string=html_string)
    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=False) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    
    return response

def export_pdf_equipdelivery(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename=Supply Inventory' + \
        str(datetime.datetime.now())+'.pdf'
    supply = deliveryequipment.objects.all()
    response['Content-Transfer-Enconding'] = 'binary'


    html_string = render_to_string('task/pdf-output-equipdelivery.html' ,{'Equipdelivery': supply})
    html = HTML(string=html_string)
    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=False) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    
    return response

def export_pdf_equipwithdraw(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename=Supply Inventory' + \
        str(datetime.datetime.now())+'.pdf'
    supply = withdrawequipment.objects.all()
    response['Content-Transfer-Enconding'] = 'binary'


    html_string = render_to_string('task/pdf-output-equipwithdraw.html' ,{'Equipwithdraw': supply})
    html = HTML(string=html_string)
    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=False) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    
    return response

def export_pdf_equipreturn(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename=Supply Inventory' + \
        str(datetime.datetime.now())+'.pdf'
    supply = returnequipment.objects.all()
    response['Content-Transfer-Enconding'] = 'binary'


    html_string = render_to_string('task/pdf-output-equipreturn.html' ,{'EquipReturn': supply})
    html = HTML(string=html_string)
    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=False) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    
    return response