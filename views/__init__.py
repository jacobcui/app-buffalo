"""Basic view handler."""


import jinja2
import webapp2


import settings

ALERT_CLASS_INFO = 'alert-info'
ALERT_CLASS_SUCCESS = 'alert-success'
ALERT_CLASS_WARNING = 'alert-warning'


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
  template_values = {'settings': settings, 'signin_url': '',
                     'signout_url': '', 'alerts': []}

  def __init__(self, *args, **kwargs):
    super(BaseView, self).__init__(*args, **kwargs)
    self.user = users.get_current_user()

    if self.user:
      self.template_values['signout_url'] = users.create_logout_url('/')
    else:
      self.template_values['signin_url'] = users.create_login_url('/signin/check')

    self.template_values['user'] = self.user or None

  def send_response(self, template_name):
    self.response.write(
      render_template(template_name, self.template_values))
