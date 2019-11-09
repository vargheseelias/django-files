from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.gethome,name='home'),
    path('register', views.getregister, name='register'),
    path('register', views.insertvalues, name='insert'),
    path('view', views.getview, name='view'),

]