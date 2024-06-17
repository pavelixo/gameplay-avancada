from abc import ABC
from typing import TypeVar, Generic, TypedDict, Optional, List, Union

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

class Channel(TypedDict):
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

class Message(TypedDict):
  id: int
  channel_id: int
  author: Optional[dict]  # user object, may not always be valid
  content: Optional[str]
  timestamp: str  # ISO8601 timestamp
  edited_timestamp: Optional[str]  # ISO8601 timestamp or None
  tts: bool
  mention_everyone: bool
  mentions: Optional[List[dict]]  # array of user objects
  mention_roles: Optional[List[int]]  # array of role object ids
  mention_channels: Optional[List[dict]]  # array of channel mention objects
  attachments: Optional[List[dict]]  # array of attachment objects
  embeds: Optional[List[dict]]  # array of embed objects
  reactions: Optional[List[dict]]  # array of reaction objects
  nonce: Optional[Union[int, str]]  # integer or string
  pinned: bool
  webhook_id: Optional[int]  # snowflake, if message is from a webhook
  type: int
  activity: Optional[dict]  # message activity object
  application: Optional[dict]  # partial application object
  application_id: Optional[int]  # snowflake, if message is from an Interaction or app webhook
  message_reference: Optional[dict]  # message reference object
  flags: Optional[int]  # message flags combined as bitfield
  referenced_message: Optional[dict]  # message object associated with message_reference
  interaction_metadata: Optional[dict]  # message interaction metadata object
  interaction: Optional[dict]  # deprecated message interaction object
  thread: Optional[dict]  # channel object for the thread
  components: Optional[List[dict]]  # array of message components
  sticker_items: Optional[List[dict]]  # array of message sticker item objects
  stickers: Optional[List[dict]]  # deprecated array of sticker objects
  position: Optional[int]  # approximate position in a thread
  role_subscription_data: Optional[dict]  # role subscription data object
  resolved: Optional[dict]  # resolved data for users, members, channels, roles
  poll: Optional[dict]  # poll object
  call: Optional[dict]  # message call object

class Endpoint(AbstractTypes):
  pass


class ID(AbstractTypes):
  pass


class Data(AbstractTypes):
  pass
