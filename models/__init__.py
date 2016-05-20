
from google.appengine.ext import ndb

class User(ndb.Model):
  email = ndb.StringProperty()
  password = ndb.StringProperty()
  is_active = ndb.BooleanProperty()

  @property
  def has_valid_email(self):
    if not '@' in self.email:
      return False
    return True

  @classmethod
  def getByEmail(cls, email):
    key = ndb.Key('User', email)
    return key.get()
