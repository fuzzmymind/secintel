from django.urls import path
from . import views

urlpatterns = [
    path('', views.url_home, name='url_home'),
    path('url/', views.url_analyze, name='url_analyze'),
    path('domain/', views.domain_analyze, name='domain_analyze')
]