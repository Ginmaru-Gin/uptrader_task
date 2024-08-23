from django import template

register = template.Library()

@register.filter
def get_item(dictionary, item):
    return dictionary.get(item ,None)
