from django.shortcuts import render

# Create your views here.

# Index (Exemplo)
def index(request):
    context = {
        'Curso': 'Programação web com Django framework'
    }
    return render(request, 'index.html', context)

# Exemplo 2
def contato(request):
    return render(request, 'contato.html')