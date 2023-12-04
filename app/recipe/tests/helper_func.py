"""
Helper Functions for testing.
"""
from django.contrib.auth import get_user_model
from recipe.models import Recipe, Tag, Ingredient

from decimal import Decimal


def create_user(
        email='user@example.com',
        password='testpassword@123',
        **params
):
    """Create and return a new user."""
    return get_user_model().objects.create_user(email, password, **params)


def create_recipe(user, **params):
    """Create and return a sample recipe."""
    defaults = {
        'title': 'Sample recipe title/',
        'time_minutes': 22,
        'price': Decimal('5.25'),
        'description': 'Sample description',
        'link': 'https://example.com/recipe.pdf'
    }
    defaults.update(params)

    recipe = Recipe.objects.create(user=user, **defaults)
    return recipe


def create_tag(user, name='Test Tag'):
    """Create and return a sample tag."""

    tag = Tag.objects.create(user=user, name=name)
    return tag


def create_ingredient(user, name='Test Ingredient'):
    """Create and return a sample ingredient."""

    ing = Ingredient.objects.create(user=user, name=name)
    return ing
