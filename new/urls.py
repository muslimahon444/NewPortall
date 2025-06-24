from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import reverse





app_name = 'new'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('create_news/', views.create_news, name='create_news'),
    path('update/<int:pk>', views.NewsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.NewsDeleteView.as_view(), name='delete_news'),
    path('detail/<int:pk>/', views.news_detail_view, name='detail'),
     path('result_serch/', views.result_serch, name='result_serch'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)