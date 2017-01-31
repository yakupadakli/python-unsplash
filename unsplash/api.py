from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib.oauth2_session import OAuth2Session

from unsplash.photo import Photo


class Api(object):

    def __init__(self, client_id=None, client_secret=None):
        self.base_url = "https://api.unsplash.com"
        self.auth_base_url = "https://unsplash.com"
        self.access_token_url = "https://unsplash.com/oauth/token"
        self.client_id = "08ed7d70933490d02efb69d99a51c266ca7d641f45ad05063fb13d52de834495"
        self.client_secret = "e38c80a4f14f9ab6686a9ce829231da1a2372c4b90893b5e4f812c573f6bfe1c"

        self.client = BackendApplicationClient(client_id=self.client_id)
        self.oauth = OAuth2Session(client=self.client)
        self.access_token = self.get_access_token()

    def get_access_token(self):
        data = self.oauth.fetch_token(
            token_url=self.access_token_url, client_id=self.client_id, client_secret=self.client_secret
        )
        return data.get("access_token")

    def refresh_token(self):
        if not self.oauth.verify:
            self.access_token = self.get_access_token()
        return self.access_token

    @property
    def photos(self):
        return Photo(api=self)
