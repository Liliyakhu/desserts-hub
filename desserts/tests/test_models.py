from django.contrib.auth import get_user_model
from django.test import TestCase

from desserts.models import Dessert, Cook, DessertType, Ingredient


class ModelTests(TestCase):
    def test_dessert_type_str(self):
        dessert_type = DessertType.objects.create(
            name="test_name"
        )
        self.assertEqual(
            str(dessert_type),
            dessert_type.name
        )

    def test_ingredient_str(self):
        ingredient = Ingredient.objects.create(
            name="test_name"
        )
        self.assertEqual(
            str(ingredient),
            ingredient.name
        )

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="test",
            password="test123",
            first_name="test_first",
            last_name="test_last",
        )
        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
        )

    def test_dessert_str(self):
        dessert_type = DessertType.objects.create(
            name="test_name"
        )
        dessert = Dessert.objects.create(
            name="test_name",
            description="test_description",
            price=2.25,
            dessert_type=dessert_type
        )
        self.assertEqual(str(dessert), dessert.name)

    def test_create_cook_with_experience(self):
        username = "test"
        password = "test123"
        years_of_experience = 2
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience
        )
        self.assertEqual(cook.username, username)
        self.assertEqual(cook.years_of_experience, years_of_experience)
        self.assertTrue(cook.check_password(password))
