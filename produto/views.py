from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from . import models
from django.contrib import messages


# Create your views here.

class ListaProdutos(ListView):
    model = models.Produto
    context_object_name = 'produtos'
    paginate_by = 2


class DetalheProdutos(DetailView):
    model = models.Produto
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'


class AddCarrinho(View):
    def get(self, *args, **kwargs):
        # redireciona na ultima pagina acessada (link externo joga para o site externo)
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista')
        )
        #caso esteja em uma url divergent
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            messages.error(
                self.request,
                'Produto não existe'
            )
            return redirect(http_referer)
        variacao =  get_object_or_404(models.Variacao, id=variacao_id)
        # inicio da sessao
        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()

        carrinho = self.request.session['carrinho']

        if variacao_id in carrinho:
            # TODO: variacao existe no carrinho
            pass
        else:
            # TODO: não existe no carrinho
            pass
        return HttpResponse(f'{variacao.produto} {variacao.nome}')

class RemoverCarrinho(View):
    pass


class Carrinho(View):
    pass


class Finalizar(View):
    pass
