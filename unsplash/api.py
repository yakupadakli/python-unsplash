from unsplash.collection import Collection
from unsplash.photo import Photo
from unsplash.search import Search
from unsplash.stat import Stat
from unsplash.user import User


class Api(object):

    def __init__(self, auth):
        self._auth = auth
        self.base_url = self._auth.BASE_API_URL
        self.base_auth_url = self._auth.BASE_AUTH_URL

    @property
    def access_token(self):
        return self._auth.access_token

    @property
    def is_authenticated(self):
        return self._auth.oauth.authorized

    @property
    def photo(self):
        return Photo(api=self)

    @property
    def user(self):
        return User(api=self)

    @property
    def search(self):
        return Search(api=self)

    @property
    def collection(self):
        return Collection(api=self)

    @property
    def stat(self):
        return Stat(api=self)
