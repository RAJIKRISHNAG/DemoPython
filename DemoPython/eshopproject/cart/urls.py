from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail,name= 'cart_detail'),
    path('add/<int:Product_id>/',views.add_cart, name= 'add_cart'),
    path('remove/<int:Product_id>/',views.cart_remove,name='cart_remove'),
    path('full_remove/<int:Product_id>/',views.full_remove,name='full_remove'),

]

