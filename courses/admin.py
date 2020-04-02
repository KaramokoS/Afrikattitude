from django.contrib import admin
from .models import Course, Subject


# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    prepopulated_fields = {'slug': ('title',)}
