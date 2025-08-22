from django.shortcuts import render

def about_view(request):
    return render(request, 'about.html')

def blog_detail_view(request):
    return render(request, 'blog-detail.html')

def blog_list_view(request):
    return render(request, 'blog-list.html')

def cart_view(request):
    return render(request, 'cart.html')

def category_view(request):
    return render(request, 'category.html')

def checkout_view(request):
    return render(request, 'checkout.html')

def coming_soon_view(request):
    return render(request, 'coming-soon.html')

def contact_view(request):
    return render(request, 'contact.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def faq_view(request):
    return render(request, 'faq.html')

def login_view(request):
    return render(request, 'login.html')

def product_detail_view(request):
    return render(request, 'product-detail.html')

def wishlist_view(request):
    return render(request, 'wishlist.html')

def error_404_view(request, exception=None):
    return render(request, '404.html', status=404)
