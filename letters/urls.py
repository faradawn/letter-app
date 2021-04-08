from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/result/', views.result, name='result'),
]