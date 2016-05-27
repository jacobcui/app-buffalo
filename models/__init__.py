
from google.appengine.ext import ndb
from webapp2_extras import sessions

class Session(ndb.Model):
  email = ndb.StringProperty()
  session = ndb.StringProperty()

  @classmethod
  def Update(cls, email, session):
    key = ndb.Key('Session', session)
    if not key.get():
      entity = cls()
      entity.key = key
      entity.email = email
      entity.session = session
      entity.put()
    else:
      entity.update(email=email, session=session)
    return entity
    
  @classmethod
  def getById(cls, session):
    if session:
      key = ndb.Key('Session', session)
      return key.get()
    return None

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
