from unsplash.client import Client


class Photo(Client):

    def __init__(self, **kwargs):
        super(Photo, self).__init__(**kwargs)
        self.ordering_values = ["latest", "oldest", "popular"]
        self.orientation_values = ["landscape", "portrait", "squarish"]

    def _all(self, url, page=1, per_page=10, order_by="latest"):
        if order_by not in self.ordering_values:
            raise Exception()
        params = {
            "page": page,
            "per_page": per_page,
            "order_by": order_by
        }
        response = self._get(url, params=params)
        return response.json()

    def all(self, page=1, per_page=10, order_by="latest"):
        return self._all("/photos", page=page, per_page=per_page, order_by=order_by)

    def curated(self, page=1, per_page=10, order_by="latest"):
        return self._all("/photos/curated", page=page, per_page=per_page, order_by=order_by)

    def get(self, photo_id, width=None, height=None, rect=None):
        url = "/photos/%s" % photo_id
        params = {
            "width": width,
            "height": height,
            "rect": rect
        }
        response = self._get(url, params=params)
        return response.json()

    def search(self, query, category=None, orientation=None, page=1, per_page=10):
        if orientation and orientation not in self.orientation_values:
            raise Exception()
        params = {
            "query": query,
            "category": category,
            "orientation": orientation,
            "page": page,
            "per_page": per_page
        }
        url = "/photos/search"
        response = self._get(url, params=params)
        return response.json()
