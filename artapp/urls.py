from django.urls import path
from . import views
from .views import gallery_view

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('artwork/', gallery_view, name='artwork'),
    path('contact/', views.contact, name='contact')
]