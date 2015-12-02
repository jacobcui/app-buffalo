from protorpc import messages

class UserInfo(messages.Message):
  nickname = messages.StringField(1)
  login_url = messages.StringField(2)

class SysInfo(messages.Message):
  current_dir = messages.StringField(1)
  name = messages.StringField(2)
  platform = messages.StringField(3)
  version = messages.StringField(4)
  path_env = messages.StringField(5)
  sizeof_int = messages.IntegerField(6)
  sizeof_long = messages.IntegerField(7)

class HeaderMessage(messages.Message):
  name = messages.StringField(1)
  value = messages.StringField(2)

class RequestInfo(messages.Message):
  remote_address = messages.StringField(1)
  server_port = messages.IntegerField(2)
  http_method = messages.StringField(3)
  service_path = messages.StringField(4)
  headers = messages.MessageField(HeaderMessage, 5, repeated=True)
