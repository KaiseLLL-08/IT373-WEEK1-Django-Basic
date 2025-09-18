from django.urls import path
from pages import views
urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.hello, name='hello'),
    path('about/', views.about,  name='about'),
    
]