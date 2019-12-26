from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', views.Accueil.as_view(), name='accueil'),
    path('',views.page_accueil_view, name='accueil'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
