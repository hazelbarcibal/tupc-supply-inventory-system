from django.urls import path
from . import views

urlpatterns = [
    path('', views.userLogin, name='inventorysystem-userLogin'),
    path('department-login/', views.deptLogin, name='inventorysystem-deptLogin'),
    path('home', views.home, name='inventorysystem-home'),
    path('add-department-account/', views.deptRegister, name='inventorysystem-deptRegister'),
    path('supplies-delivery/', views.suppliesDeliver, name='inventorysystem-suppliesDeliver'),
    path('update-supplies-delivery/<int:pk>/', views.updateSuppliesDeliver, name='inventorysystem-updateSuppliesDeliver'),
    path('add-new-items/', views.addItem, name='inventorysystem-addItem'),
    path('equipment-delivery/', views.equipmentDeliver, name='inventorysystem-equipmentDeliver'),
    path('update-equipment-delivery/<int:pk>/', views.updateEquipmentDeliver, name='inventorysystem-updateEquipmentDeliver'),
    #path('add-equipment-item/', views.addEquipment, name='inventorysystem-addEquipment'),
    path('supplies-withdraw/', views.suppliesWithdraw, name='inventorysystem-suppliesWithdraw'),
    path('equipment-withdraw/', views.equipmentWithdraw, name='inventorysystem-equipmentWithdraw'),
    path('createqr-equipment-withdraw/', views.createqrequipmentWithdraw, name='inventorysystem-createqrequipmentWith'),

    path('view-request-supplies/', views.viewRequestSupply, name='inventorysystem-viewRequestSupply'),
    path('edit-request-supplies/<int:pk>/', views.editRequestSupply, name='inventorysystem-editRequestSupply'),

    path('supplies-withdraw-status/<int:pk>/', views.suppliesWithdrawStatus, name='inventorysystem-suppliesWithdrawStatus'),
    path('view-request-equipment/', views.viewRequestEquipment, name='inventorysystem-viewRequestEquipment'),
    path('dep-request-supply/', views.depRequestSupply, name='inventorysystem-depRequestSupply'),
    path('edit-dep-request-supply/<int:pk>/', views.editdepRequestSupply, name='inventorysystem-editdepRequestSupply'),

    path('dep-request-equipment/', views.depRequestEquipment, name='inventorysystem-depRequestEquipment'),
    path('status-limit/', views.statusLimit, name='inventorysystem-statusLimit'),
    path('update-status/<int:pk>/', views.updateStatus, name='inventorysystem-updateStatus'),
    path('equipment-return/', views.equipmentReturn, name='inventorysystem-equipmentReturn'),
    path('storage-mapping/', views.storageMapping, name='inventorysystem-storageMapping'),
    path('update-storage/<int:pk>/', views.updateStoragemapping, name='inventorysystem-updateStoragemapping'),
    path('export_excel/', views.export_excel, name='export_excel'),
]

