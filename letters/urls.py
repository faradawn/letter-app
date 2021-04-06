from django.urls import path

from . import views

urlpatterns = [
    path('', views.letter_home, name='letter_home'),
]