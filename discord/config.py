from django.conf import settings
from .utils import fetch_data, parser
from .types import Endpoint, ID, Data


class DiscordConfig:

  # Base endpoints 
  DISCORD_API_BASE: Endpoint = settings.DISCORD_API_BASE
  DISCORD_IMAGE_BASE: Endpoint = settings.DISCORD_IMAGE_BASE

  # ID's
  GUILD_ID: ID = settings.GUILD_ID
  
  # Endpoints
  GUILDS_ENDPOINT: Endpoint = f'{DISCORD_API_BASE}/guilds'
  USER_AVATARS_ENDPOINT: Endpoint = f'{DISCORD_IMAGE_BASE}/avatars'
  GUILD_MEMBERS: Endpoint = f'{GUILDS_ENDPOINT}/{GUILD_ID}/members'
  GUILD_CHANNELS: Endpoint = f'{GUILDS_ENDPOINT}/{GUILD_ID}/channels'
  CHANNELS: Endpoint = f'{DISCORD_API_BASE}/channels'
  
  # Data, Fetching: Guild
  GUILD_DATA: Data = fetch_data(f'{DISCORD_API_BASE}/guilds/{GUILD_ID}?with_counts=true')
  GUILD_MEMBERS_COUNT: Data = GUILD_DATA['approximate_member_count']

  # Data, Fetching: Owner
  OWNER_DATA: Data = fetch_data(f'{DISCORD_API_BASE}/users/{GUILD_DATA["owner_id"]}')
  OWNER_USERNAME: Data = OWNER_DATA['username']
  OWNER_GLOBAL_NAME: Data = OWNER_DATA['global_name']

  GUILD_NAME = GUILD_DATA['name']
  GUILD_FAVICON = f"{DISCORD_IMAGE_BASE}/icons/{GUILD_ID}/{GUILD_DATA['icon']}.png"

  guild_members_count: int = parser(GUILD_MEMBERS_COUNT, int)
