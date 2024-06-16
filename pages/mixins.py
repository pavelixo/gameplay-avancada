from datetime import timedelta
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

class CacheMixin:
  cache_timeout = timedelta(days=1)

  @classmethod
  def as_view(cls, **initkwargs):
    view = super().as_view(**initkwargs)
    return method_decorator(cache_page(cls.cache_timeout))(view)
