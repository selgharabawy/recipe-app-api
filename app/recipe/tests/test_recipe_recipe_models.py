"""
Test recipe models.
"""
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
