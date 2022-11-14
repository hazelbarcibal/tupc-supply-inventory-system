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
# from weasyprint import HTML 
import tempfile

def home(request):
    return render(request, 'task/home.html')

def SupplyInventorySystem(request):
    return render(request, 'task/landing-page.html')

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
                update_record.delivery_supply_description = getdata1
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

def updateSuppliesDeliver(request, pk):
    data = supplymainstorage.objects.get(supplymainstorage_id=pk)
    form = updateDeliverySupplyForm(request.POST or None, instance=data)
    # if request.method == 'POST':
    #     if int(request.POST.get('supplymainstorage_RequestQuantity')) > 0:
            
    #             getdata1 = supplymainstorage.objects.get(supplymainstorage_id=pk).supplymainstorage_id
    #             getdata2 = supplymainstorage.objects.get(supplymainstorage_id= getdata1).supplymainstorage_description
    #             update_record = deliverysupply()
    #             update_record.delivery_supply_description = getdata2
    #             update_record.delivery_supply_unit = supplymainstorage.objects.get(supplymainstorage_id= getdata1).supplymainstorage_unit
    #             getdata3 = supplymainstorage.objects.get(supplymainstorage_id=pk).supplymainstorage_id
    #             getdata4 = supplymainstorage.objects.get(supplymainstorage_id= getdata3)
    #             adding = int(getdata4.supplymainstorage_quantity) + int(request.POST.get('supplymainstorage_RequestQuantity'))
    #             update_record.delivery_supply_quantity = request.POST.get('supplymainstorage_RequestQuantity')
    #             update_record.delivery_supply_remaining = adding
    #             update_record.save()

    #             update_delivery = supplymainstorage()
    #             update_delivery.supplymainstorage_id = getdata1
    #             update_delivery.supplymainstorage_description = getdata2
    #             update_delivery.supplymainstorage_unit = supplymainstorage.objects.get(supplymainstorage_id= getdata1).supplymainstorage_unit
    #             getdata5 = supplymainstorage.objects.get(supplymainstorage_id=pk).supplymainstorage_id
    #             getdata6 = supplymainstorage.objects.get(supplymainstorage_id= getdata5)
    #             adding1 = int(getdata6.supplymainstorage_quantity) + int(request.POST.get('supplymainstorage_RequestQuantity'))
    #             update_delivery.supplymainstorage_quantity = adding1
    #             getdata7 = supplymainstorage.objects.get(supplymainstorage_id=pk).supplymainstorage_id
    #             getdata8 = supplymainstorage.objects.get(supplymainstorage_id= getdata7)
    #             supplymainstorage.objects.filter(supplymainstorage_description = getdata8.supplymainstorage_description).filter(supplymainstorage_unit = getdata8.supplymainstorage_unit).delete()
    #             update_delivery.save()
    #             getdata9 = supplymainstorage.objects.get(supplymainstorage_id=pk).supplymainstorage_id
    #             getdata10 = supplymainstorage.objects.get(supplymainstorage_id= getdata9).supplymainstorage_description

    #             messages.success(request, 'Record updated for: ' + getdata10)
    #             return redirect('inventorysystem-suppliesDeliver')

    #     else:
    #         messages.info(request, "invalid quantity")

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
        update_limit_department = request.POST.get('limit_department')
        update_limit_description = request.POST.get('limit_description')
        update_limit_unit = request.POST.get('limit_unit')
        update_limit_quantity = request.POST.get('limit_quantity')
        update_limit_addquantity = request.POST.get('limit_addquantity')

        if 'new_limit' in request.POST:

            if supplymainstorage.objects.filter(supplymainstorage_description = description).filter(supplymainstorage_unit = unit).exists() == True:
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

def updateStatus(request, pk):
    data = limitrecords.objects.get(limit_id=pk)
    form = statusForm(request.POST or None, instance=data)
    # if request.method == 'POST':
        # getdata2 = limitrecords.objects.get(limit_id=pk).limit_id
        # getdata3 = limitrecords.objects.get(limit_id = getdata2)
        # if int(request.POST.get('limit_addquantity')) > 0:
        #     update_record = limitrecords()
        #     update_record.limit_id = getdata2
        #     update_record.limit_description = getdata3.limit_description
        #     update_record.limit_unit = getdata3.limit_unit
        #     update_record.limit_department = getdata3.limit_department
        #     getdata = limitrecords.objects.get(limit_id=pk).limit_id
        #     getdata1 = limitrecords.objects.get(limit_id=getdata)
        #     adding = int(getdata1.limit_quantity) + int(request.POST.get('limit_addquantity'))
        #     update_record.limit_quantity = adding
        #     getdatalimit = limitrecords.objects.get(limit_id=pk).limit_id
        #     limitrecords.objects.filter(limit_id = getdatalimit).delete()
        #     update_record.save()
        #     getdata4 = limitrecords.objects.get(limit_id=pk).limit_id
        #     getdata5 = limitrecords.objects.get(limit_id = getdata4).limit_description
        #     getdata6 = limitrecords.objects.get(limit_id = getdata4).limit_unit
        #     getdata7 = limitrecords.objects.get(limit_id = getdata4).limit_department

        #     messages.success(request, 'Record updated for Itemname: ' + getdata5 +  " with a unit: " + getdata6 + " into department: " + getdata7)
        #     return redirect('inventorysystem-statusLimit')
        # else:
        #     messages.info(request, "invalid quantity")

    context = {
            'data': data,
            'form': form,
        }

    return render(request, 'task/update-status.html', context)


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

        if int(supplymainstorage.objects.get(supplymainstorage_description = getdata2.request_supply_description).supplymainstorage_quantity) > int(getdata2.request_supply_quantity):
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
            number = str(supplymainstorage.objects.get(supplymainstorage_description = getdata1.request_supply_description).supplymainstorage_quantity)
            messages.info(request, 'This item does not have enough stock in the main storage,'+ ' Mainstorage Remaining: ' + number)
    context = {
        'info': info,
        # 'info1': info1,

    }
    return render(request, 'task/view-request-supplies.html', context)

def editRequestSupply(request, pk):
    data = requestsupply.objects.get(requestsupply_id=pk)
    form = requestSupplyForm(request.POST or None, instance=data)
    # if request.method == 'POST':
    #     getdata = requestsupply.objects.get(requestsupply_id=pk).requestsupply_id
    #     getdata1 = requestsupply.objects.get(requestsupply_id = getdata)
    #     if int(supplymainstorage.objects.get(supplymainstorage_description = getdata1.request_supply_description).supplymainstorage_quantity) > int(getdata1.request_supply_quantity):
    #         accept = acceptSupplyRequests()
    #         accept.acceptSupplyRequests_id = getdata
    #         accept.arequest_supply_department = getdata1.request_supply_department
    #         accept.arequest_supply_description = getdata1.request_supply_description
    #         accept.arequest_supply_unit = getdata1.request_supply_unit
    #         accept.arequest_supply_quantity = getdata1.request_supply_quantity
    #         accept.arequest_supply_remaining = supplymainstorage.objects.get(supplymainstorage_description = getdata1.request_supply_description).supplymainstorage_quantity
    #         accept.arequest_supply_status = "Ready for pick-up"
    #         data1 = requestsupply.objects.get(requestsupply_id=pk).requestsupply_id
    #         # subject = "Supply Department"
    #         # message = "Your Item is ready for pick up"
    #         # get1 = requestsupply.objects.get(requestsupply_id=pk).requestsupply_id
    #         # get2 = str(requestsupply.objects.get(requestsupply_id = getdata).request_supply_department)
    #         # depinfo = str(requestsupply.objects.get(requestsupply_id = getdata1).request_supply_department)
    #         # print(depinfo)
    #         # recipient = str(CustomUser.objects.get(department= get2).email)
    #         # # email field ng bawat department
    #         # send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
    #         requestsupply.objects.filter(requestsupply_id = data1).delete()       
    #         status = statusSupplyRequest()
    #         status.statusSupplyRequests_id = getdata
    #         status.status_supply_description = getdata1.request_supply_description
    #         status.status_supply_unit = getdata1.request_supply_unit
    #         status.status_supply_quantity = getdata1.request_supply_quantity
    #         status.status_supply_remaining = limitrecords.objects.get(limit_id = getdata).limit_quantity
    #         status.status_supply_department = getdata1.request_supply_department
    #         status.status_supply_status = "Ready for pick-up"  
    #         statusSupplyRequest.objects.filter(statusSupplyRequests_id = getdata).delete()  
    #         messages.success(request, 'request accepted')
    #         accept.save()
    #         status.save()
          

    #         return redirect('inventorysystem-viewRequestSupply')
    #     else:
    #         number = str(supplymainstorage.objects.get(supplymainstorage_description = getdata1.request_supply_description).supplymainstorage_quantity)
    #         messages.info(request, 'This item does not have enough stock in the main storage,'+ ' Mainstorage Remaining: ' + number)

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
    if request.method == 'POST':
        request_description = request.POST.get('request_description')
        request_unit = request.POST.get('request_unit')
        request_quantity = request.POST.get('request_quantity')
        request_addquantity = request.POST.get('request_addquantity')
        requestingitem = limitrecords.objects.get(limit_description = request_description)
        requestingID = limitrecords.objects.get(limit_description = request_description).limit_id
        if statusSupplyRequest.objects.filter(status_supply_description = requestingitem).filter(status_supply_department = request.user).exists() == True:
                messages.info(request, 'You already have a request for this item.')
                return redirect('inventorysystem-depRequestSupply')

        elif int(request_addquantity) == 0:
                messages.info(request, 'Not enough quantity for this item.')
                return redirect('inventorysystem-depRequestSupply')

        elif int(request_addquantity) <= 0:
                messages.info(request, 'Check the available quantity')
                return redirect('inventorysystem-depRequestSupply')

        elif statusSupplyRequest.objects.filter(statusSupplyRequests_id = requestingID).exists() == False:
    
                if limitrecords.objects.filter(limit_id = requestingID).exists() == True:
                    getdata3 = limitrecords.objects.get(limit_id = requestingID)
                    requesting = requestsupply()
                    requesting.requestsupply_id = requestingID
                    requesting.request_supply_description = request_description
                    requesting.request_supply_unit = request_unit
                    requesting.request_supply_quantity = request_addquantity
                    requesting.request_supply_remaining = request_quantity
                    requesting.request_supply_department = getdata3.limit_department
                    requesting.request_supply_status = "pending"
                    status = statusSupplyRequest()
                    status.statusSupplyRequests_id = requestingID
                    status.status_supply_description = request_description
                    status.status_supply_unit = request_unit
                    status.status_supply_quantity = request_addquantity
                    status.status_supply_remaining = request_quantity
                    status.status_supply_department = getdata3.limit_department
                    status.status_supply_status = "pending"
                    requesting.save()
                    status.save()
                    getdata4 = limitrecords.objects.get(limit_id = requestingID).limit_description

                    messages.success(request, 'Request Successful for itemname ' + getdata4)
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

def editdepRequestSupply(request, pk):
    info1 = limitrecords.objects.get(limit_id=pk)
    form = depRequestSupplyForm(request.POST or None, instance=info1)
    # if request.method == 'POST':
    #     requestingID = limitrecords.objects.get(limit_id=pk).limit_id
    #     requestingitem = limitrecords.objects.get(limit_id= requestingID).limit_description
    #     if statusSupplyRequest.objects.filter(status_supply_description = requestingitem).filter(status_supply_department = request.user).exists() == True:
    #             messages.info(request, 'You already have a request for this item.')
    #             return redirect('inventorysystem-depRequestSupply')

    #     elif int(request.POST.get('limit_quantity')) == 0:
    #             messages.info(request, 'Not enough quantity for this item.')
    #             return redirect('inventorysystem-depRequestSupply')

    #     elif int(request.POST.get('limit_addquantity')) <= 0:
    #             messages.info(request, 'Check the available quantity')
    #             return redirect('inventorysystem-depRequestSupply')

    #     elif statusSupplyRequest.objects.filter(statusSupplyRequests_id = requestingID).exists() == False:
    #             requestID = limitrecords.objects.get(limit_id=pk).limit_id

    #             requestqty = request.POST.get('limit_addquantity')
    #             if limitrecords.objects.filter(limit_id = requestID).exists() == True:
    #                 getdata3 = limitrecords.objects.get(limit_id = requestID)
    #                 requesting = requestsupply()
    #                 requesting.requestsupply_id = requestID
    #                 requesting.request_supply_description = getdata3.limit_description
    #                 requesting.request_supply_unit = getdata3.limit_unit
    #                 requesting.request_supply_quantity = requestqty
    #                 requesting.request_supply_remaining = getdata3.limit_quantity
    #                 requesting.request_supply_department = getdata3.limit_department
    #                 requesting.request_supply_status = "pending"
    #                 status = statusSupplyRequest()
    #                 status.statusSupplyRequests_id = requestID
    #                 status.status_supply_description = getdata3.limit_description
    #                 status.status_supply_unit = getdata3.limit_unit
    #                 status.status_supply_quantity = requestqty
    #                 status.status_supply_remaining = getdata3.limit_quantity
    #                 status.status_supply_department = getdata3.limit_department
    #                 status.status_supply_status = "pending"
    #                 requesting.save()
    #                 status.save()
    #                 getdata4 = limitrecords.objects.get(limit_id = requestID).limit_description

    #                 messages.success(request, 'Request Successful for itemname ' + getdata4)
    #                 subject = str(limitrecords.objects.get(limit_id = requestID).limit_department)
    #                 message = "New Request"
    #                 depinfo = str(CustomUser.objects.get(is_superuser=True).email)
    #                 # limitrecords.objects.get(limit_id = requestID).limit_department
    #                 # str(CustomUser.objects.get(department= depinfo).email)
    #                 print(depinfo)
    #                 recipient = depinfo
    #                 # email ni sir gascon 
    #                 send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
    #                 return redirect('inventorysystem-depRequestSupply')


    context = {
        'info1': info1,
        'form': form,
    }
    return render(request, 'task/edit-dep-request-supply.html', context)

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
        update_limit.limit_id = getdata1
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


def updateSupplyWithdraw(request, pk):
    data = acceptSupplyRequests.objects.get(acceptSupplyRequests_id=pk)
    form = withdrawStatusForm(request.POST or None, instance=data)
    # if request.method == 'POST':
    #     getdata4 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id=pk).acceptSupplyRequests_id
    #     getdata5 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id = getdata4)

    #     update_storage = supplymainstorage()
    #     getdata = supplymainstorage.objects.get(supplymainstorage_description = getdata5.arequest_supply_description)
    #     update_storage.supplymainstorage_description = getdata5.arequest_supply_description
    #     update_storage.supplymainstorage_unit = getdata5.arequest_supply_unit
    #     update_storage.supplymainstorage_id = getdata.supplymainstorage_id
    #     update_storage.supplymainstorage_quantity = int(getdata.supplymainstorage_quantity) - int(getdata5.arequest_supply_quantity)
    #     getdata6 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id=pk).acceptSupplyRequests_id
    #     getdata7 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id = getdata6).arequest_supply_description
    #     supplymainstorage.objects.filter(supplymainstorage_description = getdata7).delete()
    #     update_storage.save()

    #     update_limit = limitrecords()
    #     getdata3 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id=pk).acceptSupplyRequests_id
    #     update_limit.limit_id = getdata3
    #     update_limit.limit_description = getdata5.arequest_supply_description
    #     update_limit.limit_unit = getdata5.arequest_supply_unit
    #     update_limit.limit_department = getdata5.arequest_supply_department
    #     getdata1 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id=pk).acceptSupplyRequests_id
    #     limitqty = limitrecords.objects.get(limit_id = getdata1).limit_quantity      
    #     update_limit.limit_quantity = int(limitqty) - int(getdata5.arequest_supply_quantity)
    #     getdata8 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id=pk).acceptSupplyRequests_id
    #     getdata9 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id = getdata8).arequest_supply_description
    #     getdata10 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id = getdata8).arequest_supply_description
    #     limitrecords.objects.filter(limit_description = getdata9).filter(limit_department = getdata10).delete()
    #     update_limit.save()

    #     accept = withdrawsupply()
    #     accept.withdraw_supply_department = getdata5.arequest_supply_department
    #     accept.withdraw_supply_description = getdata5.arequest_supply_description
    #     accept.withdraw_supply_unit = getdata5.arequest_supply_unit
    #     accept.withdraw_supply_quantity = getdata5.arequest_supply_quantity
    #     accept.withdraw_supply_remaining = supplymainstorage.objects.get(supplymainstorage_description = getdata5.arequest_supply_description).supplymainstorage_quantity
    #     data1 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id=pk).acceptSupplyRequests_id
    #     acceptSupplyRequests.objects.filter(acceptSupplyRequests_id = data1).delete()
    #     statusSupplyRequest.objects.filter(statusSupplyRequests_id = getdata1).delete()         
    #     accept.save()

    #     messages.success(request, 'successfully withdraw')
    #     return redirect('inventorysystem-suppliesWithdraw')

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
        update_itemname = request.POST.get('equipmentmainstorage_itemName')
        update_description = request.POST.get('equipmentmainstorage_description')
        update_brand = request.POST.get('equipmentmainstorage_brand')
        update_quantity = request.POST.get('equipmentmainstorage_RequestQuantity')

    
        if 'delivery_equipment_new' in request.POST:

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

    context = {
        'form': form,
        'info': info,
        'info1': info1,

    }
    return render(request, 'task/equipment-delivery.html', context)


def updateEquipmentDeliver(request, pk):
    data = equipmentmainstorage.objects.get(equipmentmainstorage_id=pk)
    form = updateEquipmentSupplyForm(request.POST or None, instance=data)
    # if request.method == 'POST':
    #     if int(request.POST.get('equipmentmainstorage_RequestQuantity')) > 0:
    #         itemname = request.POST.get('equipmentmainstorage_itemName')
    #         update_record = deliveryequipment()
    #         update_record.delivery_equipment_itemname = request.POST.get('equipmentmainstorage_itemName')
    #         update_record.delivery_equipment_brand = request.POST.get('equipmentmainstorage_brand')
    #         update_record.delivery_equipment_description = request.POST.get('equipmentmainstorage_description')
    #         getdata = equipmentmainstorage.objects.get(equipmentmainstorage_itemName = itemname)
    #         adding = int(getdata.equipmentmainstorage_quantity) + int(request.POST.get('equipmentmainstorage_RequestQuantity'))
    #         update_record.delivery_equipment_remaining = adding
    #         update_record.delivery_equipment_quantity = request.POST.get('equipmentmainstorage_RequestQuantity')
    #         update_record.save()
    #         update_delivery = equipmentmainstorage()
    #         update_delivery.equipmentmainstorage_id = equipmentmainstorage.objects.get(equipmentmainstorage_itemName = itemname).equipmentmainstorage_id
    #         update_delivery.equipmentmainstorage_itemName = request.POST.get('equipmentmainstorage_itemName')
    #         update_delivery.equipmentmainstorage_brand = request.POST.get('equipmentmainstorage_brand')
    #         update_delivery.equipmentmainstorage_description = request.POST.get('equipmentmainstorage_description')
    #         getdata = equipmentmainstorage.objects.get(equipmentmainstorage_itemName = itemname)
    #         adding = int(getdata.equipmentmainstorage_quantity) + int(request.POST.get('equipmentmainstorage_RequestQuantity'))
    #         update_delivery.equipmentmainstorage_remaining = 0
    #         update_delivery.equipmentmainstorage_quantity = adding
    #         equipmentmainstorage.objects.filter(equipmentmainstorage_itemName = itemname).delete()
    #         update_delivery.save()


    #         messages.success(request, 'Record updated for: ' + itemname)
    #         return redirect('inventorysystem-equipmentDeliver')
    #     else:
    #         messages.info(request, "invalid quantity")

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
        accept.arequest_equipment_issued_to = getdata1.request_equipment_department
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
            if equipmentmainstorage.objects.filter(equipmentmainstorage_itemName = request.POST.get('non-existing_equipment_itemname')).exists == False:
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
                
            elif equipmentmainstorage.objects.filter(equipmentmainstorage_itemName = request.POST.get('non-existing_equipment_itemname')).exists == True:
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
        requestqty = request.POST.get('equipmentmainstorage_RequestQuantity')
        requestingID1 = equipmentmainstorage.objects.get(equipmentmainstorage_id=pk).equipmentmainstorage_id
        requestingitem1 = equipmentmainstorage.objects.get(equipmentmainstorage_id= requestingID1).equipmentmainstorage_itemName
        if statusEquipmentRequest.objects.filter(status_equipment_itemname =  requestingitem1).exists() == True:
                messages.info(request, 'You already have a request for this equipment.')
                return redirect('inventorysystem-depRequestEquipment')

        elif int(request.POST.get('equipmentmainstorage_quantity')) == 0:
                messages.info(request, 'Not enough quantity for this equipment.')
                return redirect('inventorysystem-depRequestEquipment')

        elif int(request.POST.get('equipmentmainstorage_RequestQuantity')) <= 0:
                messages.info(request, 'Check the available quantity')
                return redirect('inventorysystem-depRequestEquipment')

        elif equipmentmainstorage.objects.filter(equipmentmainstorage_id = requestID).exists() == True:
            getdata3 = equipmentmainstorage.objects.get(equipmentmainstorage_id = requestID)
            requesting = requestequipment()
            requesting.requestequipment_id = requestID
            requesting.request_equipment_itemname = getdata3.equipmentmainstorage_itemName
            requesting.request_equipment_description = getdata3.equipmentmainstorage_description
            requesting.request_equipment_brand = getdata3.equipmentmainstorage_brand
            requesting.request_equipment_quantity = requestqty
            requesting.request_equipment_department = str(request.user)
            requesting.request_equipment_status = "pending"
            status = statusEquipmentRequest()
            status.statusEquipmentRequests_id = requestID
            status.status_equipment_itemname = getdata3.equipmentmainstorage_itemName
            status.status_equipment_description = getdata3.equipmentmainstorage_description
            status.status_equipment_brand = getdata3.equipmentmainstorage_brand
            status.status_equipment_quantity = requestqty
            status.status_equipment_remaining = getdata3.equipmentmainstorage_quantity
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

    context = {
        'info': info,
        'info1': info1
    }

    return render(request, 'task/storage-mapping.html', context)

def updateSupplyStorage(request, pk):
    data = supply_storagemapping.objects.get(supplyStoragemapping_id=pk)
    form = supply_storageForm(request.POST or None, instance=data)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('inventorysystem-storageMapping')
    context = {
        'data': data,
        'form': form,
    }

    return render(request, 'task/update-supply-storage.html', context)

def updateEquipmentStorage(request, pk):
    data = equipment_storagemapping.objects.get(equipmentStoragemapping_id=pk)
    form = equipment_storageForm(request.POST or None, instance=data)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('inventorysystem-storageMapping')
    context = {
        'data': data,
        'form': form,
    }

    return render(request, 'task/update-equipment-storage.html', context)


#------------------- EXPORT EXCEL FILE -----------------------------
def export_excel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Supply Inventory' + '.xls'
    wb =xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Supply Delivery')
    ws1 = wb.add_sheet('Equipment Delivery')
    row_num = 0
    row_num1 = 0
    supply_font = xlwt.XFStyle()
    equipment_font = xlwt.XFStyle()
    

#supply delivery
    supply_font.font.bold = True
    supplydelivery = ['Description', 'Unit', 'Quantity', 'Remaining Quantity', 'Date']

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
                'Quantity', 'Remaining Quantity', 'Date']

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

    wb.save(response)
    return response
