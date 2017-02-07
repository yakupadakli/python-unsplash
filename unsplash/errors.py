import six


class UnsplashError(Exception):
    """Unsplash exception"""

    def __init__(self, message, **kwargs):
        self.message = six.text_type(message) if message else "Unknown error"
        super(UnsplashError, self).__init__(message, **kwargs)

    def __str__(self):
        return self.message


class UnsplashAuthError(UnsplashError):

    def __init__(self, reason, **kwargs):
        self.reason = reason
        self.message = "Unsplash Authentication Error: %s " % self.reason
        super(UnsplashAuthError, self).__init__(message=self.message, **kwargs)
