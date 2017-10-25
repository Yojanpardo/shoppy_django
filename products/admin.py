from django.contrib import admin
from .models import Product, Favorite

# Register your models here.

#admin.site.register(Product)
@admin.register(Product) #esto se llama un decorador 
class AdminProduct(admin.ModelAdmin): #creamos la clase que va a contener los datos que queremos mostrar
	list_display=('name','category','price',)#indicamos los datos que queremos que se muestren
	list_filter=('category',)#nos da la opcion de filtrar nuestros productos de la forma que queramos, nombre, categoria, etc.
	
@admin.register(Favorite)
class AdminFavorite(admin.ModelAdmin):
	list_display = ('user','product',)
	list_filter = ( 'user', 'product',)