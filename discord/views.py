
from django.views import View
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
      'site_name': 'Gameplay Avançada',
      'guild_name': config.GUILD_NAME,
      'favicon': config.GUILD_FAVICON,
      'description': f'estamos na ditadura de @{config.OWNER_USERNAME} A.K.A {config.OWNER_GLOBAL_NAME}'
    },
  }

  def get_context_data(self, **kwargs) -> dict:
    context = super().get_context_data(**kwargs)
    context.update(self.discord_context)
    return context
  
  def render_template(self, request, context=None):
    context = self.get_context_data(**context)
    return render(request, self.template_name, context)