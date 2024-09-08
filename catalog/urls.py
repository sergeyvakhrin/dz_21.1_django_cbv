from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import product_list, contact_list, product_detail, contact_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('', product_list, name='product_list'),
    path('contacts/', contact_list, name='contacts'),
    path('products/<int:pk>', product_detail, name='product_detail'),
    path('contacts/<int:pk>', contact_detail, name='contact_detail'),
]