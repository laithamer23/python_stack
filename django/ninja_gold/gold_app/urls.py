from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
   path('buttom',views.increase),
   path('buttom1',views.dncrease),
      
]