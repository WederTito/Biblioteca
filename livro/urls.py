from django.urls import path

from . import views

urlpatterns = [
    path ('home/' , views.home, name = 'home'),
    path ('ver_livros/<int:id>', views.ver_livros, name ='ver_livros'),
    path ('cadastar_livro', views.cadastar_livro, name='cadastar_livro'),
    path ('excluir_livro/<int:id>', views.excluir_livro, name='excluir_livro'),
    path ('cadastar_categoria/', views.cadastar_categoria, name='cadastar_categoria'),
    path ('cadastar_emprestimo', views.cadastar_emprestimo, name='cadastar_emprestimo')
]
