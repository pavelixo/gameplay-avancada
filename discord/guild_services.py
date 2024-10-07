from typing import List

from .guild_interfaces import IChannelService, IChannelProcessor, IMessageService, IMessageProcessor
from .config import DiscordConfig
from .types import Channel, ID, Data, Message
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
    channels_data: Data = fetch_data(endpoint=endpoint, params={'nfsw': False})
    return channels_data
  
  def get_channel(self, channel_id: ID) -> Channel:
    endpoint = f'{self.config.CHANNELS}/{channel_id}'
    channel_data: Data = fetch_data(endpoint=endpoint)
    return channel_data


class ChannelProcessor(IChannelProcessor):
  def process_channels(self, channels: List[Channel], channel_type: str = 'text') -> List[Channel]:
    matching = {
      'text': GUILD_TEXT,
    }

    target = matching.get(channel_type)
    if channels is not None:
      return [channel for channel in channels if channel['type'] == target]
    return None


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
              if message['referenced_message']['author']['avatar']:
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
          else:
              processed_message = message
          processed_messages.append(processed_message)

      return processed_messages

  def process_users_avatars_messages(self, messages: List[Message]) -> List[Message]:
    processed_messages = []

    for message in messages:
      if message['author']['avatar'] is not None:
        processed_message = {
          **message,
          'author': {
            **message['author'],
            'avatar': f'{self.config.DISCORD_IMAGE_BASE}/avatars/{message["author"]["id"]}/{message["author"]["avatar"]}'
          }
        }
      else:
        processed_messages.append(message)
      processed_messages.append(processed_message)
    return processed_messages
    
    
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
  
  def get_channel(self, channel_id: ID) -> Channel:
    return self.channel_service.get_channel(channel_id=channel_id)
  
  def get_channels(self, channel_type: str = 'text') -> List[Channel]:
    channels = self.channel_service.get_channels()
    return self.channel_processor.process_channels(channels, channel_type)
  
  def get_channel_messages(self, channel_id: ID, limit: int = 10) -> Channel:
    fetch_messages = self.message_service.get_messages(channel_id=channel_id, limit=limit)

    if fetch_messages:
      avatar_processor = self.message_processor.process_users_avatars_messages(fetch_messages)
      messages = self.message_processor.process_replies_messages(avatar_processor)
      return messages
    return None
