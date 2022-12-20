from .forms import *
from .models import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
import datetime
import xlwt
import os

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings

from django.template.loader import render_to_string
from weasyprint import HTML , CSS 
import tempfile

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def depWithdrawnItems(request):
    info2 = withdrawsupply.objects.all().filter(withdraw_supply_department = request.user)
    info = withdrawequipment.objects.all().filter(withdraw_equipment_issued_to = request.user)

    context = {
        'info2': info2,
        'info': info,
        }
    return render(request, 'task/dep-withdrawn-items.html', context)  

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def suppliesCreateform(request):
    form = supplycreateforminputsForm()
    label = request.user
    if request.method == "POST":
        if 'save_details' in request.POST:
            if supply_createform_inputs.objects.filter(createformsupply_inputs_department = request.user).filter(current_date = request.POST.get('date')).exists() == False:
                form = supply_createform_inputs()
                form.createformsupply_inputs_office = request.POST.get('createformsupply_inputs_office')
                form.createformsupply_inputs_requestedby = request.POST.get('createformsupply_inputs_requestedby')
                form.createformsupply_inputs_purpose = request.POST.get('createformsupply_inputs_purpose')
                form.createformsupply_inputs_approvedby = "MYRNA M. TEPORA"
                form.createformsupply_inputs_receivedby = request.POST.get('createformsupply_inputs_receivedby')
                form.createformsupply_inputs_issuedby = "B.F. GASCON"
                form.createformsupply_inputs_department = request.user
                form.current_date = request.POST.get('date')
                form.save()
                messages.success(request, 'Ready for creating a form!')
                
                return redirect('inventorysystem-suppliesCreateform')
            elif supply_createform_inputs.objects.filter(createformsupply_inputs_department = request.user).filter(current_date = request.POST.get('date')).exists() == False:
                messages.info(request, 'You already have saved details for this form')
                return redirect('inventorysystem-suppliesCreateform')

        if 'read_form' in request.POST:
            if supply_createform.objects.filter(current_date = request.POST.get('date')).exists() == False:
                messages.info(request, 'You do not have available for request for this date.')
                return redirect('inventorysystem-suppliesCreateform')

    context = {
        'form': form,
        'label': label,
        }
    return render(request, 'task/supply-createform-inputs.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def equipmentIcsform(request):
    form = equipment_icsform_inputsForm()
    if request.method == "POST":
        if 'save_inputs' in request.POST:
            form =  equipment_icsform_inputs()
            form.icsform_inputs_icsno = request.POST.get('icsform_inputs_icsno')
            form.icsform_inputs_invoiceno = request.POST.get('icsform_inputs_invoiceno')
            form.icsform_inputs_pono = request.POST.get('icsform_inputs_pono')
            form.icsform_inputs_receivedby = request.POST.get('icsform_inputs_receivedby')
            form.icsform_inputs_receivedfrom = request.POST.get('icsform_inputs_receivedfrom')
            form.icsform_inputs_suppliedby = request.POST.get('icsform_inputs_suppliedby')
            form.save()
            messages.success(request, 'Ready for creating a form!')
            return redirect('inventorysystem-equipment-icsform')
    context = {
        'form': form,
        }
    return render(request, 'task/equipment-icsform-inputs.html', context) 

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def equipmentAreform(request):
    form = equipment_areform_inputsForm()
    if request.method == "POST":
        if 'save_inputs' in request.POST:
            form = equipment_areform_inputs()
            form.areform_inputs_no = request.POST.get('areform_inputs_no')
            form.areform_inputs_invoiceno = request.POST.get('areform_inputs_invoiceno')
            form.areform_inputs_pono = request.POST.get('areform_inputs_pono')
            form.areform_inputs_receivedby = request.POST.get('areform_inputs_receivedby')
            form.areform_inputs_receivedfrom = request.POST.get('areform_inputs_receivedfrom')
            form.areform_inputs_suppliedby = request.POST.get('areform_inputs_suppliedby')
            form.areform_inputs_totalamount = request.POST.get('areform_inputs_totalamount')
            form.save()
            messages.success(request, 'Ready for creating a form!')
            return redirect('inventorysystem-equipment-areform')

    context = {
        'form': form,
        }
    return render(request, 'task/equipment-areform-inputs.html', context) 

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def index(request):
    return render(request, 'task/index.html')  

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def dashboard(request):
    if (request.user.is_authenticated and request.user.is_superuser) or \
        (request.user.is_authenticated and request.user.is_admin):
        
        label = request.user
        label1 = int(requestsupply.objects.all().count())
        label2 = int(withdrawsupply.objects.all().count())
        label3 = int(requestequipment.objects.all().count())
        label4 = int(withdrawequipment.objects.all().count())

        context = {
            'label': label,
            'label1': label1,
            'label2': label2,
            'label3': label3,
            'label4': label4,


        }
        return render(request, 'task/dashboard.html', context) 
    else:
        return redirect('inventorysystem-usersLogin')


def logoutUser(request):
    logout(request)

    return redirect('inventorysystem-usersLogin')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = CustomUser.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "task/password_message.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'TUPC Supply Inventory System',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, '' , [user.email], fail_silently=False)
					except BadHeaderError:

						return HttpResponse('Invalid header found.')
						
					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="task/password_reset.html", context={"password_reset_form":password_reset_form})
    

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES['file']
        form2 = department_form.objects.create(dep_form = file)
        form2.save()
        return HttpResponse(str(form2.pk) + str(form2.dep_form))
    else:
        form = UploadFileForm()
    return render (request, 'task/upload.html', {'form': form})

def table(request):
    context = {'files': department_form.objects.all()}
    return render(request,'task/table.html', context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response = HttpResponse(fh.read(), content_type='application/dep_form')
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    else:
        print('error')


#--------- LOGIN --------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def usersLogin(request):
    if (request.user.is_authenticated and request.user.is_superuser) or \
        (request.user.is_authenticated and request.user.is_admin):
        return redirect('inventorysystem-dashboard')
    elif request.user.is_authenticated and request.user.is_department:
        return redirect('inventorysystem-depRequestSupply')
    else:
        if request.method == "POST":
            username1 = request.POST.get('logname')
            password1 = request.POST.get('logpass1')

            username2 = request.POST.get('logusername')
            # email2 = request.POST.get('email2')
            password2 = request.POST.get('logpass2')

            user1 = authenticate(request, username=username1, password=password1)
            user2 = authenticate(request, username=username2, password=password2)

            if (user1 is not None and user1.is_superuser) or \
            (user1 is not None and user1.is_admin):
                login(request, user1)
                messages.success(request, 'Hello ' + username1 + '!')
                return redirect('inventorysystem-dashboard')
            else:
                messages.info(request, 'Invalid credentials. Please try again.') 

            if user2 is not None and user2.is_department:
                login(request, user2)
                messages.success(request, 'Hello ' + username2 + '!')
                return redirect('inventorysystem-depRequestSupply')
            else:
                messages.info(request, 'Invalid credentials. Please try again.')  

        return render(request, 'task/usersLogin.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def deptRegister(request):
    if (request.user.is_authenticated and request.user.is_superuser) or \
        (request.user.is_authenticated and request.user.is_admin):
        
        label = request.user
        form = DeptRegisterForm()

        if request.method == "POST":
            form = DeptRegisterForm(request.POST)
            if form.is_valid():
                role = request.POST.get('deptRole')
                dept = request.POST.get('department')
                email = request.POST.get('email')

                if dept == '':
                    messages.info(request, 'Please add a department office.')

                elif CustomUser.objects.filter(department = dept).exists() == True:
                    messages.info(request, 'There is already an existing account for ' + dept)

                elif role == 'department':
                    form.instance.is_department = True

                    form.save()
                    messages.success(request, 'Account was created for ' + dept)
                    subject = 'Account Registration'
                    message = "Good day! \nYour account has been successfully registered " + dept + "! \nYou can now access your account by logging in to the website. Thank you!" 
                    recipient = email 
                    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
                    return redirect('inventorysystem-deptRegister')
            else:
                messages.warning(request, form.errors)

        context = {
            'form': form,
            'label': label,
        }

        return render(request, 'task/department-register.html', context)
    else:
        return redirect('inventorysystem-usersLogin')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def adminRegister(request):
    if (request.user.is_authenticated and request.user.is_superuser) or \
        (request.user.is_authenticated and request.user.is_admin):
        
        label = request.user
        form = AdminRegisterForm()
        if request.method == "POST":
            form = DeptRegisterForm(request.POST)
            if form.is_valid():
                getRole = request.POST.get('adminRole')
                username = request.POST.get('username') 
                email = request.POST.get('email') 

                if getRole == 'admin':
                    form.instance.is_admin = True
                    form.instance.is_staff = True
    
                    form.save()
                    messages.success(request, 'Account was created for ' + username)
                    subject = 'Account Registration'
                    message = "Good day! \nYour account has been successfully registered " + username + "! \nYou can now access your account by logging in to the website. Thank you!" 
                    recipient = email 
                    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
                    return redirect('inventorysystem-adminRegister')
            else:
                messages.warning(request, form.errors)

        context = {
            'form': form,
            'label': label,
        }

        return render(request, 'task/admin-register.html', context)
    else:
        return redirect('inventorysystem-usersLogin')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def adminProfileUpdate(request):
    if (request.user.is_authenticated and request.user.is_superuser) or \
        (request.user.is_authenticated and request.user.is_admin):
        
        label = request.user
        if request.method == 'POST':
            user_form = AdminUpdateForm(request.POST, instance=request.user)
            email = request.POST.get('email')
            username = request.POST.get('username')
            # profile_form = AdminUpdateForm(request.POST, request.FILES, instance=request.user.profile)

            if user_form.is_valid():
                if CustomUser.objects.filter(username = username).filter(email = email).exists() == False:
                    user_form.save()
                    # profile_form.save()
                    messages.success(request, 'Your profile is successfully updated.')
                    subject = 'Update Profile'
                    message = "Good day "+ username + "! \nYour account has been successfully updated! \nYou can now access your account by logging in to the website. Thank you!" 
                    recipient = email 
                    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
                    return redirect(to='inventorysystem-adminProfileUpdate')
                
                else:
                    messages.info(request, 'Existing record. Please try again.')
                    return redirect(to='inventorysystem-adminProfileUpdate')
        else:
            user_form = AdminUpdateForm(instance=request.user)
            # profile_form = AdminUpdateForm(instance=request.user.adminProfileUpdate)

        context = {
            'user_form': user_form,
            'label': label,
        }

        return render(request, 'task/updateAdminProfile.html', context)
    else:
        return redirect('inventorysystem-usersLogin')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def deptProfileUpdate(request):
    if (request.user.is_authenticated and request.user.is_department):
        
        label = request.user
        if request.method == 'POST':
            user_form = DeptUpdateForm(request.POST, instance=request.user)
            email = request.POST.get('email')
            username = request.POST.get('username')
            # profile_form = DeptUpdateForm(request.POST, request.FILES, instance=request.user.profile)

            if user_form.is_valid():
                # if username is not None and email is not None == username and email:
                #     messages.info(request, 'No changes submitted.')
                
                if CustomUser.objects.filter(username = username).filter(email = email).exists() == False:
                    user_form.save()
                    # profile_form.save()
                    messages.success(request, 'Your profile is successfully updated.')
                    subject = 'Update Profile'
                    message = "Good day "+ username + "! \nYour account has been successfully updated! \nYou can now access your account by logging in to the website. Thank you!" 
                    recipient = email 
                    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
                    return redirect(to='inventorysystem-adminProfileUpdate')
                
                else:
                    messages.info(request, 'Existing record. Please try again.')
                    return redirect(to='inventorysystem-adminProfileUpdate')
        else:
            user_form = DeptUpdateForm(instance=request.user)
            # profile_form = DeptUpdateForm(instance=request.user.adminProfileUpdate)

        context = {
            'user_form': user_form,
            'label': label,
        }
        return render(request, 'task/updateDeptProfile.html', context)
    else:
        return redirect('inventorysystem-usersLogin')



#------------------- DELIVERY SUPPLIES -----------------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def suppliesDeliver(request):
    if (request.user.is_authenticated and request.user.is_superuser) or \
        (request.user.is_authenticated and request.user.is_admin):
        
        label = request.user
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
            rackno = request.POST.get('delivery_supplyRackNo')
            layerno = request.POST.get('delivery_supplyLayerNo')
            cabinetno = request.POST.get('delivery_supplyCabinetNo')
            shelfno = request.POST.get('delivery_supplyShelfNo')

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
                            storageupdate.supplymainstorage_supplyRackNo = rackno
                            storageupdate.supplymainstorage_supplyLayerNo = layerno
                            storageupdate.supplymainstorage_supplyCabinetNo = cabinetno
                            storageupdate.supplymainstorage_supplyShelfNo = shelfno
                            storageupdate.save()
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
                    update_delivery.supplymainstorage_supplyRackNo = supplymainstorage.objects.get(supplymainstorage_id = getdata1.supplymainstorage_id).supplymainstorage_supplyRackNo
                    update_delivery.supplymainstorage_supplyLayerNo = supplymainstorage.objects.get(supplymainstorage_id = getdata1.supplymainstorage_id).supplymainstorage_supplyLayerNo
                    update_delivery.supplymainstorage_supplyCabinetNo = supplymainstorage.objects.get(supplymainstorage_id = getdata1.supplymainstorage_id).supplymainstorage_supplyCabinetNo
                    update_delivery.supplymainstorage_supplyShelfNo = supplymainstorage.objects.get(supplymainstorage_id = getdata1.supplymainstorage_id).supplymainstorage_supplyShelfNo
                    supplymainstorage.objects.filter(supplymainstorage_description = update_description).filter(supplymainstorage_unit = update_unit).delete()
                    update_delivery.save()

                    messages.success(request, 'Record updated for: ' + str(getdata1.supplymainstorage_description))
                    return redirect('inventorysystem-suppliesDeliver')

            elif 'delivery_edit' in request.POST:
                if limitrecords.objects.filter(limit_description = supplymainstorage.objects.get(supplymainstorage_id = request.POST.get('supplymainstorage_editid')).supplymainstorage_description).exists() == False:

                    update_delivery1 = supplymainstorage()
                    update_delivery1.supplymainstorage_id = request.POST.get('supplymainstorage_editid')
                    update_delivery1.supplymainstorage_description = request.POST.get('supplymainstorage_editdescription')
                    update_delivery1.supplymainstorage_unit = request.POST.get('supplymainstorage_editunit')
                    update_delivery1.supplymainstorage_quantity = request.POST.get('mainstorage_editquantity')
                    supplymainstorage.objects.filter(supplymainstorage_description = request.POST.get('supplymainstorage_editdescription')).filter(supplymainstorage_unit = request.POST.get('supplymainstorage_editunit')).delete()
                    update_delivery1.save()
                    messages.success(request, 'Record for ' + request.POST.get('supplymainstorage_editdescription') + ' has been updated.')

                elif limitrecords.objects.filter(limit_description = supplymainstorage.objects.get(supplymainstorage_id = request.POST.get('supplymainstorage_editid')).supplymainstorage_description).exists() == True:
                    messages.info(request, "this item is existing in limit records")

            else:
                messages.info(request, "invalid quantity")

            

        
        context = {
            'form': form,
            'info': info,
            'info1': info1,
            'label': label,
        }

        return render(request, 'task/supplies-delivery.html', context)
    else:
        return redirect('inventorysystem-usersLogin')



#------------------- STATUS LIMIT SUPPLIES -----------------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def statusLimit(request):
    if (request.user.is_authenticated and request.user.is_superuser) or \
        (request.user.is_authenticated and request.user.is_admin):
        
        label = request.user
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
            'label': label,
        }
        return render(request, 'task/status-limit.html', context)
    else:
        return redirect('inventorysystem-usersLogin')



#------------------- ADMIN VIEW REQUEST SUPPLIES -----------------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def viewRequestSupply(request):
    if (request.user.is_authenticated and request.user.is_superuser) or \
        (request.user.is_authenticated and request.user.is_admin):

        label = request.user
        info = requestsupply.objects.all()
        info1 = supply_email.objects.all()
        info2 = supply_createform.objects.all()
        
        if request.method == 'POST':
            request_id = request.POST.get('requestsupply_id')
            request_department = request.POST.get('request_supply_department')
            request_unit = request.POST.get('request_supply_unit')
            request_description = request.POST.get('request_supply_description')
            request_quantity = request.POST.get('request_supply_quantity')
            request_accept_quantity = request.POST.get('request_supply_acceptquantity')
            request_amount = request.POST.get('supplyamount')
            request_requestby = request.POST.get('request_supply_requestedby')
            request_issuedby = request.POST.get('issuedby')


            if 'acceptbtn' in request.POST:
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
                    accept.arequest_supply_amount = request_amount
                    accept.arequest_supply_issued_by = request_issuedby
                    accept.arequest_supply_status = "Item Accepted"
                    accept.arequest_supply_dateaccepted = datetime.date.today()
                    accept.arequest_supply_LayerNo = request.POST.get('Supply_Layer')
                    accept.arequest_supply_RackNo = request.POST.get('Supply_Rack')
                    accept.arequest_supply_CabinetNo = request.POST.get('Supply_Cabinet')
                    accept.arequest_supply_ShelfNo = request.POST.get('Supply_Shelf')
                    requestsupply.objects.filter(requestsupply_id = getdata1).delete()       
                    status = statusSupplyRequest()
                    status.statusSupplyRequests_id = request_id
                    status.status_supply_description = request_description
                    status.status_supply_unit = request_unit
                    status.status_supply_quantity = request_quantity
                    status.status_supply_remaining = limitrecords.objects.get(limit_id = getdata1).limit_quantity
                    status.status_supply_acceptquantity = request_accept_quantity
                    status.status_supply_department = request_department
                    status.status_supply_status = "Item Accepted" 
                    statusSupplyRequest.objects.filter(status_supply_department = request_department).filter(status_supply_description = request_description).delete()  
                    messages.success(request, 'request accepted')
                    accept.save()
                    status.save()

                    form = supply_createform()
                    form.createformsupply_department = request_department
                    form.createformsupply_description = request_description
                    form.createformsupply_unit = request_unit
                    form.createformsupply_amount = request_amount
                    form.createformsupply_requestedby = request_requestby
                    form.createformsupply_issued_by = request_issuedby
                    form.current_date = datetime.date.today()
                    form.createformsupply_acceptedquantity = request_accept_quantity
                    form.save()

                    if supply_email.objects.filter(emailsupply_department = request_department).filter(current_date = datetime.date.today()).exists() == True:
                        emaildept = supply_email()
                        emaildept.emailsupply_id = supply_email.objects.get(emailsupply_department = request_department).emailsupply_id
                        emaildept.emailsupply_department = request_department
                        emailqty = supply_email.objects.get(emailsupply_department = request_department).emailsupply_acceptedquantity
                        emaildept.emailsupply_acceptedquantity = int(emailqty) + int(1)
                        emaildept.current_date = datetime.date.today()
                        supply_email.objects.filter(emailsupply_department = request_department).delete()
                        emaildept.save()

                    elif supply_email.objects.filter(emailsupply_department = request_department).filter(current_date = datetime.date.today()).exists() == False:
                        emaildept1 = supply_email()
                        emaildept1.emailsupply_department = request_department
                        emaildept1.emailsupply_acceptedquantity = 1
                        emaildept1.current_date = datetime.date.today()
                        emaildept1.save()

                    return redirect('inventorysystem-viewRequestSupply')


                else:
                    number = str(supplymainstorage.objects.get(supplymainstorage_description = getdata2.request_supply_description).supplymainstorage_quantity)
                    messages.info(request, 'This item does not have enough stock in the main storage,'+ ' Mainstorage Remaining: ' + number)


            elif 'emailBtn1' in request.POST:

                subject = "SUPPLY DEPARTMENT ADMIN"
                message = "Good day! \n\nYour request has been accepted. Please pick up the item/s as soon as possible. Thankyou. \n\nKind regards,\nSupply Admin"
                depinfo = str(CustomUser.objects.get(department=str(request.POST.get('email_supply_department'))).email)
                print(depinfo)
                recipient = depinfo
                send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
                supply_email.objects.filter(emailsupply_department = request.POST.get('email_supply_department')).filter(current_date = request.POST.get('email_supply_date')).delete()
                messages.success(request, 'successfully sent')

            # elif 'create_form' in request.POST:
            #     data = request.POST.get('department_createform')
            #     if supply_createform.objects.filter(createformsupply_department = data).exists() == True:
            #         data = request.POST.get('department_createform')
            #         response=HttpResponse(content_type='application/pdf')
            #         response['Content-Disposition'] = 'inline; attachment; filename=Supply Inventory' + \
            #             str(datetime.datetime.now())+'.pdf'
            #         supply = supply_createform.objects.all().filter(createformsupply_department = data)
            #         response['Content-Transfer-Enconding'] = 'binary'


            #         html_string = render_to_string('task/pdf-output-supplycreateform.html' ,{'Form': supply})
            #         html = HTML(string=html_string, base_url=request.build_absolute_uri())
            #         result = html.write_pdf(presentational_hints=True)

            #         with tempfile.NamedTemporaryFile(delete=False) as output:
            #             output.write(result)
            #             output.flush()
            #             output = open(output.name, 'rb')
            #             response.write(output.read())

                    
            #         return response
                # elif supply_createform.objects.filter(createformsupply_department = data).exists() == False:
                #         messages.info(request, 'Invalid department name')
                #         return redirect('inventorysystem-viewRequestSupply')  

        context = {
            'info': info,
            'label': label,
            'info1': info1,
            'info2': info2,

        }
        return render(request, 'task/view-request-supplies.html', context)
    else:
        return redirect('inventorysystem-usersLogin')


#------------------- DEPARTMENT REQUEST SUPPLIES -----------------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def depRequestSupply(request):
    if (request.user.is_authenticated and request.user.is_department):

        info1 = limitrecords.objects.all().filter(limit_department = request.user)
        info = statusSupplyRequest.objects.all().filter(status_supply_department = request.user)
        info3 = supply_createform.objects.all().filter(createformsupply_department = request.user)
        # info2 = withdrawsupply.objects.all().filter(withdraw_supply_department = request.user)

        if request.method == 'POST':

            request_id = request.POST.get('limit_id')
            request_description = request.POST.get('request_description')
            request_unit = request.POST.get('request_unit')
            request_quantity = request.POST.get('request_quantity')
            request_addquantity = request.POST.get('request_addquantity')
            request_requestedby = request.POST.get('requestedby')

            if 'create_form' in request.POST:
                # print(request.POST.get('datepicker'))
                if request.POST.get('datepicker') == '':
                    messages.info(request, 'Please type in a date.')

                elif supply_createform.objects.filter(createformsupply_department = request.user).filter(current_date = request.POST.get('datepicker')).exists() == True:
                    return redirect('inventorysystem-suppliesCreateform')

                elif supply_createform.objects.filter(createformsupply_department = request.user).filter(current_date = request.POST.get('datepicker')).exists() == False:
                    messages.info(request, 'Invalid.')
                    
                # if supply_createform.objects.filter(createformsupply_department = request.user).exists() == True:
                #     response=HttpResponse(content_type='application/pdf')
                #     response['Content-Disposition'] = 'inline; attachment; filename=Supply Inventory' + \
                #         str(datetime.datetime.now())+'.pdf'
                #     supply = supply_createform.objects.all().filter(createformsupply_department = request.user)
                #     response['Content-Transfer-Enconding'] = 'binary'


                #     html_string = render_to_string('task/pdf-output-supplycreateform.html' ,{'Form': supply})
                #     html = HTML(string=html_string, base_url=request.build_absolute_uri())
                #     result = html.write_pdf(presentational_hints=True)

                #     with tempfile.NamedTemporaryFile(delete=False) as output:
                #         output.write(result)
                #         output.flush()
                #         output = open(output.name, 'rb')
                #         response.write(output.read())

                #     return response

                # elif supply_createform.objects.filter(createformsupply_department = request.user).exists() == False:

                #     messages.info(request, 'No available items')
                #     return redirect('inventorysystem-depRequestSupply')
                    
            
            if 'request_update' in request.POST:

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
                    requesting = requestsupply()
                    requesting.requestsupply_id = request_id
                    requesting.request_supply_description = request_description
                    requesting.request_supply_unit = request_unit
                    requesting.request_supply_quantity = request_addquantity
                    requesting.request_supply_remaining = request_quantity
                    requesting.request_supply_department = str(request.user)
                    requesting.request_supply_supplyRackNo = supplymainstorage.objects.get(supplymainstorage_description = request_description).supplymainstorage_supplyRackNo
                    requesting.request_supply_supplyLayerNo = supplymainstorage.objects.get(supplymainstorage_description = request_description).supplymainstorage_supplyLayerNo
                    requesting.request_supply_supplyCabinetNo = supplymainstorage.objects.get(supplymainstorage_description = request_description).supplymainstorage_supplyCabinetNo
                    requesting.request_supply_supplyShelfNo = supplymainstorage.objects.get(supplymainstorage_description = request_description).supplymainstorage_supplyShelfNo
                    requesting.request_supply_status = "waiting to accept"
                    requesting.request_supply_daterequested = datetime.date.today()
                    status = statusSupplyRequest()
                    status.status_supply_description = request_description
                    status.status_supply_unit = request_unit
                    status.status_supply_quantity = request_addquantity
                    status.status_supply_remaining = request_quantity
                    status.status_supply_department = request.user
                    status.status_supply_status = "waiting to accept"
                    status.date_requested = datetime.date.today()
                    requesting.save()
                    status.save()

                    messages.success(request, 'Request Successful for itemname ')
                    subject = str(request.user)
                    message = "Good day!\n\nI have requested item in supply. Please see the details in the website. Thank you!\n\nKind regards,\n"+ str(request.user)
                    depinfo = str(CustomUser.objects.get(department=str(request.user)).email)
                    print(depinfo)
                    recipient = settings.EMAIL_HOST_USER
                    send_mail(subject, message, depinfo, [recipient], fail_silently=False)

                    return redirect('inventorysystem-depRequestSupply')



        context = {
            'info1': info1,
            'info': info,
            'info3': info3,
        }   
        return render(request, 'task/dep-request-supply.html', context)
    else:
        return redirect('inventorysystem-usersLogin')



#------------------- WITHDRAW SUPPLIES -----------------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def suppliesWithdraw(request):
    if (request.user.is_authenticated and request.user.is_superuser) or \
        (request.user.is_authenticated and request.user.is_admin):

        label = request.user
        info = acceptSupplyRequests.objects.all()
        info1 = withdrawsupply.objects.all()

        if request.method == 'POST':
            getdata = request.POST.get('acceptSupplyRequests_id')
            withdraw_department = request.POST.get('arequest_supply_department')
            withdraw_description = request.POST.get('arequest_supply_description')
            withdraw_unit = request.POST.get('arequest_supply_unit')
            withdraw_quantity = request.POST.get('arequest_supply_quantity')
            getdata1 = acceptSupplyRequests.objects.get(acceptSupplyRequests_id = getdata).acceptSupplyRequests_id

            if supply_email.objects.filter(emailsupply_department = withdraw_department).exists() == False:

                update_storage = supplymainstorage()
                getdata2 = supplymainstorage.objects.get(supplymainstorage_description = withdraw_description)
                update_storage.supplymainstorage_description = withdraw_description
                update_storage.supplymainstorage_unit = withdraw_unit
                update_storage.supplymainstorage_id = getdata2.supplymainstorage_id
                update_storage.supplymainstorage_quantity = int(getdata2.supplymainstorage_quantity) - int(withdraw_quantity)
                update_storage.supplymainstorage_supplyRackNo = supplymainstorage.objects.get(supplymainstorage_id = getdata2.supplymainstorage_id).supplymainstorage_supplyRackNo
                update_storage.supplymainstorage_supplyLayerNo = supplymainstorage.objects.get(supplymainstorage_id = getdata2.supplymainstorage_id).supplymainstorage_supplyLayerNo
                update_storage.supplymainstorage_supplyCabinetNo = supplymainstorage.objects.get(supplymainstorage_id = getdata2.supplymainstorage_id).supplymainstorage_supplyCabinetNo
                update_storage.supplymainstorage_supplyShelfNo = supplymainstorage.objects.get(supplymainstorage_id = getdata2.supplymainstorage_id).supplymainstorage_supplyShelfNo
                supplymainstorage.objects.filter(supplymainstorage_description = withdraw_description).delete()
                update_storage.save()

                update_limit = limitrecords()
                update_limit.limit_id = getdata
                update_limit.limit_description = withdraw_description
                update_limit.limit_unit = withdraw_unit
                update_limit.limit_department = withdraw_department
                limitqty = limitrecords.objects.get(limit_id = getdata1).limit_quantity      
                update_limit.limit_quantity = int(limitqty) - int(withdraw_quantity)
                update_limit.save()

                accept = withdrawsupply()
                accept.withdraw_supply_department = withdraw_department
                accept.withdraw_supply_description = withdraw_description
                accept.withdraw_supply_unit = withdraw_unit
                accept.withdraw_supply_quantity = withdraw_quantity
                accept.withdraw_supply_remaining = supplymainstorage.objects.get(supplymainstorage_description = withdraw_description).supplymainstorage_quantity
                acceptSupplyRequests.objects.filter(acceptSupplyRequests_id = getdata1).delete()
                statusSupplyRequest.objects.filter(status_supply_department = withdraw_department).filter(status_supply_description = withdraw_description).delete()    
                supply_createform.objects.all().filter(createformsupply_department = withdraw_department).delete() 
                supply_createform_inputs.objects.all().filter(createformsupply_inputs_department = withdraw_department).delete()
                accept.save()

                messages.success(request, 'successfully withdraw')
                return redirect('inventorysystem-suppliesWithdraw')

            elif supply_email.objects.filter(emailsupply_department = withdraw_department).filter(current_date = acceptSupplyRequests.objects.get(acceptSupplyRequests_id = getdata1).current_date).exists() == True:
                messages.info(request, 'please email the department first.')
                return redirect('inventorysystem-suppliesWithdraw')
        context = {
            'info': info,
            'info1': info1,
            'label': label,
        }
        return render(request, 'task/supplies-withdraw.html', context)
    else:
        return redirect('inventorysystem-usersLogin')


#------------------- DELIVERY EQUIPMENTS -----------------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def equipmentDeliver(request):
    if (request.user.is_authenticated and request.user.is_superuser) or \
        (request.user.is_authenticated and request.user.is_admin):

        label = request.user
        info = equipmentmainstorage.objects.all()
        info3 = equipmentmainstorage.objects.filter(equipmentmainstorage_quantity = 0).delete()
        info1 = deliveryequipment.objects.all()
        info2 = requestequipment.objects.all()
        info4 = equipment_email.objects.all()
        form = deliveryEquipmentForm()
        if request.method == 'POST':
            form = deliveryEquipmentForm(request.POST)

            if 'delivery_dep' in request.POST:

                request_id = request.POST.get('requestequipment_id')
                request_department = request.POST.get('request_equipment_department')
                request_itemname = request.POST.get('request_equipment_itemname')
                request_quantity = request.POST.get('request_equipment_quantity')
                request_description = request.POST.get('request_equipment_description')
                request_brand = request.POST.get('request_equipment_brand')
                request_acceptquantity = request.POST.get('request_equipment_acceptquantity')
                getdata = requestequipment.objects.get(requestequipment_id=request_id).requestequipment_id

                if int(request_acceptquantity) > int(request_quantity):

                    messages.info(request, 'request quantity is less than to accept quantity')
                    return redirect('inventorysystem-equipmentDeliver')
                
                elif int(request_acceptquantity) < int(request_quantity) or int(request_acceptquantity) == int(request_quantity):
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
                        accept.save()
                        storage = equipmentmainstorage()  
                        storage.equipmentmainstorage_itemName = request_itemname
                        storage.equipmentmainstorage_description = request_description
                        storage.equipmentmainstorage_brand = request_brand
                        storage.equipmentmainstorage_remaining = request_acceptquantity
                        storage.equipmentmainstorage_quantity = request_acceptquantity
                        storage.save()

                        delivery_record1 = deliveryequipment()
                        delivery_record1.delivery_equipment_itemname = request_itemname
                        delivery_record1.delivery_equipment_description = request_description
                        delivery_record1.delivery_equipment_brand = request_brand
                        delivery_record1.delivery_equipment_quantity = request_acceptquantity
                        delivery_record1.delivery_equipment_remaining = request_acceptquantity
                        delivery_record1.save()
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
                        status.save()

                        if int(request.POST.get('request_equipment_unitcost')) < int(50000) :
                            saveform = receiptform_equipment()
                            saveform.receiptformequipment_itemname = request_itemname
                            saveform.receiptformequipment_department = request_department
                            saveform.receiptformequipment_description = request_description
                            saveform.receiptformequipment_unit = request.POST.get('request_equipment_unit')
                            saveform.receiptformequipment_quantity = request_acceptquantity
                            saveform.receiptformequipment_propertyno = request.POST.get('request_equipment_iin')
                            saveform.receiptformequipment_amount = request.POST.get('request_equipment_unitcost')
                            saveform.current_date = datetime.date.today()
                            saveform.save()

                        elif int(request.POST.get('request_equipment_unitcost')) >= int(50000):
                            saveform2 = custodian_slip()
                            saveform2.custodianslip_itemname = request_itemname
                            saveform2.custodianslip_description = request_description
                            saveform2.custodianslip_department = request_department
                            saveform2.custodianslip_unit = request.POST.get('request_equipment_unit')
                            saveform2.custodianslip_quantity = request_acceptquantity
                            saveform2.custodianslip_inventoryitemno = request.POST.get('request_equipment_iin')
                            saveform2.custodianslip_unitcost = request.POST.get('request_equipment_unitcost')
                            saveform2.custodianslip_totalcost = int(request_acceptquantity) * int(request.POST.get('request_equipment_unitcost'))
                            saveform2.current_date = datetime.date.today()
                            saveform2.save()

                        
                        if equipment_email.objects.filter(emailequipment_department = request_department).filter(current_date = datetime.date.today()).exists() == True:
                            emaildept = equipment_email()
                            emaildept.emailequipment_id = equipment_email.objects.get(emailequipment_department = request_department).emailequipment_id
                            emaildept.emailequipment_department = request_department
                            emailqty = equipment_email.objects.get(emailequipment_department = request_department).emailequipment_acceptedquantity
                            emaildept.emailequipment_acceptedquantity = int(emailqty) + int(1)
                            emaildept.current_date = datetime.date.today()
                            equipment_email.objects.filter(emailequipment_department = request_department).delete()
                            emaildept.save()
                            messages.success(request, 'request accepted')

                        elif equipment_email.objects.filter(emailequipment_department = request_department).filter(current_date = datetime.date.today()).exists() == False:
                            emaildept1 = equipment_email()
                            emaildept1.emailequipment_department = request_department
                            emaildept1.emailequipment_acceptedquantity = 1
                            emaildept1.current_date = datetime.date.today()
                            emaildept1.save()
                            messages.success(request, 'request accepted')

                        return redirect('inventorysystem-equipmentDeliver')

            elif 'emailBtn1' in request.POST:

                subject = "SUPPLY DEPARTMENT ADMIN"
                message = "Good day! \n\nYour request has been accepted. Please pick up the item/s as soon as possible. Thankyou. \n\nKind regards,\nSupply Admin"
                depinfo = str(CustomUser.objects.get(department=str(request.POST.get('email_equipment_department'))).email)
                print(depinfo)
                recipient = depinfo
                send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
                equipment_email.objects.filter(emailequipment_department = request.POST.get('email_equipment_department')).filter(current_date = request.POST.get('email_equipment_date')).delete()
                messages.success(request, 'successfully sent')

        context = {
            'form': form,
            'info': info,
            'info1': info1,
            'info2': info2,
            'info3': info3,
            'info4': info4,
            'label': label,

        }
        return render(request, 'task/equipment-delivery.html', context)
    else:
        return redirect('inventorysystem-usersLogin')



#------------------- ADMIN VIEW REQUEST EQUIPMENTS -----------------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def viewDeliveryRecords(request):
    if (request.user.is_authenticated and request.user.is_superuser) or \
        (request.user.is_authenticated and request.user.is_admin):

        label = request.user
        info = deliveryequipment.objects.all()
        context = {
            'info': info,
            'label': label,
        }
        return render(request, 'task/view-delivery-records.html', context)
    else:
        return redirect('inventorysystem-usersLogin') 



#------------------- DEPARTMENT REQUEST EQUIPMENTS -----------------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def depRequestEquipment(request):
    if (request.user.is_authenticated and request.user.is_department):

        info = equipmentmainstorage.objects.all()
        info1  = statusEquipmentRequest.objects.all().filter(status_equipment_department = request.user)
        # info2 = withdrawequipment.objects.all().filter(withdraw_equipment_issued_to = request.user)

        if request.method == 'POST':
            if int(request.POST.get('non_existing_equipment_quantity')) > 0:
                if statusEquipmentRequest.objects.filter(status_equipment_itemname = request.POST.get('non_existing_equipment_itemname')).filter(status_equipment_department = request.user).exists() == False:
                    requesting = requestequipment()
                    requesting.request_equipment_itemname = request.POST.get('non_existing_equipment_itemname')
                    requesting.request_equipment_quantity = request.POST.get('non_existing_equipment_quantity')
                    requesting.request_equipment_department = str(request.user)
                    requesting.request_equipment_description = request.POST.get('non_existing_equipment_description')
                    requesting.request_equipment_status = "pending"
                    status = statusEquipmentRequest()
                    status.status_equipment_itemname = request.POST.get('non_existing_equipment_itemname')
                    status.status_equipment_quantity = request.POST.get('non_existing_equipment_quantity')
                    status.status_equipment_department = str(request.user)
                    status.status_equipment_description = request.POST.get('non_existing_equipment_description')
                    status.status_equipment_status = "pending"
                    messages.success(request, 'Request Successful for itemname ')
                    subject = str(request.user)
                    message = "Good day!\n\nI have requested item in supply. Please see the details in the website. Thank you!\n\nKind regards,\n"+ str(request.user)
                    depinfo = str(CustomUser.objects.get(department=str(request.user)).email)
                    print(depinfo)
                    recipient = settings.EMAIL_HOST_USER
                    send_mail(subject, message, depinfo, [recipient], fail_silently=False)
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
        }
        return render(request, 'task/dep-request-equipment.html', context)
    else:
        return redirect('inventorysystem-usersLogin')



#------------------- WITHDRAW EQUIPMENTS -----------------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def equipmentWithdraw(request):
    if (request.user.is_authenticated and request.user.is_superuser) or \
        (request.user.is_authenticated and request.user.is_admin):
        
        label = request.user
        info = acceptEquipmentRequests.objects.all()
        info1 = withdrawequipment.objects.all()
        info2 = custodian_slip.objects.all()
        info3 = receiptform_equipment.objects.all()
        context = {
            'info': info,
            'info1': info1,
            'info2': info2,
            'info3': info3,
            'label': label,
        }
        return render(request, 'task/equipment-withdraw.html', context)
    else:
        return redirect('inventorysystem-usersLogin')

@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def createqrequipmentWithdraw(request, pk):
    if (request.user.is_authenticated and request.user.is_superuser) or \
        (request.user.is_authenticated and request.user.is_admin):

        label = request.user
        data = acceptEquipmentRequests.objects.get(arequest_equipment_id=pk)
        form = withdrawEquipmentForm(request.POST or None, instance=data)
        if request.method == 'POST':
            getdata4 = acceptEquipmentRequests.objects.get(arequest_equipment_id=pk).arequest_equipment_id
            getdata5 = acceptEquipmentRequests.objects.get(arequest_equipment_id = getdata4)

            if withdrawequipment.objects.filter(withdraw_equipment_property_no = request.POST.get('arequest_equipment_property_no')).exists() == True:
                messages.info(request, 'existing property no.')

            elif withdrawequipment.objects.filter(withdraw_equipment_serial_no = request.POST.get('arequest_equipment_serial_no')).exists() == True:
                messages.info(request, 'existing serial no.')

            elif withdrawequipment.objects.filter(withdraw_equipment_model_no = request.POST.get('arequest_equipment_model_no')).exists() == True:
                messages.info(request, 'existing model no.')


            elif equipment_email.objects.filter(emailequipment_department = request.POST.get('arequest_equipment_issued_to')).exists() == True:
                messages.info(request, 'please email the department.')


            elif acceptEquipmentRequests.objects.filter(arequest_equipment_itemname = request.POST.get('arequest_equipment_itemname')).filter(arequest_equipment_issued_to = request.POST.get('arequest_equipment_issued_to')).exists() == True:

                data1 = acceptEquipmentRequests.objects.get(arequest_equipment_id=pk).arequest_equipment_id

                if int(acceptEquipmentRequests.objects.get(arequest_equipment_id = data1).arequest_equipment_quantity) == 1:
                    accept = withdrawequipment()
                    getdata2 = acceptEquipmentRequests.objects.get(arequest_equipment_id=pk).arequest_equipment_id
                    accept.withdraw_equipment_property_no = request.POST.get('arequest_equipment_property_no')
                    accept.withdraw_equipment_itemname = request.POST.get('arequest_equipment_itemname')
                    accept.withdraw_equipment_description = request.POST.get('arequest_equipment_description')
                    accept.withdraw_equipment_brand = request.POST.get('arequest_equipment_brand')
                    accept.withdraw_equipment_yearacquired = request.POST.get('arequest_equipment_yearacquired')
                    accept.withdraw_equipment_issued_to = request.POST.get('arequest_equipment_issued_to')
                    accept.withdraw_equipment_model_no = request.POST.get('arequest_equipment_model_no')
                    accept.withdraw_equipment_serial_no = request.POST.get('arequest_equipment_serial_no')
                    accept.withdraw_equipment_certifiedcorrect = request.POST.get('arequest_equipment_certifiedcorrect')
                    accept.withdraw_equipment_status = "withdrawn"
                    acceptEquipmentRequests.objects.filter(arequest_equipment_id = data1).delete()
                    statusEquipmentRequest.objects.filter(statusEquipmentRequests_id = getdata2).delete()         
                    acceptEquipmentRequests.objects.filter(arequest_equipment_id = data1).delete()
                    statusEquipmentRequest.objects.filter(statusEquipmentRequests_id = getdata2).delete()
                    accept.save()
                    messages.success(request, 'successfully withdraw')
                    return redirect('inventorysystem-equipmentWithdraw')


                elif int(acceptEquipmentRequests.objects.get(arequest_equipment_id = data1).arequest_equipment_quantity) > 1:

                    accept = withdrawequipment() 
                    getdata2 = acceptEquipmentRequests.objects.get(arequest_equipment_idd=pk).arequest_equipment_id
                    accept.withdraw_equipment_property_no = request.POST.get('arequest_equipment_property_no')
                    accept.withdraw_equipment_itemname = request.POST.get('arequest_equipment_itemname')
                    accept.withdraw_equipment_description = request.POST.get('arequest_equipment_description')
                    accept.withdraw_equipment_brand = request.POST.get('arequest_equipment_brand')
                    accept.withdraw_equipment_yearacquired = request.POST.get('arequest_equipment_yearacquired')
                    accept.withdraw_equipment_issued_to = request.POST.get('arequest_equipment_issued_to')
                    accept.withdraw_equipment_model_no = request.POST.get('arequest_equipment_model_no')
                    accept.withdraw_equipment_serial_no = request.POST.get('arequest_equipment_serial_no')
                    accept.withdraw_equipment_certifiedcorrect = request.POST.get('arequest_equipment_certifiedcorrect')
                    accept.withdraw_equipment_status = "withdrawn"
                    acceptEquipmentRequests.objects.filter(arequest_equipment_id = data1).delete()

                    not_delete = acceptEquipmentRequests()
                    not_delete.arequest_equipment_id = getdata4
                    not_delete.arequest_equipment_itemname = getdata5.arequest_equipment_itemname
                    not_delete.arequest_equipment_description = getdata5.arequest_equipment_description
                    not_delete.arequest_equipment_brand = getdata5.arequest_equipment_brand
                    not_delete.arequest_equipment_quantity = int(getdata5.arequest_equipment_quantity) - 1
                    not_delete.arequest_equipment_status = getdata5.arequest_equipment_status
                    not_delete.arequest_equipment_issued_to = getdata5.arequest_equipment_issued_to
                    not_delete.current_date = getdata5.current_date
                    not_delete.save()
                    accept.save()
                    messages.success(request, 'Successfully withdrawn.')
                    return redirect('inventorysystem-equipmentWithdraw')

                
        context = {
            'data': data,
            'form': form,
            'label': label,
        }

        return render(request, 'task/createqr-equipment-withdraw.html', context)
    else:
        return redirect('inventorysystem-usersLogin')


#------------------- RETURN EQUIPMENTS -----------------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def equipmentReturn(request):
    if (request.user.is_authenticated and request.user.is_superuser) or \
        (request.user.is_authenticated and request.user.is_admin):
        
        label = request.user
        info = returnequipment.objects.all()
        if request.method == 'POST':
            data = request.POST.get('property')
            if 'returnBtn' in request.POST:
                if returnequipment.objects.filter(return_equipment_property_no = data).exists() == True:
                    messages.info(request, 'This equipment was already returned.')
                    return redirect('inventorysystem-equipmentReturn')

                elif withdrawequipment.objects.filter(withdraw_equipment_property_no = data).exists() == True:
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
                    
                    changestats = withdrawequipment()
                    changestats.withdraw_equipment_property_no = getdata.withdraw_equipment_property_no
                    changestats.withdraw_equipment_itemname = getdata.withdraw_equipment_itemname
                    changestats.withdraw_equipment_description = getdata.withdraw_equipment_description
                    changestats.withdraw_equipment_brand = getdata.withdraw_equipment_brand
                    changestats.withdraw_equipment_yearacquired = getdata.withdraw_equipment_yearacquired
                    changestats.withdraw_equipment_issued_to = getdata.withdraw_equipment_issued_to
                    changestats.withdraw_equipment_model_no = getdata.withdraw_equipment_model_no
                    changestats.withdraw_equipment_serial_no = getdata.withdraw_equipment_serial_no
                    changestats.withdraw_equipment_certifiedcorrect = getdata.withdraw_equipment_certifiedcorrect
                    changestats.withdraw_equipment_status = "Returned"
                    withdrawequipment.objects.filter(withdraw_equipment_property_no = data).delete()
                    changestats.save()


                    messages.success(request, 'Equipment returned sucessfully.')
                    return redirect('inventorysystem-equipmentReturn')

                    
                else: 
                    messages.info(request, 'Non-existing equipment record. Please scan a valid one.')
                    return redirect('inventorysystem-equipmentReturn')

            if 'disposedBtn' in request.POST:

                disposed = equipment_disposal()
                disposed.dispose_equipment_location = request.POST.get('disposedLocation')
                disposed.dispose_equipment_property_no = request.POST.get('disposedPropertyNo')
                disposed.dispose_equipment_itemname = request.POST.get('disposedItemName')
                disposed.dispose_equipment_description = request.POST.get('disposedDescription')
                disposed.dispose_equipment_brand = request.POST.get('disposedBrand')
                disposed.dispose_equipment_yearacquired = request.POST.get('disposedYearAcquired')
                disposed.dispose_equipment_issued_to = request.POST.get('disposedIssuedTo')
                disposed.dispose_equipment_model_no = request.POST.get('disposedModelNo')
                disposed.dispose_equipment_serial_no = request.POST.get('disposedSerialNo')
                disposed.dispose_equipment_certifiedcorrect = request.POST.get('disposedCertifiedCorrect')
                disposed.return_date = request.POST.get('disposed_returnDate')
                returnequipment.objects.filter(return_equipment_property_no = request.POST.get('disposedPropertyNo')).delete()
                disposed.save()
                messages.success(request, 'Equipment disposed sucessfully.')

                changestats = withdrawequipment()
                changestats.withdraw_equipment_property_no = request.POST.get('disposedPropertyNo')
                changestats.withdraw_equipment_itemname = request.POST.get('disposedItemName')
                changestats.withdraw_equipment_description = request.POST.get('disposedDescription')
                changestats.withdraw_equipment_brand = request.POST.get('disposedBrand')
                changestats.withdraw_equipment_yearacquired = request.POST.get('disposedYearAcquired')
                changestats.withdraw_equipment_issued_to = request.POST.get('disposedSerialNo')
                changestats.withdraw_equipment_model_no = request.POST.get('disposedModelNo')
                changestats.withdraw_equipment_serial_no = request.POST.get('disposedSerialNo')
                changestats.withdraw_equipment_certifiedcorrect = request.POST.get('disposedCertifiedCorrect')
                changestats.withdraw_equipment_status = "Disposed"
                withdrawequipment.objects.filter(withdraw_equipment_property_no = request.POST.get('disposedPropertyNo')).delete()
                changestats.save()


        context = {
            'info': info,
            'label': label,
        }
        return render(request, 'task/equipment-return.html', context)
    else:
        return redirect('inventorysystem-usersLogin')


#------------------- STORAGE MAPPING -----------------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='inventorysystem-usersLogin')
def storageMapping(request):
    if (request.user.is_authenticated and request.user.is_superuser) or \
        (request.user.is_authenticated and request.user.is_admin):

        label = request.user
        info = supplymainstorage.objects.all()
        info1 = equipment_disposal.objects.all()

        if request.method == 'POST':

            if 'storagesupply_update' in request.POST:
                item = request.POST.get('supplyItemName')
                locsave = supplymainstorage()
                locsave.supplymainstorage_id = request.POST.get('supplymainstorage_id')
                locsave.supplymainstorage_description = request.POST.get('supplyItemName')
                locsave.supplymainstorage_unit = supplymainstorage.objects.get(supplymainstorage_description = request.POST.get('supplyItemName')).supplymainstorage_unit
                locsave.supplymainstorage_quantity = supplymainstorage.objects.get(supplymainstorage_description = request.POST.get('supplyItemName')).supplymainstorage_quantity
                locsave.supplymainstorage_supplyRackNo = request.POST.get('supplyRackNo')
                locsave.supplymainstorage_supplyLayerNo = request.POST.get('supplyLayerNo')
                locsave.supplymainstorage_supplyCabinetNo = request.POST.get('supplyCabinetNo')
                locsave.supplymainstorage_supplyShelfNo = request.POST.get('supplyShelfNo')
                supplymainstorage.objects.filter(supplymainstorage_description = request.POST.get('supplyItemName')).delete()
                locsave.save()
                messages.success(request, 'Successfully updated storage mapping for item ' + item)
                return redirect('inventorysystem-storageMapping')

        context = {
            'info': info,
            'info1': info1,
            'label': label,
        }

        return render(request, 'task/storage-mapping.html', context)
    else:
        return redirect('inventorysystem-usersLogin')


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
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf(presentational_hints=True)

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
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf(presentational_hints=True)

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
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf(presentational_hints=True)

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
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf(presentational_hints=True)

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
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf(presentational_hints=True)

    with tempfile.NamedTemporaryFile(delete=False) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    
    return response

def uploadsupplypdf(request):
     return render(request, 'task/upload-supply-pdf.html',)


def export_pdf_supplycreateform(request):
        response=HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; attachment; filename=Supply Inventory' + \
            str(datetime.datetime.now())+'.pdf'
        supply = supply_createform.objects.all().filter(createformsupply_department = request.user)
        supply1 = supply_createform_inputs.objects.all().filter(createformsupply_inputs_department = request.user)
        response['Content-Transfer-Enconding'] = 'binary'


        html_string = render_to_string('task/pdf-output-supplycreateform.html' ,{'Form': supply,'Form1': supply1})
        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        result = html.write_pdf(presentational_hints=True)

        with tempfile.NamedTemporaryFile(delete=False) as output:
            output.write(result)
            output.flush()
            output = open(output.name, 'rb')
            response.write(output.read())

        return response

def export_pdf_equipment_arecreateform(request):
        response=HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; attachment; filename=Supply Inventory' + \
            str(datetime.datetime.now())+'.pdf'
        equipment = receiptform_equipment.objects.all()
        equipment1 = equipment_areform_inputs.objects.all()
        response['Content-Transfer-Enconding'] = 'binary'


        html_string = render_to_string('task/pdf-output-equipment-are.html' ,{'Form': equipment, 'Form1': equipment1})
        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        result = html.write_pdf(presentational_hints=True)

        with tempfile.NamedTemporaryFile(delete=False) as output:
            output.write(result)
            output.flush()
            output = open(output.name, 'rb')
            response.write(output.read())

        return response

def export_pdf_equipment_icscreateform(request):
        response=HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; attachment; filename=Supply Inventory' + \
            str(datetime.datetime.now())+'.pdf'
        equipment = custodian_slip.objects.all()
        equipment1 = equipment_icsform_inputs.objects.all()
        response['Content-Transfer-Enconding'] = 'binary'


        html_string = render_to_string('task/pdf-output-equipment-ics.html' ,{'Equip': equipment, 'Equips': equipment1})
        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        result = html.write_pdf(presentational_hints=True)

        with tempfile.NamedTemporaryFile(delete=False) as output:
            output.write(result)
            output.flush()
            output = open(output.name, 'rb')
            response.write(output.read())

        return response