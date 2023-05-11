"""
Test recipe models.
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from recipe import models


class ModelTests(TestCase):
    """Test recipe models."""

    def test_create_recipe(self):
        """Test creating a recipe is successful"""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpassword123'
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample recipe name',
            time_minutes=5,
            price=Decimal(5.50),
            description='Sample recipe description.',
        )

        self.assertEqual(str(recipe), recipe.title)
