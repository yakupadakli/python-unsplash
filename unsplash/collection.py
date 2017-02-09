# coding=utf-8

from unsplash.client import Client
from unsplash.models import Collection as CollectionModel, Photo as PhotoModel


class Collection(Client):
    """
    Unsplash Collection operations.

    Collections have the following link relations:
    self: API location of this collection.
    html: HTML location of this collection.
    photos:	API location of this collection’s photos.
    related: API location of this collection’s related collections. (Non-curated collections only)
    download: Download location of this collection’s zip file. (Curated collections only)
    """

    def __init__(self, **kwargs):
        super(Collection, self).__init__(**kwargs)

    def _all(self, url, page=1, per_page=10):
        params = {
            "page": page,
            "per_page": per_page
        }
        return self._get(url, params=params)

    def all(self, page=1, per_page=10):
        """
        Get a single page from the list of all collections.

        :param page [integer]: Page number to retrieve. (Optional; default: 1)
        :param per_page [integer]: Number of items per page. (Optional; default: 10)
        :return: [Array]: A single page of the Collection list.
        """
        url = "/collections"
        result = self._all(url, page=page, per_page=per_page)
        return CollectionModel.parse_list(result)

    def featured(self, page=1, per_page=10):
        """
        Get a single page from the list of featured collections.

        :param page [integer]: Page number to retrieve. (Optional; default: 1)
        :param per_page [integer]: Number of items per page. (Optional; default: 10)
        :return: [Array]: A single page of the Collection list.
        """
        url = "/collections/featured"
        result = self._all(url, page=page, per_page=per_page)
        return CollectionModel.parse_list(result)

    def curated(self, page=1, per_page=10):
        """
        Get a single page from the list of curated collections.

        :param page [integer]: Page number to retrieve. (Optional; default: 1)
        :param per_page [integer]: Number of items per page. (Optional; default: 10)
        :return: [Array]: A single page of the Collection list.
        """
        url = "/collections/curated"
        result = self._all(url, page=page, per_page=per_page)
        return CollectionModel.parse_list(result)

    def get(self, collection_id):
        """
        Retrieve a single collection.
        To view a user’s private collections, the 'read_collections' scope is required.

        :param collection_id [string]: The collections’s ID. Required.
        :return: [Collection]: The Unsplash Collection.
        """
        url = "/collections/%s" % collection_id
        result = self._get(url)
        return CollectionModel.parse(result)

    def get_curated(self, collection_id):
        """
        Retrieve a single curated collection.
        To view a user’s private collections, the 'read_collections' scope is required.

        :param collection_id [string]: The collections’s ID. Required.
        :return: [Collection]: The Unsplash Collection.
        """
        url = "/collections/curated/%s" % collection_id
        result = self._get(url)
        return CollectionModel.parse(result)

    def photos(self, collection_id, page=1, per_page=10):
        """
        Retrieve a collection’s photos.

        :param collection_id [string]: The collection’s ID. Required.
        :param page [integer]: Page number to retrieve. (Optional; default: 1)
        :param per_page [integer]: Number of items per page. (Optional; default: 10)
        :return: [Array]: A single page of the Photo list.
        """
        url = "/collections/%s/photos" % collection_id
        result = self._all(url, page=page, per_page=per_page)
        return PhotoModel.parse_list(result)

    def curated_photos(self, collection_id, page=1, per_page=10):
        """
        Retrieve a collection’s curated photos.

        :param collection_id [string]: The collection’s ID. Required.
        :param page [integer]: Page number to retrieve. (Optional; default: 1)
        :param per_page [integer]: Number of items per page. (Optional; default: 10)
        :return: [Array]: A single page of the Photo list.
        """
        url = "/collections/curated/%s/photos" % collection_id
        result = self._all(url, page=page, per_page=per_page)
        return PhotoModel.parse_list(result)

    def related(self, collection_id):
        """
        Retrieve a list of collections related to this one.

        :param collection_id [string]: The collection’s ID. Required.
        :return: [Array]: A single page of the Collection list.
        """
        url = "/collections/%s/related" % collection_id
        result = self._get(url)
        return CollectionModel.parse_list(result)

    def create(self, title, description=None, private=False):
        """
        Create a new collection.
        This requires the 'write_collections' scope.

        :param title [string]: The title of the collection. (Required.)
        :param description [string]: The collection’s description. (Optional.)
        :param private [boolean]: Whether to make this collection private. (Optional; default false).
        :return: [Collection]: The Unsplash Collection.
        """
        url = "/collections"
        data = {
            "title": title,
            "description": description,
            "private": private
        }
        result = self._post(url, data=data)
        return CollectionModel.parse(result)

    def update(self, collection_id, title=None, description=None, private=False):
        """
        Update an existing collection belonging to the logged-in user.
        This requires the 'write_collections' scope.

        :param collection_id [string]: The collection’s ID. Required.
        :param title [string]: The title of the collection. (Required.)
        :param description [string]: The collection’s description. (Optional.)
        :param private [boolean]: Whether to make this collection private. (Optional; default false).
        :return: [Collection]: The Unsplash Collection.
        """
        url = "/collections/%s" % collection_id
        data = {
            "title": title,
            "description": description,
            "private": private
        }
        result = self._put(url, data=data)
        return CollectionModel.parse(result)

    def delete(self, collection_id):
        """
        Delete a collection belonging to the logged-in user.
        This requires the 'write_collections' scope.

        :param collection_id [string]: The collection’s ID. Required.
        :return:
        """
        url = "/collections/%s" % collection_id
        return self._delete(url)

    def add_photo(self, collection_id, photo_id):
        """
        Add a photo to one of the logged-in user’s collections.
        Requires the 'write_collections' scope.

        Note: If the photo is already in the collection, this acion has no effect.

        :param collection_id [string]: The collection’s ID. Required.
        :param photo_id [string]: The photo’s ID. Required.
        :return: [Tuple]: The Unsplash Collection and Photo
        """
        url = "/collections/%s/add" % collection_id
        data = {
            "collection_id": collection_id,
            "photo_id": photo_id
        }
        result = self._post(url, data=data) or {}
        return CollectionModel.parse(result.get("collection")), PhotoModel.parse(result.get("photo"))

    def remove_photo(self, collection_id, photo_id):
        """
        Remove a photo from one of the logged-in user’s collections.
        Requires the 'write_collections' scope.

        :param collection_id [string]: The collection’s ID. Required.
        :param photo_id [string]: The photo’s ID. Required.
        :return: [Tuple]: The Unsplash Collection and Photo
        """
        url = "/collections/%s/remove" % collection_id
        data = {
            "collection_id": collection_id,
            "photo_id": photo_id
        }
        result = self._delete(url, data=data) or {}
        return CollectionModel.parse(result.get("collection")), PhotoModel.parse(result.get("photo"))
