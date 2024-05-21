from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	   
    path('Registration',views.Registration),
    path('success',views.success),
    
]