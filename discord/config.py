from django.conf import settings
from .types import Endpoint, ID

class DiscordConfig:
  # Base endpoints 
  DISCORD_API_BASE: Endpoint = 'https://discord.com/api/v10'
  DISCORD_IMAGE_BASE: Endpoint = 'https://cdn.discordapp.com'

  # ID's
  GUILD_ID: ID = settings.GUILD_ID

  # Endpoints
  GUILDS_ENDPOINT: Endpoint = f'{DISCORD_API_BASE}/guilds'
  USER_AVATARS_ENDPOINT: Endpoint = f'{DISCORD_IMAGE_BASE}/avatars'
  GUILD_MEMBERS: Endpoint = f'{GUILDS_ENDPOINT}/{GUILD_ID}/members'
