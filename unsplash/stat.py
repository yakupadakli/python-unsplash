from unsplash.client import Client


class Stat(Client):

    def __init__(self, **kwargs):
        super(Stat, self).__init__(**kwargs)

    def total(self):
        url = "/stats/total"
        response = self._get(url)
        return response.json()
