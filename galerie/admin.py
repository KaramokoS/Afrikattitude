from django.contrib import admin
from .models import Galerie
# Register your models here.

@admin.register(Galerie)
class GalerieAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','slug','photo')
    prepopulated_fields = {'slug': ('name',)}
