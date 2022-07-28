from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='inventorysystem-home'),
    path('supplies-delivery/', views.suppliesDeliver, name='inventorysystem-suppliesDeliver'),
    path('add-supply-item/', views.addSupply, name='inventorysystem-addSupply'),
]
