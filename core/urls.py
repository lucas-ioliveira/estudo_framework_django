from django.urls import path
from .views import index, contato

# É necessário ser ciada uma variável igual no arquivo urls principal

urlpatterns = [
    path('', index),
    path('contato', contato)
]