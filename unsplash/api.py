from unsplash.collection import Collection
from unsplash.photo import Photo
from unsplash.search import Search
from unsplash.stat import Stat
from unsplash.user import User


class Api(object):
    """Unsplash API"""

    def __init__(self, auth, api_version=None, **kwargs):
        """
        Unsplash Api Instance Constructor

        :param auth [Auth]: OAuth authentication handler
        :param api_version [string]: Api version
        :param kwargs:
        """
        self._auth = auth
        self.base_url = self._auth.BASE_API_URL
        self.base_auth_url = self._auth.BASE_AUTH_URL
        self.api_version = api_version or self._auth.DEFAULT_VERSION
        self.client_id = self._auth.client_id

    @property
    def access_token(self):
        """
        Access Token for Api
        :return:
        """
        return self._auth.access_token

    @property
    def is_authenticated(self):
        """
        Shows current Api has authenticated user or not
        :return:
        """
        return self._auth.is_authenticated

    @property
    def photo(self):
        """
        Unsplash Photo Operations

        Available methods:

        all     : All photos.
        curated : Curated photos.
        get     : Single photo.
        search  : Search photos.
        random  : Random photo or photos.
        stats   : Stats of photo.
        download: Download link.
        like    : Like photo. Requires Authentication.
        unlike  : Unlike photo. Requires Authentication.
        """
        return Photo(api=self)

    @property
    def user(self):
        """
        Unsplash User Operations

        Available methods:

        me          : Get current user. Requires Authentication.
        update      : Update current user. Requires Authentication.
        get         : Single user.
        portfolio   : Portfolio of a user.
        likes       : Liked Photos of a user.
        collections : Collections of a user.
        """
        return User(api=self)

    @property
    def search(self):
        """
        Unsplash Search Operations

        Available methods:

        photos      : Search photos.
        collections : Search collections.
        users       : Search users.
        """
        return Search(api=self)

    @property
    def collection(self):
        """
        Unsplash Photo Operations

        Available methods:

        all             : All collections.
        featured        : Featured collections.
        curated         : Curated collections.
        get             : Single collection.
        get_curated     : Single curated collection.
        photos          : All photos of a collection.
        curated_photos  : All curated photos of a collection.
        related         : Related collections of a collection.
        create          : Create collection. Requires Authentication.
        update          : Update collection. Requires Authentication.
        delete          : Delete collection. Requires Authentication.
        add_photo       : Add a photo to a collection. Requires Authentication.
        remove_photo    : remove a photo from a collection. Requires Authentication.
        """
        return Collection(api=self)

    @property
    def stat(self):
        """
        Unsplash Photo Operations

        Available methods:
        total   : Unsplash total counts
        """
        return Stat(api=self)
