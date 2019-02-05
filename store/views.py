from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views.generic import DetailView, FormView, ListView
from django.views.generic.edit import CreateView, DeleteView


from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Product, Customers
from .forms import ProductBuyForm
from .serializers import ProductSerializer


def index(request):
    return render(request, 'store/index.html')


def success(request):
    return render(request, 'store/success.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'store/signup.html', {'form': form})


class ProductList(ListView):
    model = Product
    template_name = 'store/product_list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        if self.kwargs.get('slug') == 'Products':
            context['products'] = Product.objects.all
            return context
        else:
            context['products'] = Product.objects.filter(manufacturer=self.kwargs.get('slug'))
            return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'store/product_detail.html'


class ProductAdd(CreateView):
    model = Product
    fields = ['name', 'manufacturer', 'price', 'image']


class ProductBuy(FormView):
    model = Customers
    form_class = ProductBuyForm
    template_name = 'store/product_buy.html'
    success_url = reverse_lazy('success')

    def get_context_data(self, **kwargs):
        context = super(ProductBuy, self).get_context_data(**kwargs)
        start = self.request.path.find('buy/') + 4
        prod_name = self.request.path[start:-1]
        prod = Product.objects.get(name=prod_name)
        context['prod_name'] = prod.name
        context['prod_manufacturer'] = prod.manufacturer
        context['prod_price'] = prod.price
        context['prod_image'] = prod.image
        return context

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        context = self.get_context_data()

        customer = Customers()
        customer.name = context['form']['first_name'].data
        customer.manufacturer = context['form']['middle_name'].data
        customer.price = context['form']['last_name'].data
        customer.image = context['form']['phone_number'].data
        customer.save()

        return HttpResponseRedirect(self.get_success_url())


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products-list')


@api_view(['GET', 'POST'])
@authentication_classes((TokenAuthentication, BasicAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticated,))
def products(request):
    prods = Product.objects.all()
    serializer = ProductSerializer(prods, many=True)
    return Response(serializer.data)




