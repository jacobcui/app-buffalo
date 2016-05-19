"""Contact page."""

from views import BaseView
import settings

class View(BaseView):
  """Contact page view."""

  def get(self):
    self.template_values['page_name'] = 'contact'
    self.send_response('contact.html')
