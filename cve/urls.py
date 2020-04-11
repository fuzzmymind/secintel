from django.urls import path
from . import views

urlpatterns = [
    path('', views.cve_search, name='cve'),
    path('cve/product/', views.cve_product, name='cve_product'),
    path('cve/getproducts', views.get_product_for_vendor, name='get_product_for_vendor'),
    path('cve/getcvebyproduct', views.get_cve_product_vendor, name='get_cve_product_vendor'),
    path('cve/last/', views.cve_last_30, name='cve_last_30')
]