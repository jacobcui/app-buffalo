"""About page."""

from views import BaseView
import settings

class View(BaseView):
  """About page view."""

  def get(self):
    self.template_values['page_name'] = 'about'
    self.send_response('about.html')
