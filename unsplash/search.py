from unsplash import messages
from unsplash.client import Client
from unsplash.enums import Color
from unsplash.models import Photo as PhotoModel, Collection as CollectionModel, User as UserModel


class Search(Client):
    """Unsplash Search operations."""

    def __init__(self, **kwargs):
        super(Search, self).__init__(**kwargs)
        self.colors = [
            Color.black_and_white.value,
            Color.black.value,
            Color.white.value,
            Color.yellow.value,
            Color.orange.value,
            Color.red.value,
            Color.purple.value,
            Color.magenta.value,
            Color.green.value,
            Color.teal.value,
            Color.blue.value,
        ]


    def _search(self, url, query, color=None, page=1, per_page=10):
        params = {
            "query": query,
            "page": page,
            "per_page": per_page,
            "color": color,
        }
        return self._get(url, params=params)

    def photos(self, query, page=1, per_page=10, color=None):
        """
        Get a single page of photo results for a query.

        :param query [string]: Search terms.
        :param page [integer]: Page number to retrieve. (Optional; default: 1)
        :param per_page [integer]: Number of items per page. (Optional; default: 10)
        :return: [dict]: {u'total': 0, u'total_pages': 0, u'results': [Photo]}
        """
        url = "/search/photos"
        if color and color not in self.colors:
            raise UnsplashError(messages.color_not_valid_error)

        data = self._search(url, query, color=color, page=page, per_page=per_page)
        data["results"] = PhotoModel.parse_list(data.get("results"))
        return data

    def collections(self, query, page=1, per_page=10):
        """
        Get a single page of collection results for a query.

        :param query [string]: Search terms.
        :param page [integer]: Page number to retrieve. (Optional; default: 1)
        :param per_page [integer]: Number of items per page. (Optional; default: 10)
        :return: [dict]: {u'total': 0, u'total_pages': 0, u'results': [Collection]}
        """
        url = "/search/collections"
        data = self._search(url, query, page=page, per_page=per_page)
        data["results"] = CollectionModel.parse_list(data.get("results"))
        return data

    def users(self, query, page=1, per_page=10):
        """
        Get a single page of user results for a query.

        :param query [string]: Search terms.
        :param page [integer]: Page number to retrieve. (Optional; default: 1)
        :param per_page [integer]: Number of items per page. (Optional; default: 10)
        :return: [dict]: {u'total': 0, u'total_pages': 0, u'results': [User]}
        """
        url = "/search/users"
        data = self._search(url, query, page=page, per_page=per_page)
        data["results"] = UserModel.parse_list(data.get("results"))
        return data
