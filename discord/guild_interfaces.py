from abc import ABC, abstractmethod
from typing import List
from .types import Channel, Message, ID

class IChannelService(ABC):
  @abstractmethod
  def get_channels(self) -> List[Channel]:
    pass

  @abstractmethod
  def get_channel(self, id: ID) -> Channel:
    pass

class IChannelProcessor(ABC):
  @abstractmethod
  def process_channels(self, channels: List[Channel], channel_type: str = 'text') -> List[Channel]:
    pass

class IMessageService(ABC):
  @abstractmethod
  def get_messages(self, channel_id: ID, limit: int = 10) -> List[Message]:
    pass

class IMessageProcessor(ABC):
  @abstractmethod
  def process_replies_messages(self, messages: List[Message]) -> List[Message]:
    pass
  
  @abstractmethod
  def process_users_avatars_messages(self, messages: List[Message]) -> List[Message]:
    pass