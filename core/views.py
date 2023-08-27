from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .forms import ProductForm
from django.db.models import Q
from django.utils import timezone

# Create your views here.

def index(request):
    product = Product.objects.all()
    return render(request, 'index.html', {'products': product})

@csrf_exempt
def dashboard(request):
    Products = Product.objects.all()
    search_query = ""
    if request.method == "POST": 
        if "create" in request.POST:
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Product added successfully")
                return JsonResponse({'success':True})
            
    
        elif "update" in request.POST:
            id = request.POST.get("eid")
            category = request.POST.get("category")
            model_name = request.POST.get("model_name")
            brand = request.POST.get("brand")
            description = request.POST.get("description")
            color = request.POST.get("color")
            size = request.POST.get("size")
            gender = request.POST.get("gender")
            stock = request.POST.get("stock")
            price = request.POST.get("price")

            try:
                image_file = request.FILES['image']
            except KeyError:
                image_file = None

            product = Product.objects.get(pk=id)

            if image_file != None:
                product.image = image_file
            else:
                product.image = product.image

            product.category = category
            product.model_name = model_name
            product.brand = brand
            product.description = description
            product.color = color
            product.size = size
            product.gender = gender
            product.stock = stock
            product.price = price
            product.created_at = timezone.now()
            product.save()
            messages.success(request, "Product updated successfully")
            return JsonResponse({'success':True})
        elif "delete" in request.POST:
            id = request.POST.get("did")
            Product.objects.get(pk=id).delete()
            messages.success(request, "Product deleted successfully")
            return JsonResponse({'success':True})
        elif "search" in request.POST:
            search_query = request.POST.get("query")
            products = Product.objects.filter(
            Q(category__icontains=search_query) 
            | Q(model_name__icontains=search_query)
            | Q(brand__icontains=search_query)
            | Q(description__icontains=search_query)
            | Q(price__icontains=search_query)
            | Q(color__icontains=search_query)
            | Q(size__icontains=search_query)
            | Q(gender__icontains=search_query)
            | Q(stock__icontains=search_query)
            )
    return render(request, "curd.html",{"products": Products, "search_query": search_query})

def signup(request):
    return render(request, 'signup.htm')


def user(request):
    return render(request, 'user.html')

def login(request):
    return render(request, 'login.htm')

def products(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products.html', {'product':product})

def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('product_list')

@csrf_exempt
def product_list(request):
    products_data = Product.objects.all() 
    return render(request, 'products_list.html', {'products': products_data, 'form': form})


