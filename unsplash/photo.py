# coding=utf-8

from unsplash.client import Client
from unsplash.models import Photo as PhotoModel
from unsplash.models import Stat as StatModel


class Photo(Client):
    """
    Unsplash Photo operations.

    Photos have the following link relations:
    self: API location of this photo.
    html: HTML location of this photo.
    download: Download location of this photo.
    """

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
        """
        Get a single page from the list of all photos.

        :param page [integer]: Page number to retrieve. (Optional; default: 1)
        :param per_page [integer]: Number of items per page. (Optional; default: 10)
        :param order_by [string]: How to sort the photos. Optional.
        (Valid values: latest, oldest, popular; default: latest)
        :return: [Array]: A single page of the Photo list.
        """
        return self._all("/photos", page=page, per_page=per_page, order_by=order_by)

    def curated(self, page=1, per_page=10, order_by="latest"):
        """
        Get a single page from the list of the curated photos (front-page’s photos).

        :param page [integer]: Page number to retrieve. (Optional; default: 1)
        :param per_page [integer]: Number of items per page. (Optional; default: 10)
        :param order_by [string]: How to sort the photos. Optional.
        (Valid values: latest, oldest, popular; default: latest)
        :return: [Array]: A single page of the curated Photo list.
        """
        return self._all("/photos/curated", page=page, per_page=per_page, order_by=order_by)

    def get(self, photo_id, width=None, height=None, rect=None):
        """
        Retrieve a single photo.

        Note: Supplying the optional w or h parameters will result
        in the custom photo URL being added to the 'urls' object:

        :param photo_id [string]: The photo’s ID. Required.
        :param width [integer]: Image width in pixels.
        :param height [integer]: Image height in pixels.
        :param rect [string]: 4 comma-separated integers representing x, y, width, height of the cropped rectangle.
        :return: [Photo]: The Unsplash Photo.
        """
        url = "/photos/%s" % photo_id
        params = {
            "w": width,
            "h": height,
            "rect": rect
        }
        result = self._get(url, params=params)
        return PhotoModel.parse(result)

    def search(self, query, category=None, orientation=None, page=1, per_page=10):
        """
        Get a single page from a photo search.
        Optionally limit your search to a set of categories by supplying the category ID’s.

        Note: If supplying multiple category ID’s,
        the resulting photos will be those that match all of the given categories,
        not ones that match any category.

        :param query [string]: Search terms.
        :param category [string]: Category ID(‘s) to filter search. If multiple, comma-separated. (deprecated)
        :param orientation [string]: Filter search results by photo orientation.
        Valid values are landscape, portrait, and squarish.
        :param page [integer]: Page number to retrieve. (Optional; default: 1)
        :param per_page [integer]: Number of items per page. (Optional; default: 10)
        :return: [Array]: A single page of the curated Photo list.
        :raise UnsplashError: If the given orientation is not in the default orientation values.
        """
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
        """
        Retrieve a single random photo, given optional filters.

        Note: If supplying multiple category ID’s,
        the resulting photos will be those that
        match all of the given categories, not ones that match any category.

        Note: You can’t use the collections and query parameters in the same request

        Note: When supplying a count parameter
        - and only then - the response will be an array of photos,
        even if the value of count is 1.

        All parameters are optional, and can be combined to narrow
        the pool of photos from which a random one will be chosen.

        :param count [integer]: The number of photos to return. (Default: 1; max: 30)
        :param category: Category ID(‘s) to filter selection. If multiple, comma-separated. (deprecated)
        :param collections: Public collection ID(‘s) to filter selection. If multiple, comma-separated
        :param featured: Limit selection to featured photos.
        :param username: 	Limit selection to a single user.
        :param query: Limit selection to photos matching a search term.
        :param w: Image width in pixels.
        :param h: Image height in pixels.
        :param orientation: Filter search results by photo orientation.
        Valid values are landscape, portrait, and squarish.
        :return: [Array] or [Photo]: A single page of the curated Photo list or The Unsplash Photo. .
        :raise UnsplashError: If the given orientation is not in the default orientation values.
        """
        kwargs.update({"count": count})
        orientation = kwargs.get("orientation", None)
        if orientation and orientation not in self.orientation_values:
            raise Exception()
        url = "/photos/random"
        result = self._get(url, params=kwargs)
        return PhotoModel.parse_list(result)

    def stats(self, photo_id):
        """
        Retrieve a single photo’s stats.

        :param photo_id [string]: The photo’s ID. Required.
        :return: [Stat]: The Unsplash Stat.
        """
        url = "/photos/%s/stats" % photo_id
        result = self._get(url)
        return StatModel.parse(result)

    # ToDO
    def download(self, photo_id):
        """
        Retrieve a single photo’s download link.

        Preferably hit this endpoint if a photo is downloaded in your application for use
        (example: to be displayed on a blog article, to be shared on social media, to be remixed, etc.).

        :param photo_id [string]: The photo’s ID. Required.
        :return: [Dictionary]: Dictionary has download url.
        """
        url = "/photos/%s/download" % photo_id
        return self._get(url)

    # ToDo
    def update(self, photo_id, **kwargs):
        url = "/photos/%s" % photo_id
        return self._put(url, data=kwargs)

    def like(self, photo_id):
        """
        Like a photo on behalf of the logged-in user.
        This requires the 'write_likes' scope.

        Note: This action is idempotent; sending the POST request
        to a single photo multiple times has no additional effect.

        :param photo_id [string]: The photo’s ID. Required.
        :return: [Photo]: The Unsplash Photo.
        """
        url = "/photos/%s/like" % photo_id
        result = self._post(url)
        return PhotoModel.parse(result)

    def unlike(self, photo_id):
        """
        Remove a user’s like of a photo.

        Note: This action is idempotent; sending the DELETE request
        to a single photo multiple times has no additional effect.

        :param photo_id [string]: The photo’s ID. Required.
        :return: [Photo]: The Unsplash Photo.
        """
        url = "/photos/%s/like" % photo_id
        result = self._delete(url)
        return PhotoModel.parse(result)
