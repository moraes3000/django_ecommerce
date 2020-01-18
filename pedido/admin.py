from django.contrib import admin
from .models import itemPedido,Pedido


class ItemPedidoInline(admin.TabularInline):
    model = itemPedido
    extra = 1


class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItemPedidoInline
    ]


admin.site.register(Pedido, PedidoAdmin)
admin.site.register(itemPedido)