
import webapp2

from views import home, signup, signin, account, about, contact

app = webapp2.WSGIApplication([
  ('/', home.View),
  ('/signup', signup.View),
  ('/signin', signin.View),
  ('/signin/check', signin.Check),
  ('/account', account.View),
  ('/about', about.View),
  ('/contact', contact.View),
], debug=True)
