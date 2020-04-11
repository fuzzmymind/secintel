from django.urls import path
from . import views

urlpatterns = [
    path('', views.url_home, name='url_home'),
    path('analyze/', views.url_analyze, name='url_analyze'),
]