from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class':arg})

@register.filter(name='add_style')
def add_style(value, arg):
    return value.as_widget(attrs={'style':arg})