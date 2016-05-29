"""Basic view handler."""

import uuid
import jinja2
import webapp2

from models import User, Session
from webapp2_extras import sessions
from logics import context

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
  def __init__(self, *args, **kwargs):
    super(BaseView, self).__init__(*args, **kwargs)

    # Get a session store for this request.
    self.session_store = sessions.get_store(request=self.request)
    self.user = self.getCurrentUser()
    self.template_values = {'settings': settings, 'signin_url': '',
                            'signout_url': '', 'alerts': []}
    self.template_values['signout_url'] = context.get_signout_url()
    self.template_values['google_signin_url'] = context.google_signin_url

    self.template_values['user'] = self.user

  def send_response(self, template_name):
    self.response.write(
      render_template(template_name, self.template_values))

  def dispatch(self):
    try:
      # Dispatch the request.
      webapp2.RequestHandler.dispatch(self)
    finally:
      # Save all sessions.
      self.session_store.save_sessions(self.response)

  @webapp2.cached_property
  def session(self):
    # Returns a session using the default cookie key.
    return self.session_store.get_session()

  def generate_session_id(self):
    return str(uuid.uuid1())

  def init_new_session(self, username):
    session_value = self.generate_session_id()
    self.session['EMAB'] = session_value
    self.template_values['session'] = session_value
    Session.Update(username=username, session=session_value)
    
  def is_same_session(self, session_value):
    return self.session.get('EMAB', '') == session_value

  def signOutCurrentUser(self):
    """ Clears the session.

    Returns:
      Sign out URL.
    """
    sign_out_url = '/'
    stored_session = Session.getById(self.session.get('EMAB', ''))
    if stored_session:
      stored_session.key.delete()

    return sign_out_url
    
  def getCurrentUser(self):
    stored_session = Session.getById(self.session.get('EMAB', ''))

    if stored_session:
      return User.getByUsername(stored_session.username)

    return None
  
