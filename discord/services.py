from requests import get, Response
from typing import List, Union

from .interface import IUserService, IAvatarProcessor, IGuildService
from .config import DiscordConfig
from .types import User, TextChannel
from .utils import fetch_data

class DiscordUserService(IUserService):
  def __init__(self, config: DiscordConfig) -> None:
    self.config = config
  
  def get_users(self) -> Union[List[User], None]:
    endpoint = self.config.GUILD_MEMBERS
    params = {
      'limit': self.config.guild_members_count
    }

    users_data: Response = fetch_data(endpoint=endpoint, params=params)
    if not users_data:
      return None
    return [user['user'] for user in users_data]


class AvatarProcecssor(IAvatarProcessor):
  def __init__(self, config: DiscordConfig):
    self.config = config
  
  def process_avatar(self, users: List[User]) -> List[User]:
    return [
      {**user, 'avatar': f'{self.config.DISCORD_IMAGE_BASE}/avatars/{user["id"]}/{user["avatar"]}'}
      for user in users
    ]


class GuildService(IGuildService):
  def __init__(self, config: DiscordConfig):
    self.config = config
  
  def get_channels(self) -> List[TextChannel]:
    endpoint = self.config.GUILD_CHANNELS
    params = {'nfsw': False}

    channels_data: Response = fetch_data(endpoint=endpoint, params=params)
    if not channels_data:
      return None
    return channels_data


class MemberService:
  def __init__(self, user_service: IUserService, avatar_processor: IAvatarProcessor) -> None:
    self.user_service = user_service
    self.avatar_processor = avatar_processor

  def get_members(self) -> Union[List[User], None]:
    users = self.user_service.get_users()
    if not users:
      return None
    
    return self.avatar_processor.process_avatar(users)