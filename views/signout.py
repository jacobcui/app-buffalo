"""Signin page."""

import views
from views import BaseView
from models import User


class View(BaseView):

  def get(self):
    self.template_values['page_name'] = 'signout'
    self.redirect(self.signOutCurrentUser())
