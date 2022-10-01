from django.urls import path
from . import views

urlpatterns = [
    path('', views.userLogin, name='inventorysystem-userLogin'),
    path('home', views.home, name='inventorysystem-home'),
    path('add-department-account/', views.deptRegister, name='inventorysystem-deptRegister'),
    path('supplies-delivery/', views.suppliesDeliver, name='inventorysystem-suppliesDeliver'),
    path('add-new-items/', views.addItem, name='inventorysystem-addItem'),
    path('equipment-delivery/', views.equipmentDeliver, name='inventorysystem-equipmentDeliver'),
    #path('add-equipment-item/', views.addEquipment, name='inventorysystem-addEquipment'),
    path('supplies-withdraw/', views.suppliesWithdraw, name='inventorysystem-suppliesWithdraw'),
    path('equipment-withdraw/', views.equipmentWithdraw, name='inventorysystem-equipmentWithdraw'),
    path('view-request-supplies/', views.viewRequestSupply, name='inventorysystem-viewRequestSupply'),
    path('view-request-equipment/', views.viewRequestEquipment, name='inventorysystem-viewRequestEquipment'),
    path('dep-request-supply/', views.depRequestSupply, name='inventorysystem-depRequestSupply'),
    path('dep-request-equipment/', views.depRequestEquipment, name='inventorysystem-depRequestEquipment'),
    path('status-limit/', views.statusLimit, name='inventorysystem-statusLimit'),
    path('equipment-return/', views.equipmentReturn, name='inventorysystem-equipmentReturn'),
    path('storage-mapping/', views.storageMapping, name='inventorysystem-storageMapping'),
    path('export_excel/', views.export_excel, name='export_excel'),
]

