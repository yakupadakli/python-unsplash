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
        self.is_authenticated = True if self._auth.access_token else False
        self.access_token = self._auth.access_token or self._auth.public_access_token

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
