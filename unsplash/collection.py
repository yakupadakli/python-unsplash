from unsplash.client import Client


class Collection(Client):

    def __init__(self, **kwargs):
        super(Collection, self).__init__(**kwargs)

    def _all(self, url, page=1, per_page=10):
        params = {
            "page": page,
            "per_page": per_page
        }
        return self._get(url, params=params)

    def all(self, page=1, per_page=10):
        url = "/collections"
        return self._all(url, page=page, per_page=per_page)

    def featured(self, page=1, per_page=10):
        url = "/collections/featured"
        return self._all(url, page=page, per_page=per_page)

    def curated(self, page=1, per_page=10):
        url = "/collections/curated"
        return self._all(url, page=page, per_page=per_page)

    def get(self, collection_id):
        url = "/collections/%s" % collection_id
        return self._get(url)

    def get_curated(self, collection_id):
        url = "/collections/curated/%s" % collection_id
        return self._get(url)

    def photos(self, collection_id, page=1, per_page=10):
        url = "/collections/%s/photos" % collection_id
        return self._all(url, page=page, per_page=per_page)

    def curated_photos(self, collection_id, page=1, per_page=10):
        url = "/collections/curated/%s/photos" % collection_id
        return self._all(url, page=page, per_page=per_page)

    def related(self, collection_id):
        url = "/collections/%s/related" % collection_id
        return self._get(url)

    def create(self, title, description=None, private=False):
        url = "/collections"
        data = {
            "title": title,
            "description": description,
            "private": private
        }
        return self._post(url, data=data)

    def update(self, collection_id, title=None, description=None, private=False):
        url = "/collections/%s" % collection_id
        data = {
            "title": title,
            "description": description,
            "private": private
        }
        return self._put(url, data=data)

    def delete(self, collection_id):
        url = "/collections/%s" % collection_id
        return self._delete(url)

    def add_photo(self, collection_id, photo_id):
        url = "/collections/%s/add" % collection_id
        data = {
            "collection_id": collection_id,
            "photo_id": photo_id
        }
        return self._post(url, data=data)

    def remove_photo(self, collection_id, photo_id):
        url = "/collections/%s/remove" % collection_id
        data = {
            "collection_id": collection_id,
            "photo_id": photo_id
        }
        return self._delete(url, data=data)
