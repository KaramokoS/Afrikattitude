from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Course


class CourseDetailView(DetailView):
    template_name  = "courses.detail.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Course.objects.all()



class CourseListView(ListView):
    template_name   = "courses/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Course.objects.all()
