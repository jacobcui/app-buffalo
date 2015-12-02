"""Hello World API implemented using Google Cloud Endpoints.

Defined here are the ProtoRPC messages needed to define Schemas for methods
as well as those methods defined in an API.
"""


import os
import sys
# https://cloud.google.com/appengine/docs/python/refdocs/google.appengine.tools.devappserver2.endpoints
import endpoints
# https://github.com/google/protorpc
from protorpc import messages
from protorpc import message_types
from protorpc import remote
# https://cloud.google.com/appengine/docs/python/refdocs/google.appengine.api#submodules
from google.appengine.api import users
from google.appengine.api import request_info

from messages import UserInfo, SysInfo
from messages import  HeaderMessage, RequestInfo

WEB_CLIENT_ID = '38883641786-ejhsrftupsubehvqirj7ou5qsn2q7obp.apps.googleusercontent.com'
ANDROID_CLIENT_ID = 'replace this with your Android client ID'
IOS_CLIENT_ID = 'replace this with your iOS client ID'
ANDROID_AUDIENCE = WEB_CLIENT_ID


@endpoints.api(name='service', version='v1',
               allowed_client_ids=[WEB_CLIENT_ID,  endpoints.API_EXPLORER_CLIENT_ID],
               audiences=[ANDROID_AUDIENCE],
               scopes=[endpoints.EMAIL_SCOPE])
class ServiceApi(remote.Service):
  """SystemInfo API v1."""

  @endpoints.method(message_types.VoidMessage,
                    SysInfo,
                    path='system/getinfo',
                    http_method='GET',
                    name='system.getSysInfo')
  def getSysInfo(self, unused_request):
    return_message = SysInfo(
      current_dir=os.path.realpath(__file__),
      name=os.name,
      platform=sys.platform,
      version=sys.version,
      path_env=':'.join(sys.path),
      sizeof_int=sys.getsizeof(1),
      sizeof_long=sys.getsizeof(1L)
    )
    return return_message

  @endpoints.method(message_types.VoidMessage,
                    RequestInfo,
                    path='system/getrequestinfo',
                    http_method='GET',
                    name='system.getRequestInfo')
  def getRequestInfo(self, unused_request):
    # HttpRequestState
    return_message = RequestInfo(
      remote_address = self.request_state.remote_address,
      server_port = self.request_state.server_port,
      http_method = self.request_state.http_method,
      service_path = self.request_state.service_path,
      headers = [HeaderMessage(name=name, value=str(value))
                 for name, value in self.request_state.headers.items()]
    )

    return return_message


  @endpoints.method(message_types.VoidMessage,
                    UserInfo,
                    path='user/getinfo',
                    http_method='GET',
                    name='user.getUserInfo')
  def getUserInfo(self, unused_request):
    nickname = ''
    user = users.get_current_user()
    if user:
      nickname = user.nickname()

    return_message = UserInfo(
      nickname = user.nickname(),
      login_url = users.create_login_url(),
    )
    return return_message

server = endpoints.api_server([ServiceApi])
