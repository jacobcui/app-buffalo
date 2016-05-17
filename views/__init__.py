"""Basic view handler."""


import jinja2
import webapp2

from google.appengine.api import users

import settings

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(settings.TEMPLATE_DIR),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def get_template(html_name):
  return JINJA_ENVIRONMENT.get_template(html_name)

def render_template(html_name, template_values):
  template = get_template(html_name)
  return template.render(template_values)

class BaseView(webapp2.RequestHandler):
  urls = {'login':'', 'logout':''}

  def __init__(self, *args, **kwargs):
    super(BaseView, self).__init__(*args, **kwargs)
    self.user = users.get_current_user()

    if self.user:
      self.urls['logout'] = users.create_logout_url(self.request.uri)
    else:
      self.urls['login'] = users.create_login_url(self.request.uri)
    print self.urls

  def send_response(self, template_name, template_values):
    self.response.write(
      render_template(template_name, template_values))
