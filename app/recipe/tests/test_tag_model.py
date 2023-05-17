"""
Test recipe models.
"""
from django.test import TestCase

from recipe import models
from recipe.tests.helper_func import create_user


class ModelTests(TestCase):
    """Test recipe:tags model."""

    def test_create_tag(self):
        """Test creating a tag is successful"""
        user = create_user()
        tag = models.Tag.objects.create(user=user, name='Tag1')

        self.assertEqual(str(tag), tag.name)
