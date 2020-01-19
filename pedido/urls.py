from django.urls import path
from .views import Pagar, FecharPedido, Detalhe

app_name = 'pedido'

urlpatterns = [
    path('', Pagar.as_view(), name='pagar'),
    path('fechar-pedido/', FecharPedido.as_view(), name='fechar-pedido'),
    path('detalhe/', Detalhe.as_view(), name='detalhe'),

]