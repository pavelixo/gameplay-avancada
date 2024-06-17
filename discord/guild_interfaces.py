from abc import ABC, abstractmethod
from typing import List
from .types import Channel, ID

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