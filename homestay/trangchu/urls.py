from django.urls import path

from .import views
urlpatterns =[
    path('home/',views.home),
    path('cart/',views.cart),
    path('add/', views.cart_add, name="cart_add"),
    path('update/', views.cart_select_update, name ="cart_select_update"),
    path('preview/<int:id>', views.xemphong, name="xemphong"),
    path('blog/', views.blog)
]