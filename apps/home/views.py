from django.shortcuts import render

def home_page(request):
    return render(request,'home/index.html')

def shop_page(request):
    return render(request,'home/shop.html')

def product_detail(request):
    return render(request,'home/product_detail.html')

def contact_page(request):
    return render(request,'home/contact.html')
