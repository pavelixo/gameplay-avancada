from django.shortcuts import render
from discord.views import DiscordView


class Home(DiscordView):
  def get(self, request):
    return render(request, 'home.html', context={'users': self.member_service.get_members()})