from django.urls import path
from . import views

urlpatterns = [
    path('', views.choose_creature, name='choose_creature'),
    path('slot/<int:creature_id>/', views.choose_slot, name='choose_slot'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
