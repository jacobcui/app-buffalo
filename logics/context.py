from google.appengine.api import users

def get_signout_url():
  if users.get_current_user():
    return users.create_logout_url('/')
  return '/'
    
google_signin_url = users.create_login_url('/signin/check')
