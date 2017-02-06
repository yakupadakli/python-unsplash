from unsplash.client import Client
from unsplash.models import Collection as CollectionModel, Photo as PhotoModel


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
        result = self._all(url, page=page, per_page=per_page)
        return CollectionModel.parse_list(result)

    def featured(self, page=1, per_page=10):
        url = "/collections/featured"
        result = self._all(url, page=page, per_page=per_page)
        return CollectionModel.parse_list(result)

    def curated(self, page=1, per_page=10):
        url = "/collections/curated"
        result = self._all(url, page=page, per_page=per_page)
        return CollectionModel.parse_list(result)

    def get(self, collection_id):
        url = "/collections/%s" % collection_id
        result = self._get(url)
        return CollectionModel.parse(result)

    def get_curated(self, collection_id):
        url = "/collections/curated/%s" % collection_id
        result = self._get(url)
        return CollectionModel.parse(result)

    def photos(self, collection_id, page=1, per_page=10):
        url = "/collections/%s/photos" % collection_id
        result = self._all(url, page=page, per_page=per_page)
        return PhotoModel.parse_list(result)

    def curated_photos(self, collection_id, page=1, per_page=10):
        url = "/collections/curated/%s/photos" % collection_id
        result = self._all(url, page=page, per_page=per_page)
        return PhotoModel.parse_list(result)

    def related(self, collection_id):
        url = "/collections/%s/related" % collection_id
        result = self._get(url)
        return CollectionModel.parse_list(result)

    def create(self, title, description=None, private=False):
        url = "/collections"
        data = {
            "title": title,
            "description": description,
            "private": private
        }
        result = self._post(url, data=data)
        return CollectionModel.parse(result)

    def update(self, collection_id, title=None, description=None, private=False):
        url = "/collections/%s" % collection_id
        data = {
            "title": title,
            "description": description,
            "private": private
        }
        result = self._put(url, data=data)
        return CollectionModel.parse(result)

    def delete(self, collection_id):
        url = "/collections/%s" % collection_id
        return self._delete(url)

    def add_photo(self, collection_id, photo_id):
        url = "/collections/%s/add" % collection_id
        data = {
            "collection_id": collection_id,
            "photo_id": photo_id
        }
        result = self._post(url, data=data)
        return CollectionModel.parse(result.get("collection")), PhotoModel.parse(result.get("photo"))

    def remove_photo(self, collection_id, photo_id):
        url = "/collections/%s/remove" % collection_id
        data = {
            "collection_id": collection_id,
            "photo_id": photo_id
        }
        result = self._delete(url, data=data)
        return CollectionModel.parse(result.get("collection")), PhotoModel.parse(result.get("photo"))
