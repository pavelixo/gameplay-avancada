from typing import List, Union

from discord.types import Data

from .user_interface import IUserService, IAvatarProcessor
from .config import DiscordConfig
from .types import User
from .utils import fetch_data

class DiscordUserService(IUserService):
  def __init__(self, config: DiscordConfig) -> None:
    self.config = config
  
  def get_users(self) -> Union[List[User], None]:
    endpoint = self.config.GUILD_MEMBERS
    params = {
      'limit': self.config.guild_members_count
    }

    users_data: Data = fetch_data(endpoint=endpoint, params=params)
    if not users_data:
      return None
    return [user['user'] for user in users_data]


class AvatarProcessor(IAvatarProcessor):
  def __init__(self, config: DiscordConfig):
    self.config = config
  
  def process_avatar(self, users: List[User]) -> List[User]:
    return [
      {
        **user, 
        'avatar': f'{self.config.DISCORD_IMAGE_BASE}/avatars/{user["id"]}/{user["avatar"]}' if user['avatar'] else None
      }
      for user in users
    ]


class MemberService:
  def __init__(self, user_service: IUserService, avatar_processor: IAvatarProcessor):
    self.user_service = user_service
    self.avatar_processor = avatar_processor

  def get_members(self) -> Union[List[User], None]:
    users = self.user_service.get_users()
    if not users:
      return None
    
    return self.avatar_processor.process_avatar(users)