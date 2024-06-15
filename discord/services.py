from requests import get, Response
from typing import Dict, List, Union
from .abstract import IUserService
from .config import DiscordConfig
from .types import User


class DiscordUserService(IUserService):
  def __init__(self, config: DiscordConfig, headers: Dict[str, str]) -> None:
    self.config = config
    self.headers = headers
  
  def get_users(self) -> Union[ List[User] | None ]:
    response: Response = get(
      url=self.config.GUILD_MEMBERS, 
      params={'limit': 15}, 
      headers=self.headers
    )

    if response.status_code == 200:
      data =  response.json()
      return [user['user'] for user in data]
    return None

