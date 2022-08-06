from django.contrib import admin

from .models import Emprestimos, Livros, Categoria

admin.site.register(Livros)
admin.site.register(Categoria)
admin.site.register(Emprestimos)
