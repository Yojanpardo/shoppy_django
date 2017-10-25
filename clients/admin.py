from django.contrib import admin
from .models import Client

# Register your models here.

@admin.register(Client)
class AdminClient(admin.ModelAdmin):
	list_display=('first_name','last_name','gender','cedula','cellphone','email','birthday',)
	list_filter=('gender',)