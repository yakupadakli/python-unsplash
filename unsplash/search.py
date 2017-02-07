from unsplash.client import Client
from unsplash.models import Photo as PhotoModel, Collection as CollectionModel, User as UserModel


class Search(Client):

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
        url = "/search/photos"
        result = self._search(url, query, page=page, per_page=per_page)
        return PhotoModel.parse_list(result)

    def collections(self, query, page=1, per_page=10):
        url = "/search/collections"
        result = self._search(url, query, page=page, per_page=per_page)
        return CollectionModel.parse_list(result)

    def users(self, query, page=1, per_page=10):
        url = "/search/users"
        result = self._search(url, query, page=page, per_page=per_page)
        return UserModel.parse_list(result)
