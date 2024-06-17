from typing import List

from discord.types import ID, Data

from .guild_interfaces import IChannelService, IChannelProcessor
from .config import DiscordConfig
from .types import Channel
from .utils import fetch_data

# Channels type
GUILD_TEXT = 0
DM = 1
GUILD_VOICE = 2
GROUP_DM = 3
GUILD_CATEGORY = 4
GUILD_ANNOUNCEMENT = 	5
ANNOUNCEMENT_THREAD = 10
PUBLIC_THREAD = 11
PRIVATE_THREAD = 12
GUILD_STAGE_VOICE = 13
GUILD_DIRECTORY = 14
GUILD_FORUM = 15
GUILD_MEDIA = 16


class ChannelService(IChannelService):
  def __init__(self, config: DiscordConfig):
    self.config = config
  
  def get_channels(self) -> List[Channel]:
    endpoint = self.config.GUILD_CHANNELS
    channels_data: Data = fetch_data(endpoint=endpoint)
    if not channels_data:
      return None
    return channels_data
  
  def get_channel(self, id: ID) -> Channel:
    endpoint = f'{self.config.GUILD_CHANNELS}/{id}'
    params = {'nfsw': False}

    channel_data: Data = fetch_data(endpoint=endpoint, params=params)
    if not channel_data:
      return None
    return channel_data


class ChannelProcessor(IChannelProcessor):
  def process_channels(self, channels: List[Channel], channel_type: str = 'text') -> List[Channel]:
    matching = {
      'text': GUILD_TEXT,
    }

    target = matching.get(channel_type)
    
    return [channel for channel in channels if channel['type'] == target]

class GuildService:
  def __init__(self, channels_service: IChannelService, channel_processor: IChannelProcessor):
    self.channel_service = channels_service
    self.channel_processor = channel_processor
  
  def get_channels(self, channel_type: str = 'text') -> List[Channel]:
    channels = self.channel_service.get_channels()
    return self.channel_processor.process_channels(channels, channel_type)
