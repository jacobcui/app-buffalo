"""Landing page."""

from views import BaseView

class View(BaseView):
  """Index/Landing page view."""

  def get(self):
    template_values = {
      'user': self.user,
      'urls': self.urls
    }

    self.send_response('signup.html', template_values)
