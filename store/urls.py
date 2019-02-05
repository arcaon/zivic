from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from store import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'success/$', views.success, name='success'),

    url(r'^login/', auth_views.login, {'template_name': 'store/login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/', views.signup, name='signup'),

    url(r'products/(?P<slug>[-\w]+)/$', views.ProductList.as_view(), name='products-list'),
    url(r'product/add/$', views.ProductAdd.as_view(), name='product-add'),
    url(r'product/(?P<pk>[0-9]+)$', views.ProductDetail.as_view(), name='product-detail'),
    url(r'product/buy/(?P<pk>[\w.@+-]+)/$', views.ProductBuy.as_view(), name='product-buy'),
    url(r'product/(?P<pk>[0-9]+)/delete/$', views.ProductDelete.as_view(), name='product-delete'),

    url(r'api/products/$', views.products),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

