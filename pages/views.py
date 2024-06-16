from datetime import timedelta as time
from discord.views import DiscordView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class Home(DiscordView):
  template_name = 'home.html'

  @method_decorator(cache_page(time(hours=16)))
  def dispatch(self, *args, **kwargs):
      return super().dispatch(*args, **kwargs)

  def get(self, request):
    context = {
      'users': self.member_service.get_members(),
    }
    return self.render_template(request, context)