
import webapp2

from views import index, signup, signin

app = webapp2.WSGIApplication([
  ('/', index.View),
  ('/signup', signup.View),
  ('/signin', signin.View),
], debug=True)
