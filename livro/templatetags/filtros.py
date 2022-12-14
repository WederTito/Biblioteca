from atexit import register
from datetime import datetime

from django import template

register = template.Library()

@register.filter
def mostra_duracao(value1, value2):
    if all((isinstance(value1, datetime), isinstance(value2, datetime))):
        dias = (value1 - value2).days
        texto = 'Dias'
        if dias == 1:
            texto = 'Dia'

        return f"{dias} {texto}."

    return "Ainda não foi devolvido!"
