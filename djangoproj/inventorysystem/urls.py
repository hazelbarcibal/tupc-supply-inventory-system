from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='inventorysystem-index'),
    path('logout/', views.logoutUser, name='inventorysystem-logout'),
    path('add-department-account/', views.deptRegister, name='inventorysystem-deptRegister'),
    path('add-admin-account/', views.adminRegister, name='inventorysystem-adminRegister'),
    path('login/', views.usersLogin, name='inventorysystem-usersLogin'),
    path('dashboard/', views.dashboard, name='inventorysystem-dashboard'),
    path('update-admin-profile/', views.adminProfileUpdate, name='inventorysystem-adminProfileUpdate'),
    path('update-dept-profile/', views.deptProfileUpdate, name='inventorysystem-deptProfileUpdate'),

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
    # path('export_pdf_supplycreateform/', views.export_pdf_supplycreateform, name='export_pdf_supplycreateform'),
]


