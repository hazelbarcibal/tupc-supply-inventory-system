from django.urls import path
from . import views

urlpatterns = [
    path('', views.userLogin, name='inventorysystem-userLogin'),
    path('department-login/', views.deptLogin, name='inventorysystem-deptLogin'),
    path('home', views.home, name='inventorysystem-home'),
    path('add-department-account/', views.deptRegister, name='inventorysystem-deptRegister'),
#---------- PATH FOR SUPPLIES ----------------------
    path('supplies-delivery/', views.suppliesDeliver, name='inventorysystem-suppliesDeliver'),
    path('update-supplies-delivery/<int:pk>/', views.updateSuppliesDeliver, name='inventorysystem-updateSuppliesDeliver'),
    #path('add-new-items/', views.addItem, name='inventorysystem-addItem'),
    path('status-limit/', views.statusLimit, name='inventorysystem-statusLimit'),
    path('update-status/<int:pk>/', views.updateStatus, name='inventorysystem-updateStatus'),
    path('supplies-withdraw/', views.suppliesWithdraw, name='inventorysystem-suppliesWithdraw'),
    path('update-supply-withdraw/<int:pk>/', views.updateSupplyWithdraw, name='inventorysystem-updateSupplyWithdraw'),
    path('supplies-withdraw-status/<int:pk>/', views.suppliesWithdrawStatus, name='inventorysystem-suppliesWithdrawStatus'),
    path('view-request-supplies/', views.viewRequestSupply, name='inventorysystem-viewRequestSupply'),
    path('edit-request-supplies/<int:pk>/', views.editRequestSupply, name='inventorysystem-editRequestSupply'),
    path('dep-request-supply/', views.depRequestSupply, name='inventorysystem-depRequestSupply'),
    path('edit-dep-request-supply/<int:pk>/', views.editdepRequestSupply, name='inventorysystem-editdepRequestSupply'),  
#---------- PATH FOR EQUIPMENT ----------------------
    path('equipment-delivery/', views.equipmentDeliver, name='inventorysystem-equipmentDeliver'),
    path('update-equipment-delivery/<int:pk>/', views.updateEquipmentDeliver, name='inventorysystem-updateEquipmentDeliver'),
    path('equipment-withdraw/', views.equipmentWithdraw, name='inventorysystem-equipmentWithdraw'),
    #PK FOR EQUIPMENT WITHDRAW, sa next line
    path('createqr-equipment-withdraw/', views.createqrequipmentWithdraw, name='inventorysystem-createqrequipmentWith'),
    path('view-request-equipment/', views.viewRequestEquipment, name='inventorysystem-viewRequestEquipment'),
    #PK FOR VIEW REQUEST, sa next line
    path('edit-request-equipment/', views.editRequestEquipment, name='inventorysystem-editRequestEquipment'),
    path('dep-request-equipment/', views.depRequestEquipment, name='inventorysystem-depRequestEquipment'),
    #norem pa dapat edit-request-equip dto sa line na to!
    path('equipment-return/', views.equipmentReturn, name='inventorysystem-equipmentReturn'),
#------------ MAPPING x EXPORT ----------------------
    path('storage-mapping/', views.storageMapping, name='inventorysystem-storageMapping'),
    path('update-storage/<int:pk>/', views.updateStoragemapping, name='inventorysystem-updateStoragemapping'),
    path('export_excel/', views.export_excel, name='export_excel'),
]

