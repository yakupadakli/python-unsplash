from unsplash.client import Client
from unsplash.models import Stat as StatModel


class Stat(Client):

    def __init__(self, **kwargs):
        super(Stat, self).__init__(**kwargs)

    def total(self):
        url = "/stats/total"
        result = self._get(url)
        return StatModel.parse(result)
