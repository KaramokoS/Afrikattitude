from django.contrib import admin
from .models import Commentaire

# Register your models here.

@admin.register(Commentaire)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('Nom', 'email', 'created')
    list_filter = ('active', 'created')
    search_fields = ('Nom', 'email', 'Message')
