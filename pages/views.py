from discord.views import DiscordView

from django.shortcuts import redirect
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.utils.decorators import method_decorator
from django.conf import settings

class Home(DiscordView):
  template_name = 'home.html'


  @method_decorator(cache_page(60 * 60))
  @method_decorator(vary_on_cookie)
  def get(self, request):
    users = self.member_service.get_members()
    text_channels = self.guild_service.get_channels()
    announcements = self.guild_service.get_channel_messages(settings.ANNOUNCEMENTS_ID, limit=1)
    return self.render_template(
      request, { 'users': users, 'announcements': announcements,'text_channels': text_channels }
    )


class AnonymousMessage(DiscordView):
  template_name = 'anonymous_message.html'


  @method_decorator(cache_page(60 * 10))
  @method_decorator(vary_on_cookie)
  def get(self, request, channel_id):    
    channel = self.guild_service.get_channel(channel_id)
    channel_messages = self.guild_service.get_channel_messages(channel_id, limit=64)

    if not channel and not channel_messages:
      return redirect('home-view')
    
    if channel['nsfw']:
      return redirect('home-view')
    
    return self.render_template(
      request, { 'channel': channel, 'channel_messages': reversed(channel_messages) }
    )
