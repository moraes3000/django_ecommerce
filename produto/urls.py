from django.urls import path
from .views import ListaProdutos, DetalheProdutos, AddCarrinho, RemoverCarrinho, Carrinho, ResumoDaCompra, Busca

app_name = 'produto'
urlpatterns = [
    path('', ListaProdutos.as_view(), name='lista'),
    path('<slug>', DetalheProdutos.as_view(), name='detalhe'),
    path('add-carrinho/', AddCarrinho.as_view(), name='add-carrinho'),
    path('remover-carrinho/', RemoverCarrinho.as_view(), name='remover-carrinho'),
    path('carrinho/', Carrinho.as_view(), name='carrinho'),
    path('resumodacompra/', ResumoDaCompra.as_view(), name="resumodacompra"),

    path('busca/', Busca.as_view(), name="busca"),

]
