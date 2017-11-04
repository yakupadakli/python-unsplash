import unittest
import uuid

from tests.config import UnsplashTestCase, SKIP_TEST
from unsplash.models import Photo, Collection


class CollectionTest(UnsplashTestCase):
    default_collection_id = u"547584"
    default_search_query = u"nature"
    default_photo_id = u"KSap1iDftvQ"
    prefix = u"yakupa"

    def test_all(self):
        collections = self.api.collection.all(per_page=2)
        self.assertIsInstance(collections, list)
        self.assertIsInstance(collections[0], Collection)
        self.assertEqual(len(collections), 2)

    def test_featured(self):
        if SKIP_TEST:
            return True

        featured_collections = self.api.collection.featured(per_page=2)
        self.assertIsInstance(featured_collections, list)
        self.assertIsInstance(featured_collections[0], Collection)
        self.assertEqual(len(featured_collections), 2)

    def test_curated(self):
        if SKIP_TEST:
            return True

        curated_collections = self.api.collection.curated(per_page=2)
        self.assertIsInstance(curated_collections, list)
        self.assertIsInstance(curated_collections[0], Collection)
        self.assertEqual(len(curated_collections), 2)

    def test_get(self):
        if SKIP_TEST:
            return True

        collection = self.api.collection.get(self.default_collection_id)
        self.assertIsNotNone(collection)
        self.assertIsInstance(collection, Collection)

    def test_get_curated(self):
        if SKIP_TEST:
            return True

        _curated_collection = self.api.collection.curated(per_page=2)[0]
        curated_collection = self.api.collection.get_curated(_curated_collection.id)
        self.assertIsNotNone(curated_collection)
        self.assertIsInstance(curated_collection, Collection)

    def test_photos(self):
        if SKIP_TEST:
            return True

        photos = self.api.collection.photos(self.default_collection_id, per_page=2)
        self.assertIsNotNone(photos)
        self.assertIsInstance(photos, list)
        self.assertIsInstance(photos[0], Photo)

    def test_curated_photos(self):
        if SKIP_TEST:
            return True

        _curated_collection = self.api.collection.curated(per_page=2)[0]
        photos = self.api.collection.curated_photos(_curated_collection.id, per_page=2)
        if photos:
            self.assertIsNotNone(photos)
            self.assertIsInstance(photos, list)
            self.assertIsInstance(photos[0], Photo)

    def test_related(self):
        if SKIP_TEST:
            return True

        related_collections = self.api.collection.related(self.default_collection_id)
        if related_collections:
            self.assertIsInstance(related_collections, list)
            self.assertIsInstance(related_collections[0], Collection)

    def test_create(self):
        if SKIP_TEST:
            return True

        title = "%s-%s" % (self.prefix, uuid.uuid4().get_hex()[0:5])
        description = "%s-%s" % (self.prefix,uuid.uuid4().get_hex()[0:5])
        collection = self.api.collection.create(title, description)
        self.assertIsNotNone(collection)
        self.assertIsInstance(collection, Collection)
        self.assertEqual(collection.title, title)
        self.assertEqual(collection.description, description)

        self.api.collection.delete(collection.id)

    def test_update(self):
        if SKIP_TEST:
            return True

        title = "%s-%s" % (self.prefix, uuid.uuid4().get_hex()[0:5])
        description = "%s-%s" % (self.prefix,uuid.uuid4().get_hex()[0:5])
        collection = self.api.collection.update(self.default_collection_id, title=title, description=description)
        self.assertIsNotNone(collection)
        self.assertIsInstance(collection, Collection)
        self.assertEqual(collection.title, title)
        self.assertEqual(collection.description, description)

    def test_add_photo(self):
        if SKIP_TEST:
            return True

        collection, photo = self.api.collection.add_photo(self.default_collection_id, self.default_photo_id)
        self.assertIsNotNone(collection)
        self.assertIsInstance(collection, Collection)

        photos = self.api.collection.photos(self.default_collection_id)
        photo_ids = map(lambda x: x.id, photos)

        self.assertIsNotNone(photo)
        self.assertIsInstance(photo, Photo)
        self.assertIn(photo.id, photo_ids)

    def test_remove_photo(self):
        if SKIP_TEST:
            return True

        collection, photo = self.api.collection.remove_photo(self.default_collection_id, self.default_photo_id)
        self.assertIsNotNone(collection)
        self.assertIsInstance(collection, Collection)

        photos = self.api.collection.photos(self.default_collection_id)
        photo_ids = map(lambda x: x.id, photos)

        self.assertIsNotNone(photo)
        self.assertIsInstance(photo, Photo)
        self.assertNotIn(photo.id, photo_ids)

    def test_delete(self):
        if SKIP_TEST:
            return True

        title = "%s-%s" % (self.prefix, uuid.uuid4().get_hex()[0:5])
        description = "%s-%s" % (self.prefix,uuid.uuid4().get_hex()[0:5])
        _collection = self.api.collection.create(title, description)
        collection = self.api.collection.delete(_collection.id)
        self.assertIsNone(collection)


if __name__ == "__main__":
    unittest.main()
