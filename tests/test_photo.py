import unittest

from tests.config import UnsplashTestCase, SKIP_TEST
from unsplash.models import Photo, Stat


class PhotoTest(UnsplashTestCase):
    default_photo_id = u"KSap1iDftvQ"
    default_search_query = u"nature"

    def test_all(self):
        photos = self.api.photo.all(per_page=2)
        self.assertIsInstance(photos, list)
        self.assertIsInstance(photos[0], Photo)
        self.assertEqual(len(photos), 2)

    def test_curated(self):
        if SKIP_TEST:
            return True

        curated_photos = self.api.photo.curated(per_page=2)
        self.assertIsInstance(curated_photos, list)
        self.assertIsInstance(curated_photos[0], Photo)
        self.assertEqual(len(curated_photos), 2)

    def test_get(self):
        if SKIP_TEST:
            return True

        photo = self.api.photo.get(self.default_photo_id)
        self.assertIsNotNone(photo)
        self.assertIsInstance(photo, Photo)

    def test_search_photo(self):
        if SKIP_TEST:
            return True

        photos = self.api.photo.search(self.default_search_query, per_page=2)
        self.assertEqual(len(photos), 2)
        self.assertIsInstance(photos, list)
        self.assertIsInstance(photos[0], Photo)

    def test_random(self):
        if SKIP_TEST:
            return True

        photos = self.api.photo.random(count=2)
        self.assertEqual(len(photos), 2)
        self.assertIsInstance(photos, list)
        self.assertIsInstance(photos[0], Photo)

    def test_stats(self):
        if SKIP_TEST:
            return True

        stat = self.api.photo.stats(self.default_photo_id)
        self.assertIsInstance(stat, Stat)

    def test_like(self):
        if SKIP_TEST:
            return True

        photo = self.api.photo.like(self.default_photo_id)
        self.assertIsInstance(photo, Photo)

    def test_unlike(self):
        if SKIP_TEST:
            return True

        photo = self.api.photo.like(self.default_photo_id)
        self.assertIsInstance(photo, Photo)


if __name__ == "__main__":
    unittest.main()
