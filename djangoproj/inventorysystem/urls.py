from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='inventorysystem-home'),
    path('supplies-delivery/', views.suppliesDeliver, name='inventorysystem-suppliesDeliver'),
    path('add-supply-item/', views.addSupply, name='inventorysystem-addSupply'),
    path('equipment-delivery/', views.equipmentDeliver, name='inventorysystem-equipmentDeliver'),
    path('add-equipment-item/', views.addEquipment, name='inventorysystem-addEquipment'),
    path('supplies-withdraw/', views.suppliesWithdraw, name='inventorysystem-suppliesWithdraw'),
    path('equipment-withdraw/', views.equipmentWithdraw, name='inventorysystem-equipmentWithdraw'),
]
