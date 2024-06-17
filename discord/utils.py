from requests import get
from django.conf import settings
from typing import Union, Type
from .types import Data, Endpoint


def fetch_data(endpoint: Endpoint, status_code=200, **kwargs) -> Union[Data, None]:
  headers = settings.DISCORD_AUTH

  response = get(url=endpoint, headers=headers, **kwargs)
  if response.status_code == status_code:
    return response.json()
  else:
    return None
  
def parser(obj: object, target: Type) -> Union[object, None]:
  if not obj:
    return None
  try:
    return target(obj)
  except ValueError:
    return None
    