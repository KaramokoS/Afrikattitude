from django.urls import path
from dakuoblog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('oeuvres/', views.oeuvres, name='oeuvres'),
    path('exposition/', views.expo, name='expo'),
    path('contact/', views.contact, name='contacte'),
    path('apropos/', views.apropos, name='about')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
