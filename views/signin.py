"""Signin page."""

from views import BaseView


class View(BaseView):
  """Sign in page view."""

  def get(self):
    self.template_values['page_name'] = 'signin'
    self.send_response('signin.html')
