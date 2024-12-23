from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from desserts.forms import (
    CookCreationForm,
    CookSearchForm,
    DessertSearchForm,
    DessertTypeSearchForm,
    IngredientSearchForm,
)


class FormsTests(TestCase):
    def test_cook_creation_form_with_experience_first_last_name_is_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "user12test",
            "password2": "user12test",
            "first_name": "Test first",
            "last_name": "Test last",
            "years_of_experience": 2,
            "image": None,
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class PrivateCookTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test", password="password123"
        )
        self.client.force_login(self.user)

    def test_create_cook(self):
        form_data = {
            "username": "new_user",
            "password1": "user12test",
            "password2": "user12test",
            "first_name": "Test first",
            "last_name": "Test last",
            "years_of_experience": 2,
        }
        self.client.post(reverse("desserts:cook-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(
            new_user.years_of_experience,
            form_data["years_of_experience"]
        )

    def test_update_cook_experience(self):
        new_user = get_user_model().objects.create_user(
            username="new_user",
            password="user12test",
            first_name="Test first",
            last_name="Test last",
            years_of_experience=2,
        )
        form_data = {"years_of_experience": 2}
        self.client.post(
            reverse("desserts:cook-update", args=[new_user.id]), data=form_data
        )
        updated_user = get_user_model().objects.get(id=new_user.id)

        self.assertEqual(
            updated_user.years_of_experience, form_data["years_of_experience"]
        )


class CookSearchFormTest(TestCase):
    def test_form_is_valid_with_valid_username(self):
        form_data = {
            "username": "user",
        }
        form = CookSearchForm(data=form_data)
        self.assertTrue(form.is_valid())


class DessertSearchFormTest(TestCase):
    def test_form_is_valid(self):
        form_data = {
            "name": "yummy",
        }
        form = DessertSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "yummy")


class DessertTypeSearchFormTest(TestCase):
    def test_form_is_valid(self):
        form_data = {
            "name": "type",
        }
        form = DessertTypeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "type")


class IngredientSearchFormTest(TestCase):
    def test_form_is_valid(self):
        form_data = {
            "name": "test_ingredient",
        }
        form = IngredientSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "test_ingredient")
