from django.shortcuts import redirect

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
      # 'announcements': self.guild_service.get_announcements()
    }
    return self.render_template(request, context)


class AnonymousMessage(DiscordView):
  template_name = 'anonymous_message.html'

  @method_decorator(cache_page(60 * 10))
  @method_decorator(vary_on_cookie)
  def get(self, request, channel_id):
    if not channel_id:
      redirect('home-view')

    try:
      context = {
        'channel_messages': self.guild_service.get_channel_messages(channel_id)
      }
      return self.render_template(request, context)
    except TypeError:
      return redirect('home-view')
  