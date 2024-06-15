from django.http import HttpResponse
from discord.views import DiscordView


class Index(DiscordView):
  def get(self, request):
    users = [user['username'] for user in self.user_service.get_users()]
    usernames = ', '.join(users)
    return HttpResponse(f'{usernames}')