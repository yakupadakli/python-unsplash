import requests

from unsplash.errors import UnsplashError


class Client(object):
    """
    Unsplash Client

    HTTP connections to and communication with the Unsplash API.
    """

    def __init__(self, api, **kwargs):
        self.api = api

    def _request(self, url, method, params=None, data=None, **kwargs):
        url = "%s%s" % (self.api.base_url, url)
        headers = self.get_auth_header()
        headers.update(self.get_version_header())
        headers.update(kwargs.pop("headers", {}))

        try:
            response = requests.request(method, url, params=params, data=data, headers=headers, **kwargs)
        except Exception, e:
            raise UnsplashError("Connection error: %s" % e)

        if not self._is_2xx(response.status_code):
            errors = response.json().get("errors")
            raise UnsplashError(errors[0] if errors else None)
        try:
            result = response.json()
        except ValueError:
            result = None
        return result

    def _get(self, url, params=None, **kwargs):
        return self._request(url, "get", params=params, **kwargs)

    def _post(self, url, data=None, **kwargs):
        return self._request(url, "post", data=data, **kwargs)

    def _delete(self, url, **kwargs):
        return self._request(url, "delete", **kwargs)

    def _put(self, url, data=None, **kwargs):
        return self._request(url, "put", data=data, **kwargs)

    def get_auth_header(self):
        """
        Getting the authorization header according to the authentication procedure

        :return [dict]: Authorization header
        """
        if self.api.is_authenticated:
            return {"Authorization": "Bearer %s" % self.api.access_token}
        return {"Authorization": "Client-ID %s" % self.api.client_id}

    def get_version_header(self):
        """
        Getting Version header

        :return [dict]: Accept-Version header
        """
        return {"Accept-Version": self.api.api_version}

    @staticmethod
    def _is_1xx(status_code):
        return 100 <= status_code <= 199

    @staticmethod
    def _is_2xx(status_code):
        return 200 <= status_code <= 299

    @staticmethod
    def _is_3xx(status_code):
        return 300 <= status_code <= 399

    @staticmethod
    def _is_4xx(status_code):
        return 400 <= status_code <= 499

    @staticmethod
    def _is_5xx(status_code):
        return 500 <= status_code <= 599
