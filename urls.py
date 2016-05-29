
import webapp2

from views import about
from views import account
from views import contact
from views import home
from views import signin
from views import signout
from views import signup

config = {}
config['webapp2_extras.sessions'] = {
  'secret_key': '--1--',
  'cookie_name': 'EMAB',
}

ROOT = '/'
SIGNIN = '/signin'
ACCOUNT_PASSWORD = '/account/password'

app = webapp2.WSGIApplication([
  (ROOT, home.View),
  ('/about', about.View),
  ('/account', account.View),
  ('/account/basic', account.Basic),
  (ACCOUNT_PASSWORD, account.Password),
  ('/contact', contact.View),
  (SIGNIN, signin.View),
  ('/signin/check', signin.Check),
  ('/signout', signout.View),
  ('/signup', signup.View),
], debug=True, config=config)

