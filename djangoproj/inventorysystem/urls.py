from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inventorysystem-index'),
    path('home', views.home, name='inventorysystem-home'),
    path('add-department-account/', views.deptRegister, name='inventorysystem-deptRegister'),
    path('add-admin-account/', views.adminRegister, name='inventorysystem-adminRegister'),
    path('login/', views.usersLogin, name='inventorysystem-usersLogin'),
#---------- PATH FOR SUPPLIES ----------------------
    path('supplies-delivery/', views.suppliesDeliver, name='inventorysystem-suppliesDeliver'),
    path('status-limit/', views.statusLimit, name='inventorysystem-statusLimit'),
    path('view-request-supplies/', views.viewRequestSupply, name='inventorysystem-viewRequestSupply'),
    path('dep-request-supply/', views.depRequestSupply, name='inventorysystem-depRequestSupply'), 
    path('supplies-withdraw/', views.suppliesWithdraw, name='inventorysystem-suppliesWithdraw'),
#---------- PATH FOR EQUIPMENT ----------------------
    path('equipment-delivery/', views.equipmentDeliver, name='inventorysystem-equipmentDeliver'),
    path('view-delivery-records/', views.viewDeliveryRecords, name='inventorysystem-viewDeliveryRecords'),
    path('dep-request-equipment/', views.depRequestEquipment, name='inventorysystem-depRequestEquipment'),
    path('equipment-withdraw/', views.equipmentWithdraw, name='inventorysystem-equipmentWithdraw'),
    path('createqr-equipment-withdraw/<int:pk>/', views.createqrequipmentWithdraw, name='inventorysystem-createqrequipmentWithraw'),
    path('equipment-return/', views.equipmentReturn, name='inventorysystem-equipmentReturn'),
#------------ MAPPING x EXPORT ----------------------
    path('storage-mapping/', views.storageMapping, name='inventorysystem-storageMapping'),
    path('export_excel/', views.export_excel, name='export_excel'),
    path('export_pdf_suppydelivery/', views.export_pdf_suppydelivery, name='export_pdf_suppydelivery'),
    path('export_pdf_suppywithdraw/', views.export_pdf_suppywithdraw, name='export_pdf_suppywithdraw'),
    path('export_pdf_equipdelivery/', views.export_pdf_equipdelivery, name='export_pdf_equipdelivery'),
    path('export_pdf_equipwithdraw/', views.export_pdf_equipwithdraw, name='export_pdf_equipwithdraw'),
    path('export_pdf_equipreturn/', views.export_pdf_equipreturn, name='export_pdf_equipreturn'),
]


