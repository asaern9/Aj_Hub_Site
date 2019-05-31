from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'hub/home.html')


def Atech(request):
    return render(request, 'hub/Atech.html')


def Adesign(request):
    return render(request, 'hub/Adesign.html')


def AkeySolution(request):
    return render(request, 'hub/AkeySolution.html')


def portfolio(request):
    return render(request, 'hub/portfolio.html')


def about(request):
    return render(request, 'hub/about.html')


def contact(request):
    return render(request, 'hub/contact.html')


