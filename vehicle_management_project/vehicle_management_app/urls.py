from . import views
from django.urls import path
from .views import vehicle_list, add_vehicle, edit_vehicle, delete_vehicle

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('list/', vehicle_list, name='vehicle_list'),
    path('add/', add_vehicle, name='add_vehicle'),
    path('edit/<int:pk>/', edit_vehicle, name='edit_vehicle'),
    path('delete/<int:pk>/', delete_vehicle, name='delete_vehicle'),
    path('logout/',views.logout_view,name='logout'),
]