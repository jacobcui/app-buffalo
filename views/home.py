"""Landing page."""

from views import BaseView
import settings

class View(BaseView):
  """Index/Landing page view."""

  def get(self):
    self.template_values['page_name'] = 'home'
    self.send_response('index.html')
