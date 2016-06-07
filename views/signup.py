"""Signup page."""

import views
from models import User
from views import BaseView


class View(BaseView):
  """Sign up page view."""

  def get(self):
    self.template_values['page_name'] = 'signup'
    self.send_response('signup.html')

  def post(self):
    self.template_values['page_name'] = 'signin'
    signup_data = dict(self.request.POST)
    # {u'_token': u'', u'username': u'jacobcui', u'password_confirmation': u'qwqq', u'g-recaptcha-response': u'', u'password': u'qwqq'}
    if not self.verify_recaptcha():
      self.template_values['alerts'].append({
        'class': views.ALERT_CLASS_WARNING,
        'content': 'Please check reCAPTCHA input.'
      })
      human_verified = False
    else:
      human_verified = True

    for field in ['username', 'password', 'password_confirmation']:
      value = signup_data.get(field, '').strip()

      if not value:
        self.template_values['alerts'].append(
          {
            'class': views.ALERT_CLASS_WARNING,
            'content': ("{} can't be empty."
                        .format(
                          field.capitalize().replace('_', ' ')))
          })

    if len(signup_data.get('password', '')) < 4:
      self.template_values['alerts'].append({
        'class': views.ALERT_CLASS_WARNING,
        'content': 'Please ensure password is longer than 4 characters.'
      })
      
    if (signup_data.get('password', '') !=
        signup_data.get('password_confirmation', '')):
      self.template_values['alerts'].append({
        'class': views.ALERT_CLASS_WARNING,
        'content': 'Please ensure passwords are the same.'
      })

    if not User.validate_username(signup_data.get('username', '')):
      self.template_values['alerts'].append({
        'class': views.ALERT_CLASS_WARNING,
        'content': 'Please input valid username. Letters, Numbers, -, _ are allowed.'
      })      
      
    if human_verified and User.getByUsername(signup_data.get('username', '')):
      self.template_values['alerts'].append({
        'class': views.ALERT_CLASS_WARNING,
        'content': 'User with username {} has been registered.'.format(signup_data.get('username'))
      })

    if self.template_values['alerts']:
      self.template_values.update(signup_data)
      self.send_response('signup.html')
      return

    username=signup_data.get('username').strip()

    # Create user
    self.user = User.Create(username=username,
                            password=signup_data.get('password'))

    self.init_new_session(username)
    self.redirect('/')
                
