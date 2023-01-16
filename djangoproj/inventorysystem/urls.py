from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
# from django.urls import re_path as url

urlpatterns = [
    path('', views.index, name='inventorysystem-index'),
    path('logout/', views.logoutUser, name='inventorysystem-logout'),
    path('add-department-account/', views.deptRegister, name='inventorysystem-deptRegister'),
    path('add-admin-account/', views.adminRegister, name='inventorysystem-adminRegister'),
    path('login/', views.usersLogin, name='inventorysystem-usersLogin'),
    path('dashboard/', views.dashboard, name='inventorysystem-dashboard'),
    path('update-admin-profile/', views.adminProfileUpdate, name='inventorysystem-adminProfileUpdate'),
    path('update-dept-profile/', views.deptProfileUpdate, name='inventorysystem-deptProfileUpdate'),

    path('upload/', views.upload_file, name='inventorysystem-upload'),
    path('table/', views.table, name='inventorysystem-table'),
    

    # path('password-reset/', views.password_reset_request, name='inventorysystem-passwordChange'),
    # path('password-reset-done/', views.password_reset_done, name='inventorysystem-passwordResetDone'),
    # # path('password-reset/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    # # path('password-reset-sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='inventorysystem-passwordResetConfirm'),
    # path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path("password-reset/", views.password_reset_request, name="inventorysystem-passwordChange"),

#---------- PATH FOR SUPPLIES ----------------------
    path('supplies-delivery/', views.suppliesDeliver, name='inventorysystem-suppliesDeliver'),
    path('status-limit/', views.statusLimit, name='inventorysystem-statusLimit'),
    path('view-request-supplies/', views.viewRequestSupply, name='inventorysystem-viewRequestSupply'),
    path('dep-request-supply/', views.depRequestSupply, name='inventorysystem-depRequestSupply'), 
    path('supplies-withdraw/', views.suppliesWithdraw, name='inventorysystem-suppliesWithdraw'),
    path('supplies-createform/', views.suppliesCreateform, name='inventorysystem-suppliesCreateform'),
#---------- PATH FOR EQUIPMENT ----------------------
    path('equipment-delivery/', views.equipmentDeliver, name='inventorysystem-equipmentDeliver'),
    path('equipment-requests/', views.equipmentRequests, name='inventorysystem-equipmentrequests'),
    path('dep-request-equipment/', views.depRequestEquipment, name='inventorysystem-depRequestEquipment'),
    path('equipment-withdraw/', views.equipmentWithdraw, name='inventorysystem-equipmentWithdraw'),
    path('createqr-equipment-withdraw/<int:pk>/', views.createqrequipmentWithdraw, name='inventorysystem-createqrequipmentWithraw'),
    path('equipment-return/', views.equipmentReturn, name='inventorysystem-equipmentReturn'),
    path('equipment-icsform/', views.equipmentIcsform, name='inventorysystem-equipment-icsform'),
    path('equipment-areform/', views.equipmentAreform, name='inventorysystem-equipment-areform'),

    url(r'^validateInfo/$', views.validateInfo, name='inventorysystem-validateInfo'),
    url(r'^validateInfo1/$', views.validateInfo1, name='inventorysystem-validateInfo1'),
    url(r'^validateInfo2/$', views.validateInfo2, name='inventorysystem-validateInfo2'),
#------------ MAPPING x EXPORT ----------------------
    path('supplies-storage-location/', views.storagelocationSupplies, name='inventorysystem-storagelocationSupplies'),
    path('equipments-storage-location/', views.storagelocationEquipment, name='inventorysystem-storagelocationEquipment'),
    path('export_excel/', views.export_excel, name='export_excel'),
    path('export_pdf_suppydelivery/', views.export_pdf_suppydelivery, name='export_pdf_suppydelivery'),
    path('export_pdf_suppywithdraw/', views.export_pdf_suppywithdraw, name='export_pdf_suppywithdraw'),
    path('export_pdf_equipdelivery/', views.export_pdf_equipdelivery, name='export_pdf_equipdelivery'),
    path('export_pdf_equipwithdraw/', views.export_pdf_equipwithdraw, name='export_pdf_equipwithdraw'),
    path('export_pdf_equipreturn/', views.export_pdf_equipreturn, name='export_pdf_equipreturn'),
    path('export_pdf_equipdisposed/', views.export_pdf_equipdisposed, name='export_pdf_equipdisposed'),
    path('export_pdf_supplycreateform/', views.export_pdf_supplycreateform, name='export_pdf_supplycreateform'),
    path('export_pdf_equipment_arecreateform/', views.export_pdf_equipment_arecreateform, name='export_pdf_equipment_arecreateform'),
    path('export_pdf_equipment_icscreateform/', views.export_pdf_equipment_icscreateform, name='export_pdf_equipment_icscreateform'),
    path('upload-supply-pdf/', views.uploadsupplypdf, name='upload-supply-pdf'),

    path('dep-withdrawn-items/', views.depWithdrawnItems, name='inventorysystem-depWithdrawnItems'),
    
    path('helpcenter/', views.Helpcenter, name='inventorysystem-helpcenter'),
    path('helpcenterdep/', views.Helpcenterdep, name='inventorysystem-helpcenterdep'),
]


