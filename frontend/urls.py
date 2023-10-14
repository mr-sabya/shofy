from django.urls import path

from .views import home, shop

urlpatterns = [
    path('', home.index, name="home"),
    path('shop', shop.index, name="shop.index"),
]
