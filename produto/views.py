from django.shortcuts import render
from django.views.generic.list import  ListView
from django.views.generic.detail import DetailView
from django.views import View
from .models import Produto, Variacao
# Create your views here.

class ListaProdutos(ListView):
    model = Produto
    context_object_name = 'produtos'
    paginate_by = 2



class DetalheProdutos(DetailView):
    model = Produto
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'

class AddCarrinho(View):
    pass

class RemoverCarrinho(View):
    pass

class Carrinho(View):
    pass

class Finalizar(View):
    pass