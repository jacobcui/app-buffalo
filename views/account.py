"""Landing page."""


from models import User
from views import BaseView
import settings
import urls
import views

CURRENT_PASSWORD = 'current_password'
PASSWORD = 'password'
PASSWORD_CONFIRMATION = 'password_confirmation'


class View(BaseView):
  """Index/Landing page view."""

  @BaseView.login_required
  def get(self):
    self.template_values['page_name'] = 'account/basic'
    self.send_response('account.html')

class Password(BaseView):
  @BaseView.login_required
  def get(self):
    self.template_values['page_name'] = 'account/password'
    self.send_response('account.html')

  @BaseView.login_required
  def post(self):

    self.template_values['page_name'] = 'account/password'
    passwords = dict(self.request.POST)

    if not self.verify_recaptcha():
      self.template_values['alerts'].append({
        'class': views.ALERT_CLASS_WARNING,
        'content': 'Please check reCAPTCHA input.'
      })
      self.template_values.update(passwords)
      self.send_response('account.html')
      return

    current_user = self.user
    if not current_user:
      self.redirect(urls.SIGNIN)
      return

    for field in ['current_password', 'password', 'password_confirmation']:
      value = passwords.get(field, '').strip()

      if not value:
        self.template_values['alerts'].append(
          {
            'class': views.ALERT_CLASS_WARNING,
            'content': ("{} can't be empty."
                        .format(
                          field.capitalize().replace('_', ' ')))
          })

    if current_user.password != passwords.get(CURRENT_PASSWORD, ''):
      self.template_values['alerts'].append({
        'class': views.ALERT_CLASS_WARNING,
        'content': 'For security reasons, please fill in correct current password.'
      })

    if len(passwords.get('password', '')) < 4:
      self.template_values['alerts'].append({
        'class': views.ALERT_CLASS_WARNING,
        'content': 'Please ensure password is longer than 4 characters.'
      })
      
    if (passwords.get('password', '') !=
        passwords.get('password_confirmation', '')):
      self.template_values['alerts'].append({
        'class': views.ALERT_CLASS_WARNING,
        'content': 'Please ensure New Password and Password Confirmation are the same.'
      })

    if self.template_values['alerts']:
      self.template_values.update(passwords)
      self.send_response('account.html')
      return

    result = current_user.UpdatePassword(passwords[CURRENT_PASSWORD], passwords[PASSWORD])

    if result is False:
      self.template_values['alerts'].append({
        'class': views.ALERT_CLASS_WARNING,
        'content': 'For security reasons, please fill in correct current password.'
      })
    else:
      self.template_values['alerts'].append({
        'class': views.ALERT_CLASS_WARNING,
        'content': 'Password updated successfully.'
      })
      
    self.template_values.update(passwords)
    self.send_response('account.html')
    

class Basic(BaseView):
  @BaseView.login_required
  def post(self):
    self.template_values['page_name'] = 'account/basic'
    if not self.verify_recaptcha():
      self.template_values['alerts'].append({
        'class': views.ALERT_CLASS_WARNING,
        'content': 'Please check reCAPTCHA input.'
      })
      self.send_response('account.html')
    else:
      # Already signed in.
      data_to_update = {}
      for field in ['email', 'fullname']:
        if self.request.get(field):
          field_data = self.request.get(field)
          if field == 'email':
            field_data = field_data.lower()
            field_data = field_data.strip()
            # Whether the email has been registered.
            user_entity = User.getByEmail(field_data)
            if user_entity and user_entity.username != self.user.username:
              self.template_values['alerts'].append({
                'class': views.ALERT_CLASS_WARNING,
                'content': 'Email {} has been used by other user.'.format(field_data)
              })
          data_to_update[field] = field_data
      
      if self.template_values['alerts']:
        self.send_response('account.html')
      else:
        self.user.Update(**data_to_update)
        self.redirect('/account')
