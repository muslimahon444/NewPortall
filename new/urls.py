from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/<int:pk>/', views.bod, name='bod'),
    # path('news/create/', views.bod, name='news_create'),
    # path('news/<int:pk>/delete/', views.news_delete, name='news_delete'),
    # path('news/<int:pk>/edit/', views.bod, name='news_edit'),
    # path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('register/', views.register_view, name='register'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)