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
    # {u'_token': u'', u'email': u'jacobcui123@gmail.com', u'password_confirmation': u'qwqq', u'g-recaptcha-response': u'', u'password': u'qwqq'}
    for field in ['email', 'password', 'password_confirmation']:
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

    if '@' not in signup_data.get('email', ''):
      self.template_values['alerts'].append({
        'class': views.ALERT_CLASS_WARNING,
        'content': 'Please input valid email.'
      })      
      
    if User.getByEmail(signup_data.get('email', '')):
      self.template_values['alerts'].append({
        'class': views.ALERT_CLASS_WARNING,
        'content': 'User with email {} has been registered.'.format(signup_data.get('email'))
      })

    if User.getByEmail(signup_data.get('email', '')):
      self.template_values['alerts'].append({
        'class': views.ALERT_CLASS_WARNING,
        'content': 'User with email {} has been registered.'.format(signup_data.get('email'))
      })
    
    if self.template_values['alerts']:
      self.template_values.update(signup_data)
      self.send_response('signup.html')
      return

    # Create user
    user = User.Create(email=signup_data.get('email'),
                       password=signup_data.get('password'))

    
    self.redirect('/')
                
