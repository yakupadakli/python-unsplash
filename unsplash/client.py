import requests


class Client(object):

    def __init__(self, api, **kwargs):
        self.api = api

    def _request(self, url, method, params=None, data=None, **kwargs):
        url = "%s%s" % (self.api.base_url, url)
        headers = self.get_auth_header()
        headers.update(kwargs.get("headers", {}))
        response = requests.request(method, url, params=params, data=data, headers=headers)

        if not self.is_2xx(response.status_code):
            raise Exception(response.json().get("errors"))
        return response

    def _get(self, url, params=None, **kwargs):
        return self._request(url, "get", params=params, **kwargs)

    def _post(self, url, data=None, **kwargs):
        return self._request(url, "post", data=data, **kwargs)

    def _delete(self, url, **kwargs):
        return self._request(url, "delete", **kwargs)

    def _put(self, url, data=None, **kwargs):
        return self._request(url, "put", data=data, **kwargs)

    def get_auth_header(self):
        return {"Authorization": "Bearer %s" % self.api.access_token}

    @staticmethod
    def is_1xx(status_code):
        return 100 <= status_code <= 199

    @staticmethod
    def is_2xx(status_code):
        return 200 <= status_code <= 299

    @staticmethod
    def is_3xx(status_code):
        return 300 <= status_code <= 399

    @staticmethod
    def is_4xx(status_code):
        return 400 <= status_code <= 499

    @staticmethod
    def is_5xx(status_code):
        return 500 <= status_code <= 599
