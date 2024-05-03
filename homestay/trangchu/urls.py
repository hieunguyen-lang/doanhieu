from django.urls import path

from .import views
urlpatterns =[
    path('home/',views.home),
    path('filter/', views.address_filter, name="address_filter"),
    path('cart/',views.cart, name="cart"),
    path('add/', views.cart_add, name="cart_add"),
    path('update/', views.cart_select_update, name ="cart_select_update"),
    path('delete/', views.cart_delete, name = "cart_delete" ),
    path('preview/<int:id>', views.xemphong, name="xemphong"),
    path('blog/', views.blog)
]