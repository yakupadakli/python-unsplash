from unsplash.client import Client
from unsplash.models import Photo as PhotoModel, Collection as CollectionModel, User as UserModel


class Search(Client):
    """Unsplash Search operations."""

    def __init__(self, **kwargs):
        super(Search, self).__init__(**kwargs)

    def _search(self, url, query, page=1, per_page=10):
        params = {
            "query": query,
            "page": page,
            "per_page": per_page
        }
        return self._get(url, params=params)

    def photos(self, query, page=1, per_page=10):
        """
        Get a single page of photo results for a query.

        :param query [string]: Search terms.
        :param page [integer]: Page number to retrieve. (Optional; default: 1)
        :param per_page [integer]: Number of items per page. (Optional; default: 10)
        :return: [Array]: A single page of the curated Photo list.
        """
        url = "/search/photos"
        result = self._search(url, query, page=page, per_page=per_page)
        return PhotoModel.parse_list(result)

    def collections(self, query, page=1, per_page=10):
        """
        Get a single page of collection results for a query.

        :param query [string]: Search terms.
        :param page [integer]: Page number to retrieve. (Optional; default: 1)
        :param per_page [integer]: Number of items per page. (Optional; default: 10)
        :return: [Array]: A single page of the curated Collection list.
        """
        url = "/search/collections"
        result = self._search(url, query, page=page, per_page=per_page)
        return CollectionModel.parse_list(result)

    def users(self, query, page=1, per_page=10):
        """
        Get a single page of user results for a query.

        :param query [string]: Search terms.
        :param page [integer]: Page number to retrieve. (Optional; default: 1)
        :param per_page [integer]: Number of items per page. (Optional; default: 10)
        :return: [Array]: A single page of the curated User list.
        """
        url = "/search/users"
        result = self._search(url, query, page=page, per_page=per_page)
        return UserModel.parse_list(result)
