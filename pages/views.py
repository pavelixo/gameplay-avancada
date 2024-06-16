from django.shortcuts import render
from discord.views import DiscordView


class Home(DiscordView):
  template_name = 'home.html'

  def get(self, request):
    context = {
      'users': self.member_service.get_members()
    }
    return self.render_template(request, context)