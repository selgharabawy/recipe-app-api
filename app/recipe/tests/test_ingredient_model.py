"""
Test ingredient model.
"""
from django.test import TestCase

from recipe import models
from recipe.tests.helper_func import create_user


class IngredientModelTests(TestCase):
    """Test ingredient:ingredient model."""

    def test_create_ingredient(self):
        """Test creating a ingredient is successful"""
        user = create_user()
        ingredient = models.Ingredient.objects.create(
            user=user,
            name='Ingredient1'
        )

        self.assertEqual(str(ingredient), ingredient.name)
