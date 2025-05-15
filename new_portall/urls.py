from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('new.urls')),
    path('user_app/', include('user_app.urls')),
]
