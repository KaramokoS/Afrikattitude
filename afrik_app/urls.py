from django.urls import path
from . import views

urlpatterns = [
    #path('', views.Accueil.as_view(), name='accueil'),
    path('',views.page_accueil_view, name='accueil'),
]
