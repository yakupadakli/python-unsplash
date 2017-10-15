import os
import unittest

from unsplash.auth import Auth
from unsplash.api import Api

SKIP_TEST = True

client_id = os.environ.get('CLIENT_ID', '')
client_secret = os.environ.get('CLIENT_SECRET', '')
redirect_uri = os.environ.get('REDIRECT_URI', '')

# Sample Authorization code
code = os.environ.get("UNSPLASH_CODE", '')

# Sample token
token = {
    u'access_token': u'f7cb80ed7ac6f32720b30cf664cb09393479dbdcd8a277e92ae1ed3529ab60e4',
    u'created_at': 1486560652,
    u'refresh_token': u'8f6484c0f34da29f89d1ae5e5753534636d619338c3b980a63156282504decdf',
    u'scope': [u'public',
               u'read_user',
               u'write_user',
               u'read_photos',
               u'write_photos',
               u'write_likes',
               u'write_followers',
               u'read_collections',
               u'write_collections'],
    u'token_type': u'bearer'
}

scope = [
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


class UnsplashTestCase(unittest.TestCase):
    default_user_name = u'yakupa'
    is_authenticated = False
    scope = scope
    token = token
    code = code

    def setUp(self):
        if self.token:
            self.auth = Auth(client_id, client_secret, redirect_uri, scope=scope, token=token)
            self.is_authenticated = True
        elif self.code:
            self.auth = Auth(client_id, client_secret, redirect_uri, scope=scope, code=code)
            self.is_authenticated = True
        else:
            self.auth = Auth(client_id, client_secret, redirect_uri, scope=scope)
        self.api = Api(self.auth)
