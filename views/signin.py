"""Signin page."""

from views import BaseView


class View(BaseView):
  """Sign in page view."""

  def get(self):
    template_values = {
        'user': self.user,
        'urls': self.urls,
        'page_name': 'signin'
    }

    self.send_response('signin.html', template_values)
