from django.contrib import admin
from .models import CustomUser
from .models import *



#admin.site.register(adminAcc)
admin.site.register(deliverysupply)
admin.site.register(deliveryequipment)
admin.site.register(requestsupply)
admin.site.register(requestequipment)
admin.site.register(withdrawsupply)
admin.site.register(withdrawequipment)
admin.site.register(returnequipment)
admin.site.register(limitrecords)
admin.site.register(supplymainstorage)
admin.site.register(equipmentmainstorage)
admin.site.register(CustomUser)

