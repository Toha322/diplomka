from django.urls import path
from .views import (
    home_page, shop_page,product_detail,contact_page
)
urlpatterns = [
    path('', home_page, name='index'),
    path('shop/', shop_page, name='shop'),
    path('product/', product_detail, name='product'),
    path('contact/', contact_page, name='contact'),
]