from django.shortcuts import render

def index(request):

    receitas = {
        1: 'Lasanha',
        2: 'Sopa',
        3: 'Brigadeiro',
        4: 'Assado',
        5: 'Hamburguer',
        6: 'Parma'

    }

    dados = {
        'nome_das_receitas': receitas
    }

    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')




