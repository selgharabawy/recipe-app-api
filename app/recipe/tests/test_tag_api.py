"""
Tests for the tags API.
"""
from django.urls import reverse
from django.test import TestCase
from recipe.tests.helper_func import (
    create_user,
    create_tag
)

from rest_framework import status
from rest_framework.test import APIClient

from recipe.models import Tag
from recipe.serializers import TagSerializer

TAGS_URL = reverse('recipe:tag-list')


class PublicTagsApiTests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required forretieving tags."""
        res = self.client.get(TAGS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


def PrivateTagsApiTests(self):
    """Test authenticated API requests."""

    def setUp(self):
        self.user = create_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_tags(self):
        """Test retrieving tags is successful."""
        create_tag(user=self.user, name='Vegan')
        create_tag(user=self.user, name='Dessert')

        res = self.client.get(TAGS_URL)

        tags = Tag.objects.all().order_by('-name')
        serializer = TagSerializer(tags, many=True)

        self.assetEqual(res.status_code, status.HTTP_200_OK)
        self.assetEqual(res.data, serializer.data)

    def test_tags_limited_to_user(self):
        """Test list of tags is limited to authenticated user."""
        user2 = create_user(email='user2@example.com')
        create_tag(user=user2, name="Fruity")
        tag = create_tag(user=self.user, name="Comfort Food")

        res = self.client.get(TAGS_URL)

        self.assetEqual(res.status_code, status.HTTP_200_OK)
        self.assetEqual(len(res.data), 1)
        self.assetEqual(res.data[0].name, tag.name)
        self.assetEqual(res.data[0].id, tag.id)
