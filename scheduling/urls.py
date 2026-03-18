from django.urls import path
from . import views

urlpatterns = [
    path('', views.choose_creature, name='choose_creature'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('slot/<int:creature_id>/', views.choose_slot, name='choose_slot'),
    path('confirm/<int:creature_id>/<int:slot_id>/', views.confirm_booking, name='confirm_booking'),
    path('success/', views.booking_success, name='booking_success'),
    path('my-booking/', views.my_booking, name='my_booking'),
]
