import re
from google.appengine.ext import ndb
from webapp2_extras import sessions


class Session(ndb.Model):
  username = ndb.StringProperty()
  session = ndb.StringProperty()

  @classmethod
  def Update(cls, username, session):
    key = ndb.Key('Session', session)
    if not key.get():
      entity = cls()
      entity.key = key
      entity.username = username
      entity.session = session
      entity.put()
    else:
      entity.update(username=username, session=session)
    return entity
    
  @classmethod
  def getById(cls, session):
    if session:
      key = ndb.Key('Session', session)
      return key.get()
    return None

class User(ndb.Model):
  username = ndb.StringProperty()
  fullname = ndb.StringProperty(default='')
  is_active = ndb.BooleanProperty()
  password = ndb.StringProperty()
  email = ndb.StringProperty()

  @property
  def has_valid_username(self):
    return (' ' not in self.username and
            all(ord(c) < 128 for c in self.username))

  @classmethod
  def getByUsername(cls, username):
    if username:
      key = ndb.Key('User', username)
      return key.get()

    return None
    
  @classmethod
  def Create(cls, username, password):
    entity = cls()
    entity.key = ndb.Key('User', username)
    entity.username = username
    entity.password = password
    entity.put()
    return entity

  def Update(self, **args):
    args.pop('username', None)
    for k, v in args.items():
      if hasattr(self, k):
        setattr(self, k, v)
        print self.key
    self.put()
    
  def UpdatePassword(self, current_password, new_password):
    if current_password != self.password:
      return False

    self.password = new_password
    self.put()
    return True
  
  @classmethod
  def validate_username(cls, username):
    return re.match('^[0-9a-zA-Z_-]+$', username) is not None
