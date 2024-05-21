from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('/wall/<int:x>',views.create_message),	  
    path('/show',views.wall),
    path('/create_comment/<int:x>/<int:w>',views.create_comment)
]   