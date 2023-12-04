"""
Test recipe models.
"""
from unittest.mock import patch
from decimal import Decimal

from django.test import TestCase

from recipe import models
from recipe.tests.helper_func import create_user


class ModelTests(TestCase):
    """Test recipe:recipe model."""

    def test_create_recipe(self):
        """Test creating a recipe is successful"""
        user = create_user()
        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample recipe name',
            time_minutes=5,
            price=Decimal(5.50),
            description='Sample recipe description.',
        )

        self.assertEqual(str(recipe), recipe.title)

    @patch('recipe.models.uuid.uuid4')
    def test_recipe_file_name_uuid(self, mock_uuid):
        """Test generating image path."""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.recipe_image_file_path(None,'example.jpg')

        self.assertEqual(file_path, f'uploads/recipe/{uuid}.jpg')
