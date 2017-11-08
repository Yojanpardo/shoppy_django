from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
	url(r'^accounts/login/$', views.auth_login, name='auth_login'),
	url(r'^accounts/signup/$', views.auth_signup, name='auth_signup'),
	url(r'^logout$', auth_views.logout, {'next_page':'/'}, name='logout'),
	url(r'^$', views.index, name='hello'),
	url(r'^products/', views.ProductList.as_view(), name='all_products'),
	url(r'^product/(?P<pk>[0-9]+)/$',views.ProductDetail.as_view(), name='product_detail'),
	url(r'^new_product/', views.new_product, name='new_product'),
] 