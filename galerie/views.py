from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import MultipleObjectMixin

from .models import Galerie


class GalerieListView(ListView):
    model = Galerie
    paginate_by = 8
    template_name = 'galerie/galerie_list.html'


class GalerieDetailView(DetailView,MultipleObjectMixin):
    model = Galerie
    paginate_by = 1
    template_name = 'galerie/galerie_detail.html'
    def get_context_data(self, **kwargs):
        object_list = Galerie.objects.filter()
        context = super(GalerieDetailView, self).get_context_data(object_list=object_list, **kwargs)
        return context



def galerie_list(request):
    object_list = Galerie.objects.all()

    paginator = Paginator(object_list, 8)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'galerie/galerie_list.html',
                  {'page': page,
                   'posts': posts})
