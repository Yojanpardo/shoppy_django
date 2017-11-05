from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader #importa el cargador de plntilla de django

from django.views.generic import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect
from .models import Product
from .forms import ProductForm


# Create your views here.

def index(request):
	title = 'Shoppy django'
	template = loader.get_template('home.html')
	context = {
		'title': title
	}
	return HttpResponse(template.render(context, request))


class ProductList(ListView):
	model = Product

class ProductDetail(DetailView):
	model = Product

def new_product(request):
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			product = form.save()
			product.save()
			return HttpResponseRedirect('/products')
	else:
		form = ProductForm()
	template = loader.get_template('products/new_product.html')
	context = {
		'form':form
	}
	return HttpResponse(template.render(context, request))

def  auth_login(request):
	if request.method == 'POST':
		action = request.POST.get('action', None)
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
	
		if action == 'signup':
			user=User.objects.create_user(username=username,
				                          password=password)
			user.save()
		elif action=='login':
			user = authenticate(username=username, password=password)
			login(request,user)
			return redirect('/')
		
	context = {}
	return render(request, 'login/login.html',context)


#def all_products(request):
#	title = 'Productos'
#	product = Product.objects.order_by('id')
#	template = loader.get_template('products/products.html')
#	context = {
#		'title': title,
#		'product': product
#	}
#		return HttpResponse(template.render(context, request))
	#return render(request, 'index.html') carga una pantilla.


#def product_detail(request, pk):
#	product = get_object_or_404(Product, pk=pk)
#	template = loader.get_template('products/product_detail.html')
#	context = {
#		'product': product
#	}
#	return HttpResponse(template.render(context, request))