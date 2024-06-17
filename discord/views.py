from django.views import View
from django.http import HttpResponse, HttpRequest
from django.views.generic.base import ContextMixin
from django.shortcuts import render
from django.conf import settings

from .config import DiscordConfig
from .user_services import DiscordUserService, AvatarProcessor, MemberService
from .user_interface import IUserService, IAvatarProcessor

from .guild_interfaces import IChannelService, IChannelProcessor
from .guild_services import GuildService, ChannelService, ChannelProcessor

class DiscordView(View, ContextMixin):
  template_name = ''

  config = DiscordConfig

  # User
  user_service: IUserService = DiscordUserService(config)
  avatar_processor: IAvatarProcessor = AvatarProcessor(config)
  member_service: MemberService = MemberService(user_service, avatar_processor)

  # Guild
  channel_service: IChannelService = ChannelService(config)
  channel_processor: IChannelProcessor = ChannelProcessor()
  guild_service: GuildService = GuildService(channel_service, channel_processor)

  discord_context = {
    'meta': {
      'guild_name': config.GUILD_NAME,
      'site_name': settings.SITE_NAME,
      'description': settings.DESCRIPTION,
      'favicon': config.GUILD_FAVICON,
    },
  }

  def get_context_data(self, **kwargs) -> dict:
    context = super().get_context_data(**kwargs)
    context.update(self.discord_context)
    return context
  
  def render_template(self, request: HttpRequest, context=None) -> HttpResponse:
    context = self.get_context_data(**context)
    return render(request, self.template_name, context)