from abc import ABC
from typing import TypeVar, Generic, TypedDict, Optional, List, Union

T = TypeVar('T')


class AbstractTypes(ABC, Generic[T]):
    def __init__(self, value: T):
        self.value = value


class User(TypedDict):
    id: str  # snowflake: The user's ID
    username: str  # string: The user's username
    avatar: Optional[str]  # avatar hash of the user
    discriminator: str  # the user's 4-digit discord-tag
    public_flags: Optional[int]  # the flags on a user's account
    flags: Optional[int]  # the flags on a user's account
    banner: Optional[str]  # the user's banner hash
    accent_color: Optional[int]  # the user's chosen accent color
    global_name: Optional[str]  # the user's linked account's global username
    avatar_decoration_data: Optional[str]  # the type of nitro badge on this user's avatar
    banner_color: Optional[str]  # the user's banner color if they have one
    clan: Optional[str]  # the user's connected guild membership info


class RoleTags(TypedDict, total=False):
    bot_id: Optional[str]  # snowflake: the id of the bot this role belongs to
    integration_id: Optional[str]  # snowflake: the id of the integration this role belongs to
    premium_subscriber: Optional[None]  # null: whether this is the guild's Booster role
    subscription_listing_id: Optional[str]  # snowflake: the id of this role's subscription sku and listing
    available_for_purchase: Optional[None]  # null: whether this role is available for purchase
    guild_connections: Optional[None]  # null: whether this role is a guild's linked role


class Role(TypedDict):
    id: str  # snowflake: role id
    name: str  # string: role name
    color: int  # integer: integer representation of hexadecimal color code
    hoist: bool  # boolean: if this role is pinned in the user listing
    icon: Optional[str]  # ?string: role icon hash
    unicode_emoji: Optional[str]  # ?string: role unicode emoji
    position: int  # integer: position of this role (roles with the same position are sorted by id)
    permissions: str  # string: permission bit set
    managed: bool  # boolean: whether this role is managed by an integration
    mentionable: bool  # boolean: whether this role is mentionable
    tags: Optional[RoleTags]  # ?role tags object: the tags this role has
    flags: int  # integer: role flags combined as a bitfield


class ChannelMention(TypedDict):
    id: str  # snowflake: id of the channel
    guild_id: str  # snowflake: id of the guild containing the channel
    type: int  # integer: the type of channel
    name: str  # name of the channel


class Attachment(TypedDict, total=False):
    id: str  # snowflake: attachment id
    filename: str  # name of file attached
    title: Optional[str]  # the title of the file
    description: Optional[str]  # description for the file (max 1024 characters)
    content_type: Optional[str]  # the attachment's media type
    size: int  # size of file in bytes
    url: str  # source url of file
    proxy_url: str  # a proxied url of file
    height: Optional[int]  # height of file (if image)
    width: Optional[int]  # width of file (if image)
    ephemeral: Optional[bool]  # whether this attachment is ephemeral
    duration_secs: Optional[float]  # the duration of the audio file (currently for voice messages)
    waveform: Optional[str]  # base64 encoded bytearray representing a sampled waveform (currently for voice messages)
    flags: Optional[int]  # attachment flags combined as a bitfield


class EmbedFooter(TypedDict, total=False):
    text: str
    icon_url: Optional[str]
    proxy_icon_url: Optional[str]


class EmbedImage(TypedDict, total=False):
    url: Optional[str]
    proxy_url: Optional[str]
    height: Optional[int]
    width: Optional[int]


class EmbedThumbnail(TypedDict, total=False):
    url: Optional[str]
    proxy_url: Optional[str]
    height: Optional[int]
    width: Optional[int]


class EmbedVideo(TypedDict, total=False):
    url: Optional[str]
    proxy_url: Optional[str]
    height: Optional[int]
    width: Optional[int]


class EmbedProvider(TypedDict, total=False):
    name: Optional[str]
    url: Optional[str]


class EmbedAuthor(TypedDict, total=False):
    name: Optional[str]
    url: Optional[str]
    icon_url: Optional[str]
    proxy_icon_url: Optional[str]


class EmbedField(TypedDict):
    name: str
    value: str
    inline: Optional[bool]


class Embed(TypedDict, total=False):
    title: Optional[str]
    type: Optional[str]
    description: Optional[str]
    url: Optional[str]
    timestamp: Optional[str]  # ISO8601 timestamp
    color: Optional[int]
    footer: Optional[EmbedFooter]
    image: Optional[EmbedImage]
    thumbnail: Optional[EmbedThumbnail]
    video: Optional[EmbedVideo]
    provider: Optional[EmbedProvider]
    author: Optional[EmbedAuthor]
    fields: Optional[List[EmbedField]]


class ReactionCountDetails(TypedDict, total=False):
    normal: int
    super: int
    burst: int


class PartialEmoji(TypedDict, total=False):
    id: Optional[str]  # emoji id (snowflake)
    name: Optional[str]  # emoji name
    animated: Optional[bool]  # whether this emoji is animated


class Reaction(TypedDict, total=False):
    count: int  # Total number of times this emoji has been used to react (including super reacts)
    count_details: ReactionCountDetails  # Reaction count details object
    me: bool  # Whether the current user reacted using this emoji
    me_burst: bool  # Whether the current user super-reacted using this emoji
    emoji: PartialEmoji  # emoji information
    burst_colors: List[str]  # HEX colors used for super reaction


class MessageActivity(TypedDict, total=False):
    type: int  # type of message activity
    party_id: Optional[str]  # party_id from a Rich Presence event


class PartialUser(TypedDict, total=False):
    id: str  # snowflake
    username: str
    avatar: str
    discriminator: str


class TeamMember(TypedDict):
    membership_state: int  # integer
    team_id: str  # snowflake
    user: PartialUser  # partial user object
    role: str  # string


class Team(TypedDict, total=False):
    id: str  # snowflake
    name: str
    icon: Optional[str]
    members: List[TeamMember]


class PartialGuild(TypedDict, total=False):
    id: str  # snowflake
    name: str
    icon: Optional[str]


class InstallParams(TypedDict, total=False):
    scopes: List[str]
    permissions: str


class IntegrationTypeConfig(TypedDict, total=False):
    scopes: List[str]
    permissions: str


class PartialApplication(TypedDict, total=False):
    id: str  # snowflake
    name: str
    icon: Optional[str]
    description: str
    rpc_origins: Optional[List[str]]
    bot_public: bool
    bot_require_code_grant: bool
    bot: Optional[PartialUser]
    terms_of_service_url: Optional[str]
    privacy_policy_url: Optional[str]
    owner: Optional[PartialUser]
    summary: str  # deprecated
    verify_key: str
    team: Optional[Team]
    guild_id: Optional[str]  # snowflake
    guild: Optional[PartialGuild]
    primary_sku_id: Optional[str]  # snowflake
    slug: Optional[str]
    cover_image: Optional[str]
    flags: Optional[int]
    approximate_guild_count: Optional[int]
    redirect_uris: Optional[List[str]]
    interactions_endpoint_url: Optional[str]
    role_connections_verification_url: Optional[str]
    tags: Optional[List[str]]  # Max of 5 tags
    install_params: Optional[InstallParams]
    integration_types_config: Optional[Dict[str, IntegrationTypeConfig]]
    custom_install_url: Optional[str]


class MessageReference(TypedDict):
    message_id: Optional[str]
    channel_id: Optional[str]
    guild_id: Optional[str]
    fail_if_not_exists: Optional[bool]


class InteractionMetadata(TypedDict):
    id: str  # snowflake, ID da interação
    application_id: str  # snowflake, ID da aplicação para qual a interação é destinada
    type: int  # tipo de interação
    data: Optional[dict]  # payload de dados da interação
    guild: Optional[PartialGuild]  # objeto parcial da guilda de onde a interação foi enviada
    guild_id: Optional[str]  # snowflake, ID da guilda de onde a interação foi enviada
    channel: Optional[PartialChannel]  # objeto parcial do canal de onde a interação foi enviada
    channel_id: Optional[str]  # snowflake, ID do canal de onde a interação foi enviada
    member: Optional[GuildMember]  # objeto de membro da guilda para o usuário que invocou a interação
    user: Optional[User]  # objeto de usuário para o usuário que invocou a interação, se invocado em uma DM
    token: str  # token de continuação para responder à interação
    version: int  # propriedade somente leitura, sempre 1
    message: Optional[dict]  # para componentes, a mensagem à qual eles estão anexados
    app_permissions: Optional[str]  # conjunto bitwise de permissões que o aplicativo tem no local de origem da interação
    locale: Optional[str]  # idioma selecionado do usuário que invocou a interação
    guild_locale: Optional[str]  # idioma preferido da guilda, se invocado em uma guilda
    entitlements: Optional[List[dict]]  # para aplicativos monetizados, quaisquer direitos para o usuário que invocou a interação
    authorizing_integration_owners: Optional[Dict[str, str]]  # mapeamento de contextos de instalação que a interação foi autorizada para IDs de usuário ou guilda relacionados
    context: Optional[str]  # tipo de contexto onde a interação foi acionada


class Interaction(TypedDict):
    id: str
    type: int
    guild_id: str
    channel_id: str
    member: Optional[GuildMember]
    user: Optional[User]
    token: str
    version: int
    data: Optional[dict]


class Thread(TypedDict):
    id: str
    guild_id: str
    parent_id: str
    owner_id: str
    name: str
    type: int
    message_count: int
    member_count: int
    rate_limit_per_user: int
    last_message_id: str
    last_pin_timestamp: Optional[str]


class MessageComponent(TypedDict):
    type: int
    custom_id: Optional[str]
    disabled: Optional[bool]
    style: Optional[int]
    label: Optional[str]
    emoji: Optional[PartialEmoji]
    url: Optional[str]
    options: Optional[List[dict]]


class MessageStickerItem(TypedDict):
    id: str
    name: str
    format_type: int


class Sticker(TypedDict):
    id: str
    pack_id: str
    name: str
    description: str
    tags: Optional[List[str]]
    asset: str
    preview_asset: Optional[str]
    format_type: int


class RoleSubscriptionData(TypedDict):
    is_premium: Optional[bool]
    premium_subscription_count: Optional[int]
    can_subscribe: Optional[bool]
    subscribed: Optional[bool]


class ResolvedData(TypedDict):
    users: Optional[dict]
    members: Optional[dict]
    roles: Optional[dict]
    channels: Optional[dict]


class Poll(TypedDict):
    id: str
    channel_id: str
    question: str
    votes: int
    options: List[str]
    duration: int
    ended: bool


class MessageCall(TypedDict):
    ended_timestamp: Optional[str]
    message_id: str
    channel_id: str


class Message(TypedDict):
    id: int  # snowflake: id of the message
    channel_id: int  # snowflake: id of the channel the message was sent in
    author: Optional[User]  # the author of this message (not guaranteed to be a valid user)
    content: Optional[str]  # contents of the message
    timestamp: str  # ISO8601 timestamp representing the timestamp when this message was sent
    edited_timestamp: Optional[str]  # ISO8601 timestamp representing the time this message was edited, or None if never
    tts: bool  # whether this was a TTS message
    mention_everyone: bool  # whether this message mentions everyone
    mentions: Optional[List[User]]  # array of user objects, with an additional partial member field
    mention_roles: Optional[List[int]]  # array of role object ids
    mention_channels: Optional[List[ChannelMention]]  # array of channel mention objects
    attachments: Optional[List[Attachment]]  # array of attachment objects
    embeds: Optional[List[Embed]]  # array of embed objects
    reactions: Optional[List[Reaction]]  # array of reaction objects
    nonce: Optional[Union[int, str]]  # used for validating a message was sent
    pinned: bool  # whether this message is pinned
    webhook_id: Optional[int]  # if the message is generated by a webhook, this is the webhook's id
    type: int  # the type of message
    activity: Optional[MessageActivity]  # sent with Rich Presence-related chat embeds
    application: Optional[PartialApplication]  # sent with Rich Presence-related chat embeds
    application_id: Optional[int]  # the id of the webhook's application, if it is an incoming webhook
    message_reference: Optional[MessageReference]  # message reference data sent with crossposted messages and replies
    flags: Optional[int]  # message flags combined as a bitfield
    referenced_message: Optional['Message']  # sent if the message is a response to a message interaction
    interaction_metadata: Optional[InteractionMetadata]  # interaction data sent with message components
    interaction: Optional[Interaction]  # interaction data sent with message components
    thread: Optional[Thread]  # the thread that was started from this message, includes thread member object
    components: Optional[List[MessageComponent]]  # message components sent with the message
    sticker_items: Optional[List[MessageStickerItem]]  # stickers sent with the message
    stickers: Optional[List[Sticker]]  # stickers sent with the message
    position: Optional[int]  # position of the message in the channel
    role_subscription_data: Optional[RoleSubscriptionData]  # data sent with roles for rich presence enabled messages
    resolved: Optional[ResolvedData]  # data sent with threads for guilds that are not yet available
    poll: Optional[Poll]  # sent with message components for responding to messages
    call: Optional[MessageCall]  # message call data


class Endpoint(AbstractTypes[str]):
    pass


class ID(AbstractTypes[int]):
    pass


class Data(AbstractTypes[Message]):
    pass
