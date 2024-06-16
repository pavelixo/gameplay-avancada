from .mixins import CacheMixin
from discord.views import DiscordView


class Home(CacheMixin, DiscordView):
  template_name = 'home.html'

  def get(self, request):
    context = {
      'users': self.member_service.get_members(),
    }
    return self.render_template(request, context)