from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter
def replace_decimal_amount(value):
    if value:
        value_split = value.split(",")
        if int(value_split[1]) == 0:
            value_replace = value.replace(",",".")
            value = int(float(value_replace))
            
        # print("value:",value)
        # print('value_split:', value_split)
    
    return mark_safe(value)