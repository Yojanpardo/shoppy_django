from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='hello'),
	url(r'^products/', views.ProductList.as_view(), name='all_products'),
	url(r'^product/(?P<pk>[0-9]+)/$',views.ProductDetail.as_view(), name='product_detail'),
	url(r'^new_product/', views.new_product, name='new_product'),
] 