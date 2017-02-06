from unsplash.client import Client
from unsplash.models import User as UserModel, Collection as CollectionModel, Link as LinkModel, Photo as PhotoModel


class User(Client):

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.ordering_values = ["latest", "oldest", "popular"]

    def me(self):
        url = "/me"
        result = self._get(url)
        return UserModel.parse(result)

    def update(self, **kwargs):
        url = "/me"
        result = self._put(url, data=kwargs)
        return UserModel.parse(result)

    def get(self, username, width=None, height=None):
        url = "/users/{username}".format(username=username)
        params = {
            "w": width,
            "h": height
        }
        result = self._get(url, params=params)
        return UserModel.parse(result)

    def portfolio(self, username):
        url = "/users/{username}/portfolio".format(username=username)
        result = self._get(url)
        return LinkModel.parse(result)

    def _photos(self, url, username, page=1, per_page=10, order_by="latest"):
        if order_by not in self.ordering_values:
            raise Exception()
        params = {
            "page": page,
            "per_page": per_page,
            "order_by": order_by
        }
        result = self._get(url, params=params)
        return PhotoModel.parse_list(result)

    def photos(self, username, page=1, per_page=10, order_by="latest"):
        url = "/users/{username}/photos".format(username=username)
        return self._photos(url, username, page=page, per_page=per_page, order_by=order_by)

    def likes(self, username, page=1, per_page=10, order_by="latest"):
        url = "/users/{username}/likes".format(username=username)
        return self._photos(url, username, page=page, per_page=per_page, order_by=order_by)

    def collections(self, username, page=1, per_page=10):
        url = "/users/{username}/collections".format(username=username)
        params = {
            "page": page,
            "per_page": per_page
        }
        result = self._get(url, params=params)
        return CollectionModel.parse_list(result)
