import unittest

from tests.config import UnsplashTestCase, SKIP_TEST
from unsplash.models import Photo, Collection, User


class PhotoTest(UnsplashTestCase):
    default_photo_id = u"KSap1iDftvQ"
    default_search_query = u"nature"
    default_search_user_query = u"yakupa"

    def test_photos(self):
        photo_dict = self.api.search.photos(self.default_search_query, per_page=2)
        photos = photo_dict.get("results")
        self.assertIsInstance(photo_dict, dict)
        self.assertIsInstance(photos, list)
        self.assertIsInstance(photos[0], Photo)
        self.assertEqual(len(photos), 2)

    def test_collections(self):
        if SKIP_TEST:
            return True

        collection_dict = self.api.search.collections(self.default_search_query, per_page=2)
        collections = collection_dict.get("results")
        self.assertIsInstance(collection_dict, dict)
        self.assertIsInstance(collections, list)
        self.assertIsInstance(collections[0], Collection)
        self.assertEqual(len(collections), 2)

    def test_users(self):
        if SKIP_TEST:
            return True

        user_dict = self.api.search.users(self.default_search_user_query, per_page=1)
        users = user_dict.get("results")
        self.assertIsInstance(user_dict, dict)
        self.assertIsInstance(users, list)
        self.assertIsInstance(users[0], User)
        self.assertEqual(len(users), 1)


if __name__ == "__main__":
    unittest.main()
