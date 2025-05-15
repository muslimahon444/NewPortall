from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    path('', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login, name='login'),
]