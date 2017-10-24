from django.shortcuts import render, get_object_or_404
from django.template import loader #importa el cargador de plntilla de django
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

def all_products(request):
	title = 'Productos'
	product = Product.objects.order_by('id')
	template = loader.get_template('productos/products.html')
	context = {
		'title': title,
		'product': product
	}
	return HttpResponse(template.render(context, request))
	#return render(request, 'index.html') carga una pantilla.


def product_detail(request, pk):
	product = get_object_or_404(Product, pk=pk)
	template = loader.get_template('productos/product_detail.html')
	context = {
		'product': product
	}
	return HttpResponse(template.render(context, request))

def new_product(request):
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			product = form.save()
			product.save()
			return HttpResponseRedirect('/products')
	else:
		form = ProductForm()
	template = loader.get_template('productos/new_product.html')
	context = {
		'form':form
	}
	return HttpResponse(template.render(context, request))