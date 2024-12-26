from django.urls import path
from .views import (
    home_page, shop_page, product_detail, contact_page, cart, search, wish_list, library,
    add_to_wishlibrary, wish_add_or_del, dell_from_wish,add_to_cart,dell_from_cart
)

urlpatterns = [
    path('', home_page, name='index'),
    path('shop/', shop_page, name='shop'),
    path('library/', library, name='library'),
    path('product/<int:pk>/', product_detail, name='product'),
    path('contact/', contact_page, name='contact'),
    path('cart/', cart, name='cart'),

    path('search/', search, name='search'),
    path('shop/genre/<slug:genre_name>/', shop_page, name='shop_by_genre'),
    path('shop/studio/<slug:studio_name>/', shop_page, name='shop_by_studio'),
    path('wish/<int:library_item_id>/',wish_add_or_del, name='wish_add'),
    path('wishlist/', wish_list, name='wish'),
    path('wish/add/<int:game_id>/<int:user_id>/', add_to_wishlibrary, name='add_to_wish_lib'),
    path('wish/dell/<int:library_item_id>/', dell_from_wish, name='dell_from_wish'),
    path('cart/<int:game_id>/<int:user_id>/', add_to_cart, name='cart'),
    path('cart/dell/<int:library_item_id>/', dell_from_cart, name='dell_from_cart'),
    path('cart/add/<int:game_id>/<int:user_id>/', add_to_cart, name='add_to_cart'),
]

