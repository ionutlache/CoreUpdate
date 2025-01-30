from django.urls import path

from cart import views


urlpatterns = [
    path('cart/', views.cart_summary, name='cart_summary' ),
    path('add_cart/', views.cart_add, name='cart_add' ),
    path('delete_cart/', views.cart_delete, name='cart_delete' ),
    path('update_cart/', views.cart_update, name='cart_update' ),
    path('checkout/', views.checkout, name='checkout' ),
]