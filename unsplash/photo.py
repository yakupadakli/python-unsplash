from unsplash.client import Client
from unsplash.models import Photo as PhotoModel
from unsplash.models import Stat as StatModel


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
        result = self._get(url, params=params)
        return PhotoModel.parse_list(result)

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
        result = self._get(url, params=params)
        return PhotoModel.parse(result)

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
        result = self._get(url, params=params)
        return PhotoModel.parse_list(result)

    def random(self, count=1, **kwargs):
        kwargs.update({"count": count})
        orientation = kwargs.get("orientation", None)
        if orientation and orientation not in self.orientation_values:
            raise Exception()
        url = "/photos/random"
        result = self._get(url, params=kwargs)
        return PhotoModel.parse_list(result) if len(result) > 1 else PhotoModel.parse(result)

    def stats(self, photo_id):
        url = "/photos/%s/stats" % photo_id
        result = self._get(url)
        return StatModel.parse(result)

    # ToDO
    def download(self, photo_id):
        url = "/photos/%s/download" % photo_id
        return self._get(url)

    # ToDo
    def update(self, photo_id, **kwargs):
        url = "/photos/%s" % photo_id
        return self._put(url, data=kwargs)

    def like(self, photo_id):
        url = "/photos/%s/like" % photo_id
        result = self._post(url)
        return PhotoModel.parse(result)

    def unlike(self, photo_id):
        url = "/photos/%s/like" % photo_id
        result = self._delete(url)
        return PhotoModel.parse(result)
