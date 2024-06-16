from typing import Any
from django.views import View
from django.conf import settings

from .config import DiscordConfig
from .services import DiscordUserService, AvatarProcecssor, MemberService
from .interface import IUserService, IAvatarProcessor

class DiscordView(View):
  config = DiscordConfig
  headers = settings.DISCORD_AUTH
  user_service: IUserService = DiscordUserService(config, headers)
  avatar_processor: IAvatarProcessor = AvatarProcecssor(config)
  member_service: MemberService = MemberService(user_service, avatar_processor)
