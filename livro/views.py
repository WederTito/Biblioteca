from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render
from usuarios.models import Usuario

from .forms import CadastroLivro
from .models import Categoria, Emprestimos, Livros


def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter(usuario = usuario)
        form = CadastroLivro()
        form.fields['usuario'].initial = request.session['usuario']
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)

        return render(request, 'home.html', {'livros': livros, 'usuario_logado': request.session.get('usuario'), 'form': form})
    else:
        return redirect('/auth/login/?status=2')

def ver_livros(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id=id)
        if request.session.get('usuario') == livros.usuario.id:
            usuario = Usuario.objects.get(id = request.session['usuario'])
            categoria_livro = Categoria.objects.filter(usuario = request.session.get('usuario'))
            emprestimos = Emprestimos.objects.filter(livro = livros)
            form = CadastroLivro()
            form.fields['usuario'].initial = request.session['usuario']
            form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
            return render(request, 'ver_livro.html', {'livro': livros, 'categoria_livro': categoria_livro, 'emprestimos': emprestimos,
            'usuario_logado': request.session.get('usuario'), 'form': form})
        else:
            return
    return redirect('/auth/login/?status=2')

def cadastar_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST)
        
        if form.is_valid:
            form.save()
            return redirect('/livro/home')
        else:
            return HttpResponse('Dados invalidos')
