from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_view, name='about'),
    path('blog_detail/', views.blog_detail_view, name='blog_detail'),
    path('blog_list/', views.blog_list_view, name='blog_list'),
    path('cart/', views.cart_view, name='cart'),
    path('category/', views.category_view, name='category'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('coming-soon/', views.coming_soon_view, name='coming_soon'),
    path('contact/', views.contact_view, name='contact'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('faq/', views.faq_view, name='faq'),
    path('login/', views.login_view, name='login'),
    path('product-detail/', views.product_detail_view, name='product_detail'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
]
