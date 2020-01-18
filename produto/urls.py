from django.urls import path
from .views import ListaProdutos, DetalheProdutos, AddCarrinho, RemoverCarrinho, Carrinho, Finalizar

app_name = 'produto'
urlpatterns = [
    path('', ListaProdutos.as_view(), name='lista'),
    path('<slug>', DetalheProdutos.as_view(), name='detalhe'),
    path('<add-carrinho>', AddCarrinho.as_view(), name='add-carrinho'),
    path('remover-carrinho/', RemoverCarrinho.as_view(), name='remover-carrinho'),
    path('carrinho/', Carrinho.as_view(), name='carrinho'),
    path('finalizar/', Finalizar.as_view(), name='finalizar'),

]
