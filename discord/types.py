from abc import ABC
from typing import TypeVar, Generic, TypedDict, Optional, List

T = TypeVar('T')

class AbstractTypes(ABC, Generic[T]):
  def __init__(self, value: T):
    self.value = value


class User(TypedDict):
  id: str
  username: str
  avatar: str
  discriminator: str
  public_flags: int
  flags: int
  banner: Optional[str]
  accent_color: Optional[int]
  global_name: str
  avatar_decoration_data: Optional[str]
  banner_color: Optional[str]
  clan: Optional[str]

class TextChannel(TypedDict):
  id: str
  guild_id: str
  name: str
  type: int
  position: int
  permission_overwrites: List
  rate_limit_per_user: int
  nsfw: bool
  topic: str
  last_message_id: str
  parent_id: str
  default_auto_archive_duration: int

class Endpoint(AbstractTypes):
  pass


class ID(AbstractTypes):
  pass


class Data(AbstractTypes):
  pass
