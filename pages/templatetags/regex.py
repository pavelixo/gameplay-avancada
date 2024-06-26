import re
from typing import Any
from django import template

register = template.Library()

@register.filter(name='is_single_url')
def is_single_url(value):
    url_pattern = re.compile(
        r'^(?:http|https)://'  # http | https
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # Domain
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # IPV4 
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # IPV6
        r'(?::\d+)?'  # Ports
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    return bool(re.fullmatch(url_pattern, value))

@register.filter(name='is_image_url')
def is_image_url(value: Any) -> bool:
    url = value.split('?')[0]
    image_extensions = r'\.(jpg|jpeg|png|gif|bmp|svg)$'
    return bool(re.search(image_extensions, url, re.IGNORECASE))

@register.filter(name='is_video_url')
def is_video_url(value: Any) -> bool:
    url = value.split('?')[0]
    video_extensions = r'\.(mp4|avi|mov|wmv|flv|mkv|webm)$'
    return bool(re.search(video_extensions, url, re.IGNORECASE))

@register.filter(name='mention')
def mention(value: Any, arg: Any):
    mention_pattern = r"<@([^>]+)>"

    users = {user['id']: user['username'] for user in arg}

    def mention_replace(match):
        user_id = match.group(1)

        return f"@{users.get(user_id, match.group(0))}"

    return re.sub(mention_pattern, mention_replace, value)