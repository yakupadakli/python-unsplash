from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib.oauth2_session import OAuth2Session

from unsplash.photo import Photo


class Api(object):

    def __init__(self, auth):
        self._auth = auth
        self.base_url = self._auth.BASE_API_URL
        self.base_auth_url = self._auth.BASE_AUTH_URL
        self.is_authenticated = True if self._auth.access_token else False
        self.access_token = self._auth.access_token or self._auth.public_access_token

    @property
    def photos(self):
        return Photo(api=self)
