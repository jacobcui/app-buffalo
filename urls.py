
import webapp2

from views import index

app = webapp2.WSGIApplication([
  ('/', index.View),
], debug=True)
