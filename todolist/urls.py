from django.contrib import admin
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.home,name='home'),
    path('add', views.add,name='add'),
    path('delete/<int:id>/', views.delete,name='delete'),
    path('update/<int:id>/', views.update,name='update')
]
