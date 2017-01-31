from unsplash.client import Client


class Photo(Client):

    def __init__(self, **kwargs):
        super(Photo, self).__init__(**kwargs)
        self.ordering_values = ["latest", "oldest", "popular"]

    def all(self, page=1, per_page=10, order_by="latest"):
        if order_by not in self.ordering_values:
            raise Exception()
        url = "/photos"
        params = {
            "page": page,
            "per_page": per_page,
            "order_by": order_by
        }
        response = self._get(url, params=params)
        return response.json()

    def curated(self, page=1, per_page=10, order_by="latest"):
        if order_by not in self.ordering_values:
            raise Exception()
        url = "/photos/curated"
        params = {
            "page": page,
            "per_page": per_page,
            "order_by": order_by
        }
        response = self._get(url, params=params)
        return response.json()

    def get(self, photo_id):
        url = "/photos/%s" % photo_id
        response = self._get(url)
        return response.json()
