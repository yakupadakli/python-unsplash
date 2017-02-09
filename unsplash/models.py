

class ResultSet(list):
    """A list like object that holds results from a Unsplash API query."""


class Model(object):

    def __init__(self, **kwargs):
        self._repr_values = ["id"]

    @classmethod
    def parse(cls, data):
        """Parse a JSON object into a model instance."""
        raise NotImplementedError

    @classmethod
    def parse_list(cls, data):
        """Parse a list of JSON objects into a result set of model instances."""
        results = ResultSet()
        data = data or []
        for obj in data:
            if obj:
                results.append(cls.parse(obj))
        return results

    def __repr__(self):
        items = filter(lambda x: x[0] in self._repr_values, vars(self).items())
        state = ['%s=%s' % (k, repr(v)) for (k, v) in items]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(state))


class Photo(Model):

    @classmethod
    def parse(cls, data):
        data = data or {}
        photo = cls() if data else None
        for key, value in data.items():
            if not value:
                setattr(photo, key, value)
                continue

            if key == "user":
                user = User.parse(value)
                setattr(photo, key, user)
            elif key == "exif":
                exif = Exif.parse(value)
                setattr(photo, key, exif)
            elif key in ["urls", "links"]:
                link = Link.parse(value)
                setattr(photo, key, link)
            elif key == "location":
                location = Location.parse(value)
                setattr(photo, key, location)
            else:
                setattr(photo, key, value)
        return photo


class Exif(Model):

    def __init__(self, **kwargs):
        super(Exif, self).__init__(**kwargs)
        self._repr_values = ["make", "model"]

    @classmethod
    def parse(cls, data):
        data = data or {}
        exif = cls() if data else None
        for key, value in data.items():
            setattr(exif, key, value)
        return exif


class Link(Model):

    def __init__(self, **kwargs):
        super(Link, self).__init__(**kwargs)
        self._repr_values = ["html", "raw", "url"]

    @classmethod
    def parse(cls, data):
        data = data or {}
        link = cls() if data else None
        for key, value in data.items():
            setattr(link, key, value)
        return link


class Location(Model):

    def __init__(self, **kwargs):
        super(Location, self).__init__(**kwargs)
        self._repr_values = ["title"]

    @classmethod
    def parse(cls, data):
        data = data or {}
        location = cls() if data else None
        for key, value in data.items():
            setattr(location, key, value)
        return location


class User(Model):

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self._repr_values = ["id", "name", "username"]

    @classmethod
    def parse(cls, data):
        data = data or {}
        user = cls() if data else None
        for key, value in data.items():
            if not value:
                setattr(user, key, value)
                continue

            if key in ["links", "profile_image"]:
                link = Link.parse(value)
                setattr(user, key, link)
            elif key == "photos":
                photo = Photo.parse_list(value)
                setattr(user, key, photo)
            else:
                setattr(user, key, value)
        return user


class Stat(Model):

    def __init__(self, **kwargs):
        super(Stat, self).__init__(**kwargs)
        self._repr_values = ["total_photos",  "photo_downloads"]

    @classmethod
    def parse(cls, data):
        data = data or {}
        stat = cls() if data else None
        for key, value in data.items():
            if not value:
                setattr(stat, key, value)
                continue

            if key == "links":
                link = Link.parse(value)
                setattr(stat, key, link)
            else:
                setattr(stat, key, value)
        return stat


class Collection(Model):

    def __init__(self, **kwargs):
        super(Collection, self).__init__(**kwargs)
        self._repr_values = ["id",  "title"]

    @classmethod
    def parse(cls, data):
        data = data or {}
        collection = cls() if data else None
        for key, value in data.items():
            if not value:
                setattr(collection, key, value)
                continue

            if key == "cover_photo":
                photo = Photo.parse(value)
                setattr(collection, key, photo)
            elif key == "user":
                user = User.parse(value)
                setattr(collection, key, user)
            elif key == "links":
                link = Link.parse(value)
                setattr(collection, key, link)
            else:
                setattr(collection, key, value)
        return collection
