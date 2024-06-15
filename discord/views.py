from typing import Any
from django.views import View
from django.conf import settings

from .config import DiscordConfig
from .services import DiscordUserService


class DiscordView(View):
  config = DiscordConfig
  headers = settings.DISCORD_AUTH

  def __init__(self, **kwargs: Any) -> None:
    kwargs = {'config': self.config, 'headers': self.headers}

    self.user_service = DiscordUserService(**kwargs)
    super().__init__(**kwargs)