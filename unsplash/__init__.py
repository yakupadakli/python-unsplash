# coding=utf-8

# Unsplash
# Copyright 2017 Yakup Adaklı
# See LICENSE for details.

"""A library that provides a Python interface to the Unsplash API"""

__version__ = "1.0.0a1"
__author__ = "Yakup Adaklı"
__license__ = "MIT"


from unsplash.api import Api
from unsplash.auth import Auth
from unsplash.errors import UnsplashError, UnsplashAuthError
