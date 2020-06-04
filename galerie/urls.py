from django.urls import path
from .views import GalerieListView, GalerieDetailView,galerie_list
from django.conf import settings
from django.conf.urls.static import static

app_name = "galerie"
urlpatterns = [
    path('<slug:slug>', GalerieDetailView.as_view(), name='galerie_detail'),
    path('', GalerieListView.as_view(), name='galerie_list_view'),
    #path('', galerie_list, name='galerie_list_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
