from django.urls import path
from . import views

app_name='myapp1'



urlpatterns = [
    path('home/',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('contactus/',views.contactus, name='contactus'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('enquiry/',views.enquiry, name='enquiry'),
    path('shop/',views.shop, name='shop'),
    path('profile/',views.profile, name='profile'),
    path('profile_view<int:pk>/',views.profile_view, name='profile_view'),
    path('login/', views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('view_cart/',views.view_cart,name='view_cart'),
    path('formals/', views.formals, name="formals"),
    path('tshirts/', views.tshirts, name="tshirts"),
    path('suits/', views.suits, name="suits"),
    path('kurtas/', views.kurtas, name="kurtas"),
    path('tops/', views.tops, name="tops"),
    path('customer/', views.tops, name="tops"),
    path('formals_product_detail<int:pk>/', views.formals_product_detail, name='formals_product_detail'),
    path('tshirts_product_detail<int:pk>/', views.tshirts_product_detail, name='tshirts_product_detail'),
    path('suits_product_detail<int:pk>/', views.suits_product_detail, name='suits_product_detail'),
    path('tops_product_detail<int:pk>/', views.tops_product_detail, name='tops_product_detail'),
    path('kurtas_product_detail<int:pk>/', views.kurtas_product_detail, name='kurtas_product_detail'),
    # path('profile/', views.myprofile, name="profile"),

    # path('products/',views.products, name='products'),
   
]

