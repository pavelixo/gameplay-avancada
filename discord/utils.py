from requests import get
from django.conf import settings
from typing import Union, Type
from .types import Data


def fetch_data(endpoint: str) -> Union[Data, None]:
  headers = settings.DISCORD_AUTH

  response = get(url=endpoint, headers=headers)
  if response.status_code == 200:
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
    