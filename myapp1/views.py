from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# from rest_framework.views import APIView
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password,make_password
from .models import *
# Create your views here.


# @login_required(login_url='myapp1:login')
def home(request):
    return render(request,'myapp1/home.html')

def dashboard(request):
    return render(request,'myapp1/dashboard.html')   

def enquiry(request):
    return render(request,'myapp1/enquiry.html')

def about(request):
    return render(request,'myapp1/about.html')

def contactus(request):
    return render(request,'myapp1/contactus.html')

def shop(request):
    return render(request,'myapp1/store.html')

def enquiry(request):
    if request.user.is_authenticated:
        return redirect('myapp1:home') 
    else: 
        if request.method=='POST':
            form=ProfileRegisterForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('myapp1:login')
        f=ProfileRegisterForm()
        return render(request,'myapp1/enquiry.html',context={'customerform':f})

# def loginPage(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#        if request.method=="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user=authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('/')
#        context={}
#        return render(request,'myapp1/login.html',context)


def login_view(request):
    if request.method=='POST':
        form=loginForm(request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user:
                login(request,user)
                return redirect(reverse('myapp1:home'))
            else:
                messages.info(request,'Username or password is not valid')
                return redirect('myapp1:login')
    f=loginForm()
    return render(request,'myapp1/login.html',context={'form':f})        

def logout_view(request):
    logout(request)
    return redirect(reverse('myapp1:login')) 

def profile(request):
    profile =ProfileModel.objects.all()
    return render(request, 'myapp1/profile.html', {'profile': profile})

def profile_view(request, pk):
    profile =ProfileModel.objects.get(pk=pk)
    return render(request, 'myapp1/profile_view.html', {'profile': profile})


def store(request):
    return render(request,'myapp1/store.html')
	
def formals(request):
    products=FormalModel.objects.all()
    context={'products':products}
    return render(request,'myapp1/formals.html',context)
    
	
def tshirts(request):
    products=TshirtsModel.objects.all()
    context={'products':products}
    return render(request,'myapp1/tshirts.html',context)
	
def suits(request):
    products=SuitsModel.objects.all()
    context={'products':products}
    return render(request,'myapp1/suits.html',context)
	
def kurtas(request):
    products=KurtasModel.objects.all()
    context={'products':products}
    return render(request,'myapp1/kurtas.html',context)
	
def tops(request):
    products=TopsModel.objects.all()
    context={'products':products}
    return render(request,'myapp1/tops.html',context)
	

def cart(request):
	context={}
	return render(request, 'myapp1/cart.html', context)

def formals_product_detail(request, pk):
    product =FormalModel.objects.get(pk=pk)
    return render(request, 'myapp1/formals_view.html', {'product': product})

def tshirts_product_detail(request, pk):
    product =TshirtsModel.objects.get(pk=pk)
    return render(request, 'myapp1/tshirts_view.html', {'product': product})

def suits_product_detail(request, pk):
    product =SuitsModel.objects.get(pk=pk)
    return render(request, 'myapp1/suits_view.html', {'product': product})

def tops_product_detail(request, pk):
    product =TopsModel.objects.get(pk=pk)
    return render(request, 'myapp1/tops_view.html', {'product': product})

def kurtas_product_detail(request, pk):
    product =KurtasModel.objects.get(pk=pk)
    return render(request, 'myapp1/kurtas_view.html', {'product': product})

# def view_cart(request):
#     cart_items = CartItem.objects.filter(user=request.user)
#     total_price = sum(item.product.prize * item.quantity for item in cart_items)
#     return render(request, 'myapp1/cart1.html', {'cart_items': cart_items, 'total_price': total_price})
 
def add_to_cart(request, product_id):
    product = FormalModel.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product,user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('myapp1:view_cart')
 
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('myapp1:view_cart')


@login_required(login_url='myapp1/login')
def view_cart(request):
    # cart = request.user.cart
    cart_items = CartItem.objects.all()
    return render(request, 'myapp1/orders.html', {'orders': cart_items})