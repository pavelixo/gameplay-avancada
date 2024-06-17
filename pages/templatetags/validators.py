from typing import Any
from django import template

register = template.Library()

@register.filter(name='validate_content_length')
def validate_content_length(value: Any) -> str:
    if len(value) > 32:
        return f'{value[:29]}...'
    return value
