from django.urls import path, include
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.hello, name='hello'),
    path('about/', views.about,  name='about'),
    path('library/', include('library.urls')),
]