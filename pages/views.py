from discord.views import DiscordView
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.utils.decorators import method_decorator


class Home(DiscordView):
  template_name = 'home.html'

  @method_decorator(cache_page(60 * 60))
  @method_decorator(vary_on_cookie)
  def get(self, request):
    context = {
      'users': self.member_service.get_members(),
      'text_channels': self.guild_service.get_channels(),
      'announcements': self.guild_service.get_announcements()
    }
    return self.render_template(request, context)