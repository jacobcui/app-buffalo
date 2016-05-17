"""Landing page."""

from views import BaseView

class View(BaseView):
  """Index/Landing page view."""

  def get(self):
    template_values = {
      'user': self.user,
      'urls': self.urls
    }

    if not self.user:
#      {% include "signout.html" %}
#      {% else %}
#        {% include "signin.html" %}
#      {% endif %}
      self.send_response('signin.html', template_values)

    self.send_response('index.html', template_values)
