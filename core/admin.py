from django.contrib import admin
from .models import Produto, Cliente

# Register your models here.
# Para uma melhor visualização em adm do django


class Produto_adm(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClienteAdm(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


admin.site.register(Produto, Produto_adm)
admin.site.register(Cliente, ClienteAdm)
