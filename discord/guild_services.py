from typing import List

from django.conf import settings
from discord.types import ID, Data, Message

from .guild_interfaces import IChannelService, IChannelProcessor, IMessageService, IMessageProcessor
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


class MessageService(IMessageService):
  def __init__(self, config: DiscordConfig):
    self.config = config
  
  def get_messages(self, channel_id: ID, limit: int = 10) -> List[Message]:
    endpoint = f'{self.config.CHANNELS}/{channel_id}/messages'
    params = {'limit': limit}
    return fetch_data(endpoint=endpoint, params=params)


class MessageProcessor(IMessageProcessor):
  def __init__(self, config: DiscordConfig):
    self.config = config
  
  def process_replies_messages(self, messages: List[Message]) -> List[Message]:
      processed_messages = []

      for message in messages:
          if 'referenced_message' in message and message['referenced_message'] is not None and 'author' in message['referenced_message']:
              processed_message = {
                  **message,
                  'referenced_message': {
                      **message['referenced_message'],
                      'author': {
                          **message['referenced_message']['author'],
                          'avatar': f"{self.config.DISCORD_IMAGE_BASE}/avatars/{message['referenced_message']['author']['id']}/{message['referenced_message']['author']['avatar']}"
                      }
                  }
              }
          else:
              processed_message = message
          processed_messages.append(processed_message)

      return processed_messages




  def process_users_avatars_messages(self, messages: List[Message]) -> List[Message]:
    return [
      {
        **message, 
        'author': {
          **message['author'], 
          'avatar': f'{self.config.DISCORD_IMAGE_BASE}/avatars/{message["author"]["id"]}/{message["author"]["avatar"]}'
        }
      } 
      for message in messages
    ]
    

class GuildService:
  def __init__(
      self, 
      channels_service: IChannelService, 
      channel_processor: IChannelProcessor,
      message_service: IMessageService,
      message_processor: IMessageProcessor
    ):

    # Channels
    self.channel_service = channels_service
    self.channel_processor = channel_processor

    # Messages
    self.message_service = message_service
    self.message_processor = message_processor
  
  def get_channels(self, channel_type: str = 'text') -> List[Channel]:
    channels = self.channel_service.get_channels()
    return self.channel_processor.process_channels(channels, channel_type)
  
  def get_announcements(self) -> List[Message]:
    announcements_channel_id: ID = settings.ANNOUNCEMENTS_CHANNEL_ID
    fetch_messages = self.message_service.get_messages(channel_id=announcements_channel_id, limit=5)
    
    avatar_processor = self.message_processor.process_users_avatars_messages(fetch_messages)
    replies_processor = self.message_processor.process_replies_messages(avatar_processor)
    
    return replies_processor