from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'dakuoblog/base.html', {})

def oeuvres(request):
    return render(request, 'dakuoblog/oeuvres.html', {})


def expo(request):
    return render(request, 'dakuoblog/expositions.html', {})

def contact(request):
    return render(request, 'dakuoblog/contact.html', {})

def apropos(request):
    return render(request, 'dakuoblog/apropos.html', {})
