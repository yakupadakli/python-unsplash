from unsplash.client import Client


class Search(Client):

    def __init__(self, **kwargs):
        super(Search, self).__init__(**kwargs)

    def _search(self, url, query, page=1, per_page=10):
        params = {
            "query": query,
            "page": page,
            "per_page": per_page
        }
        response = self._get(url, params=params)
        return response.json()

    def photos(self, query, page=1, per_page=10):
        url = "/search/photos"
        return self._search(url, query, page=page, per_page=per_page)

    def collections(self, query, page=1, per_page=10):
        url = "/search/collections"
        return self._search(url, query, page=page, per_page=per_page)

    def users(self, query, page=1, per_page=10):
        url = "/search/users"
        return self._search(url, query, page=page, per_page=per_page)
