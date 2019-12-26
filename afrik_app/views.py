from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView
from .forms import CommentsForm

# Create your views here.

class Accueil(TemplateView):
    template_name = 'afrik_app/page_accueil.html'

def page_accueil_view(request):

    new_comment = None

    if request.method == 'POST':

        comment_form = CommentsForm(data=request.POST)

        if comment_form.is_valid():
             new_comment = comment_form.save()
    else:
        comment_form = CommentsForm()

    return render(request,'afrik_app/page_accueil.html',{'new_comment': new_comment,
                                                         'comment_form': comment_form})
