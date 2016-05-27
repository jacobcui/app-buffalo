"""Signin page."""

import views
from views import BaseView
from models import User


class View(BaseView):
  """Sign in page view."""

  def get(self):
    self.template_values['page_name'] = 'signin'
    self.template_values['alerts'] = []
    self.send_response('signin.html')

  def post(self):
    has_error = False
    self.template_values['alerts'] = []

    email = self.request.POST.get('email', '')
    password = self.request.POST.get('password', '')
    remember_me = self.request.POST.get('remember_me', '')

    self.template_values['page_name'] = 'signin'

    self.user = User.getByEmail(email)
    if not self.user:
      has_error = True
      self.template_values['alerts'].append(
        {'class': views.ALERT_CLASS_WARNING,
         'content': 'Email is not registered.'})

    if not password:
      has_error = True
      self.template_values['alerts'].append(
        {'class': views.ALERT_CLASS_WARNING,
         'content': "Password can't be empty."})

    if has_error:
      self.template_values['email'] = email
      self.template_values['password'] = password
      self.template_values['remember_me'] = remember_me
      self.send_response('signin.html')
      return

    self.init_new_session(email)
    self.redirect('/')


class Check(BaseView):
  """Checks user account."""

  def get(self):
    self.template_values['page_name'] = 'signin'
    current_user = getCurrentUser()
    
    self.send_response('signin.html')
