from requests import get
from django.conf import settings
from typing import Union, Type
from .types import Endpoint, ID, Data


class DiscordConfig:
  @staticmethod
  def fetch_data(endpoint: str) -> Union[Data, None]:
    headers = settings.DISCORD_AUTH

    response = get(url=endpoint, headers=headers)
    if response.status_code == 200:
      return response.json()
    else:
      return None
  
  @staticmethod
  def parser(obj: object, target: Type) -> Union[object, None]:
    if not obj:
      return None
    try:
      return target(obj)
    except ValueError:
      return None

  # Base endpoints 
  DISCORD_API_BASE: Endpoint = settings.DISCORD_API_BASE
  DISCORD_IMAGE_BASE: Endpoint = settings.DISCORD_IMAGE_BASE

  # ID's
  GUILD_ID: ID = settings.GUILD_ID

  # Endpoints
  GUILDS_ENDPOINT: Endpoint = f'{DISCORD_API_BASE}/guilds'
  USER_AVATARS_ENDPOINT: Endpoint = f'{DISCORD_IMAGE_BASE}/avatars'
  GUILD_MEMBERS: Endpoint = f'{GUILDS_ENDPOINT}/{GUILD_ID}/members'
  

  # Data, Fetching: Guild
  GUILD_DATA: Data = fetch_data(f'{DISCORD_API_BASE}/guilds/{GUILD_ID}?with_counts=true')
  GUILD_MEMBERS_COUNT: Data = GUILD_DATA['approximate_member_count']

  # Data, Fetching: Owner
  OWNER_DATA: Data = fetch_data(f'{DISCORD_API_BASE}/users/{GUILD_DATA["owner_id"]}')
  OWNER_USERNAME: Data = OWNER_DATA['username']
  OWNER_GLOBAL_NAME: Data = OWNER_DATA['global_name']

  GUILD_NAME = GUILD_DATA['name']
  GUILD_FAVICON = f"{DISCORD_IMAGE_BASE}/icons/{GUILD_ID}/{GUILD_DATA['icon']}.png"
  GUILD_MEMBERS_COUNT: int = parser(GUILD_MEMBERS_COUNT, int)
