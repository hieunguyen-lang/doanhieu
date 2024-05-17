from django.urls import path

from .import views 
from .views import *
urlpatterns =[
    path('home/',views.home, name='home'),
    path('Home_Update_Search/',views.Home_Update_Search, name='Home_Update_Search'),
    path('getdate/', views.home, name='getdate'),
    path('search/', views.search, name='search'),
    path('filter', roomapiview.as_view() ),
    path('filter/roomid', roomid.as_view() ),
    path('cart/',views.cart, name="cart"),
    path('checkout/<int:phong_id>/', views.checkout, name='checkout'),
    path('billinginfo/<int:id>', views.billinginfo, name='billinginfo'),
    path('add/', views.cart_add, name="cart_add"),
    path('update/', views.cart_select_update, name ="cart_select_update"),
    path('delete/', views.cart_delete, name = "cart_delete" ),
    path('preview/<int:id>', views.xemphong, name="xemphong"),
    path('previewupdate/', views.PreviewUpdate, name="PreviewUpdate"),
    path('blog/', views.blog)
]