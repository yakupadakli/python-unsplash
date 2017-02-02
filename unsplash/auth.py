from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib.oauth2_session import OAuth2Session

from unsplash.photo import Photo


class Auth(object):
    BASE_API_URL = "https://api.unsplash.com"
    BASE_AUTH_URL = "https://unsplash.com"

    def __init__(self, client_id, client_secret, redirect_uri, code=None, scope=None):
        self.access_token_url = "%s/oauth/token" % self.BASE_AUTH_URL
        self.authorization_url = "%s/oauth/authorize" % self.BASE_AUTH_URL
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.token = None

        self.scope_list = [
            "public",
            "read_user",
            "write_user",
            "read_photos",
            "write_photos",
            "write_likes",
            "write_followers",
            "read_collections",
            "write_collections"
        ]

        self.oauth = OAuth2Session(client_id=self.client_id, redirect_uri=self.redirect_uri, scope=self.scope_list)
        self.access_token = self.get_access_token(code=code) if code else None

        self.client = BackendApplicationClient(client_id=self.client_id, scope=self.scope_list)
        self.public_oauth = OAuth2Session(
            client_id=self.client_id, client=self.client, redirect_uri=self.redirect_uri, scope=self.scope_list
        )
        self.public_access_token = self.get_access_token()

    def get_access_token(self, code=None):
        oauth = self.oauth if code else self.public_oauth
        data = oauth.fetch_token(
            token_url=self.access_token_url,
            client_id=self.client_id,
            client_secret=self.client_secret,
            scope=self.scope,
            code=code
        )
        self.token = data
        return data.get("access_token")

    def refresh_token(self):
        return self.access_token
