from django.urls import path
from . import views

urlpatterns = [
    path('', views.library_list, name='library_list'),
    path('create/', views.library_create, name='library_create'),
    path('edit/<int:id>/', views.library_edit, name='library_edit'),  
    path('delete/<int:id>/', views.library_delete, name='library_delete'),
]




