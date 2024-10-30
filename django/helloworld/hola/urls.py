from django.urls import path
from .views import homePage, contactPage, aboutPage

urlpatterns = [
    path('', homePage, name="home"),
    path('contact/', contactPage, name="contact"),
    path('about/', aboutPage, name="about"),
]

# 127.0.0.1:8000/contact -> contact