"""Signup page."""

from views import BaseView

class View(BaseView):
  """Sign up page view."""

  def get(self):
    self.template_values['page_name'] = 'signup'
    self.send_response('signup.html')
