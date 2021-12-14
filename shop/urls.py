from django.urls import path
from shop.views import index, detail, checkout, confirmation, Boisson, Accompagnement, Hamburger, Dessert

urlpatterns = [
    path('', index, name='home'),
    path('Hamburger', Hamburger, name='Hamburger'),
    path('Boisson', Boisson, name='Boisson'),
    path('Accompagnement', Accompagnement, name='Accompagnement'),
    path('Dessert', Dessert, name='Dessert'),
    path('<int:myid>', detail, name="detail"),
    path('checkout', checkout, name="checkout"),
    path('confirmation', confirmation, name="confirmation"),

]