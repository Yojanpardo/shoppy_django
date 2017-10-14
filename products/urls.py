from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='hello'),
	url(r'^products/', views.all_products, name='all_products'),
	url(r'^product/(?P<pk>[0-9]+)/$',views.product_detail, name='product_detail'),
	url(r'^new_product/', views.new_product, name='new_product'),
]