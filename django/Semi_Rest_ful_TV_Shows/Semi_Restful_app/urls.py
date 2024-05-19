from django.urls import path     
from . import views
urlpatterns = [
    path('show', views.index),	
    path('show/create_user',views.create_user) ,
    path('show/add_new',views.add_new,),
    path('show/<int:x>',views.show2),
    path('show/delete/<int:x>',views.delete),
    path('show/edit/<int:x>',views.edit)
    
 
]   