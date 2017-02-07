# coding=utf-8

from unsplash.client import Client
from unsplash.models import User as UserModel, Collection as CollectionModel, Link as LinkModel, Photo as PhotoModel


class User(Client):
    """
    Unsplash User operations.

    Users have the following link relations:

    self: API location of this user.
    html: HTML location of this user.
    photos: API location of this user’s photos.
    portfolio: API location of this user’s external portfolio.
    followers: API location of this user’s followers.
    following: API location of users this user is following.
    """

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.ordering_values = ["latest", "oldest", "popular"]

    def me(self):
        """
        Get the currently-logged in user.

        Note: To access a user’s private data,
        the user is required to authorize the 'read_user' scope.
        Without it, this request will return a '403 Forbidden' response.

        Note: Without a Bearer token (i.e. using a Client-ID token)
        this request will return a '401 Unauthorized' response.

        :return: [User]: The Unsplash User.
        """
        url = "/me"
        result = self._get(url)
        return UserModel.parse(result)

    def update(self, **kwargs):
        """
        Update the currently-logged in user.

        Note: This action requires the write_user scope.
        Without it, it will return a 403 Forbidden response.

        All parameters are optional.
        :param username [string]: Username.
        :param first_name [string]: First name.
        :param last_name [string]: Last name.
        :param email [string]: Email.
        :param url [string]: Portfolio/personal URL.
        :param location [string]: 	Location.
        :param bio [string]: About/bio.
        :param instagram_username [string]: Instagram username.
        :return: [User]: The Unsplash User.
        """
        url = "/me"
        result = self._put(url, data=kwargs)
        return UserModel.parse(result)

    def get(self, username, width=None, height=None):
        """
        Retrieve public details on a given user.

        Note: Supplying the optional w or h parameters will result
        in the 'custom' photo URL being added to the 'profile_image' object:

        :param username [string]: The user’s username. Required.
        :param width [integer]: Profile image width in pixels.
        :param height [integer]: Profile image height in pixels.
        :return: [User]: The Unsplash User.
        """
        url = "/users/{username}".format(username=username)
        params = {
            "w": width,
            "h": height
        }
        result = self._get(url, params=params)
        return UserModel.parse(result)

    def portfolio(self, username):
        """
        Retrieve a single user’s portfolio link.

        :param username [string]: The user’s username. Required.
        :return: [Link]: The Unsplash Link.
        """
        url = "/users/{username}/portfolio".format(username=username)
        result = self._get(url)
        return LinkModel.parse(result)

    def _photos(self, url, username, page=1, per_page=10, order_by="latest"):
        if order_by not in self.ordering_values:
            raise Exception()
        params = {
            "page": page,
            "per_page": per_page,
            "order_by": order_by
        }
        return self._get(url, params=params)

    def photos(self, username, page=1, per_page=10, order_by="latest"):
        """
        Get a list of photos uploaded by a user.

        :param username [string]: The user’s username. Required.
        :param page [integer]: Page number to retrieve. (Optional; default: 1)
        :param per_page [integer]: Number of items per page. (Optional; default: 10)
        :param order_by [string]: How to sort the photos. Optional.
        (Valid values: latest, oldest, popular; default: latest)
        :return: [Array]: A single page of the Photo list.
        """
        url = "/users/{username}/photos".format(username=username)
        result = self._photos(url, username, page=page, per_page=per_page, order_by=order_by)
        return PhotoModel.parse_list(result)

    def likes(self, username, page=1, per_page=10, order_by="latest"):
        """
        Get a list of photos liked by a user.

        :param username [string]: The user’s username. Required.
        :param page [integer]: Page number to retrieve. (Optional; default: 1)
        :param per_page [integer]: Number of items per page. (Optional; default: 10)
        :param order_by [string]: How to sort the photos. Optional.
        (Valid values: latest, oldest, popular; default: latest)
        :return: [Array]: A single page of the Photo list.
        """
        url = "/users/{username}/likes".format(username=username)
        result = self._photos(url, username, page=page, per_page=per_page, order_by=order_by)
        return PhotoModel.parse_list(result)

    def collections(self, username, page=1, per_page=10):
        """
        Get a list of collections created by the user.

        :param username [string]: The user’s username. Required.
        :param page [integer]: Page number to retrieve. (Optional; default: 1)
        :param per_page [integer]: Number of items per page. (Optional; default: 10)
        :return: [Array]: A single page of the Collection list.
        """
        url = "/users/{username}/collections".format(username=username)
        params = {
            "page": page,
            "per_page": per_page
        }
        result = self._get(url, params=params)
        return CollectionModel.parse_list(result)
