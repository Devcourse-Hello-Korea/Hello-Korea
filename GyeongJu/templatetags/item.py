from django import template
import re

register = template.Library()

@register.filter
def return_item(l):
    result = re.search('>(.*?)<', str(l))

    if result:
        extracted_string = result.group(1)
        return extracted_string
    else:
        return None

@register.filter
def return_value(l):
    result = re.search(r'"(.*?)"', str(l))

    if result:
        extracted_string = result.group(1)
        return extracted_string
    else:
        return None