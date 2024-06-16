from requests import get, Response
from typing import Dict, List, Union
from .interface import IUserService, IAvatarProcessor
from .config import DiscordConfig
from .types import User


class DiscordUserService(IUserService):
  def __init__(self, config: DiscordConfig, headers: Dict[str, str]) -> None:
    self.config = config
    self.headers = headers
  
  def get_users(self) -> Union[List[User], None]:
    response: Response = get(
      url=self.config.GUILD_MEMBERS, 
      params={'limit': self.config.GUILD_MEMBERS_COUNT}, 
      headers=self.headers
    )

    if response.status_code == 200:
      data =  response.json()
      return [user['user'] for user in data]
    return None


class AvatarProcecssor(IAvatarProcessor):
  def __init__(self, config: DiscordConfig):
    self.config = config
  
  def process_avatar(self, users: List[User]) -> List[User]:
    return [
      {**user, 'avatar': f'{self.config.DISCORD_IMAGE_BASE}/avatars/{user["id"]}/{user["avatar"]}'}
      for user in users
    ]


class MemberService:
  def __init__(self, user_service: IUserService, avatar_processor: IAvatarProcessor) -> None:
    self.user_service = user_service
    self.avatar_processor = avatar_processor

  def get_members(self) -> Union[List[User], None]:
    users = self.user_service.get_users()
    if not users:
      return None
    
    return self.avatar_processor.process_avatar(users)