# coding=utf-8

# Unsplash
# Copyright 2017 Yakup Adaklı
# See LICENSE for details.

"""A library that provides a Python interface to the Unsplash API"""

__version__ = "1.0.0a1"
__author__ = "Yakup Adaklı"
__license__ = "MIT"


from .api import Api                                        # noqa
from .auth import Auth                                      # noqa
from .errors import UnsplashError, UnsplashAuthError        # noqa
