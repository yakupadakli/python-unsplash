from unsplash.client import Client


class User(Client):

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.ordering_values = ["latest", "oldest", "popular"]

    def me(self):
        url = "/me"
        response = self._get(url)
        return response.json()

    def update(self, **kwargs):
        url = "/me"
        response = self._put(url, data=kwargs)
        return response.json()

    def get(self, username, width=None, height=None):
        url = "/users/{username}".format(username=username)
        params = {
            "w": width,
            "h": height
        }
        response = self._get(url, params=params)
        return response.json()

    def portfolio(self, username):
        url = "/users/{username}/portfolio".format(username=username)
        response = self._get(url)
        return response.json()

    def _photos(self, url, username, page=1, per_page=10, order_by="latest"):
        if order_by not in self.ordering_values:
            raise Exception()
        params = {
            "page": page,
            "per_page": per_page,
            "order_by": order_by
        }
        response = self._get(url, params=params)
        return response.json()

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
        response = self._get(url, params=params)
        return response.json()
