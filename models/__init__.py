
from google.appengine.api import users
from google.appengine.ext import ndb

class User(ndb.Model):
  username = ndb.StringProperty()
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

  @classmethod
  def getByEmail(cls, email):
    key = ndb.Key('User', email)
    return key.get()

  @classmethod
  def Create(cls, email, password):
    entity = cls()
    entity.key = ndb.Key('User', email)
    entity.email = email
    entity.password = password
    entity.put()
    return entity

  @classmethod
  def getCurrentUser(cls)
