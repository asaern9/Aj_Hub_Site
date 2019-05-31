from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='hub-home'),
    path('about/', views.about, name='hub-about'),
    path('adesign/', views.Adesign, name='Adesign'),
    path('atech/', views.Atech, name='Atech'),
    path('akeySolution/', views.AkeySolution, name='AkeySolution'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
]