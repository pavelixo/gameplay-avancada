from abc import ABC, abstractmethod
from typing import Dict, List, Union
from .types import User

class IUserService(ABC):
  @abstractmethod
  def get_users(self) -> Union[ List[User] | None ]:
    pass

class IAvatarProcessor(ABC):
  @abstractmethod
  def process_avatar(self, users: List[User]) -> List[User]:
    pass
