from django.urls import path
from . import views

urlpatterns = [
    path('', views.cve_search, name='cve'),
    path('cve/product/', views.cve_product, name='cve_product'),
    path('cve/last/', views.cve_last_30, name='cve_last_30')
]