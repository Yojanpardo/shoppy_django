from django.shortcuts import render
from django.template import loader #importa el cargador de plntilla de django
from django.http import HttpResponse
from .models import Product


# Create your views here.

def index(request):
	product = Product.objects.order_by('id')
	template = loader.get_template('home.html')
	context = {
		'product': product
	}
	return HttpResponse(template.render(context, request))
	#return render(request, 'index.html') carga una pantilla.