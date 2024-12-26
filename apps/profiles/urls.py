from django.urls import path

from .views import (
    profile_page,
    login_view,
    registration_view,
    user_logout,

)

urlpatterns = [
    path('', profile_page, name='profile'),
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
    path('logout/', user_logout, name='logout'),
]