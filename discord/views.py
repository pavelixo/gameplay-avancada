from django.views import View
from django.http import HttpResponse, HttpRequest
from django.views.generic.base import ContextMixin
from django.shortcuts import render
from django.conf import settings

from .config import DiscordConfig
from .services import DiscordUserService, AvatarProcecssor, MemberService
from .interface import IUserService, IAvatarProcessor

class DiscordView(View, ContextMixin):
  template_name = ''

  config = DiscordConfig
  headers = settings.DISCORD_AUTH
  user_service: IUserService = DiscordUserService(config, headers)
  avatar_processor: IAvatarProcessor = AvatarProcecssor(config)
  member_service: MemberService = MemberService(user_service, avatar_processor)

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