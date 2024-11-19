from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from desserts.models import Dessert, DessertType, Ingredient

DESSERT_TYPE_URL = reverse("desserts:dessert-type-list")
INGREDIENT_URL = reverse("desserts:ingredient-list")
DESSERT_URL = reverse("desserts:dessert-list")
COOK_URL = reverse("desserts:cook-list")


class PublicDessertTypeTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(DESSERT_TYPE_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateDessertTypeTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.dessert_type_one = DessertType.objects.create(
            name="test_dessert_type_one",
        )
        self.dessert_type_two = DessertType.objects.create(
            name="test_dessert_type_two",
        )
        self.client.force_login(self.user)

    def test_retrieve_dessert_types(self):
        response = self.client.get(DESSERT_TYPE_URL)
        self.assertEqual(response.status_code, 200)
        dessert_types = DessertType.objects.all()
        self.assertEqual(
            list(response.context["dessert_type_list"]),
            list(dessert_types),
        )
        self.assertTemplateUsed(response, "desserts/dessert_type_list.html")

    def test_search_dessert_types(self):
        response = self.client.get(
            reverse("desserts:dessert-type-list"),
            {"name": "test_dessert_type_one"}
        )
        self.assertContains(response, self.dessert_type_one.name)
        self.assertNotContains(response, self.dessert_type_two.name)


class PublicIngredientTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(INGREDIENT_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateIngredientTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.ingredient_one = Ingredient.objects.create(
            name="test_ingredient_one",
        )
        self.ingredient_two = Ingredient.objects.create(
            name="test_ingredient_two",
        )
        self.client.force_login(self.user)

    def test_retrieve_ingredients(self):
        response = self.client.get(INGREDIENT_URL)
        self.assertEqual(response.status_code, 200)
        ingredients = Ingredient.objects.all()
        self.assertEqual(
            list(response.context["ingredient_list"]),
            list(ingredients),
        )
        self.assertTemplateUsed(response, "desserts/ingredient_list.html")

    def test_search_ingredients(self):
        response = self.client.get(
            reverse("desserts:ingredient-list"),
            {"name": "test_ingredient_one"}
        )
        self.assertContains(response, self.ingredient_one.name)
        self.assertNotContains(response, self.ingredient_two.name)


class PublicDessertTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(DESSERT_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateDessertTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_user",
            email="test@test.com",
            password="password",
            years_of_experience=2,
        )
        dessert_type = DessertType.objects.create(
            name="test_dessert_type",
        )
        self.first_dessert = Dessert.objects.create(
            dessert_type=dessert_type,
            name="test_name_one",
            description="test_description_one",
            price=10,
        )
        self.second_dessert = Dessert.objects.create(
            dessert_type=dessert_type,
            name="test_name_two",
            description="test_description_two",
            price=20,
        )
        self.first_dessert.cooks.set([self.user])
        self.second_dessert.cooks.set([self.user])
        self.client.force_login(self.user)

    def test_retrieve_desserts(self):
        response = self.client.get(DESSERT_URL)
        self.assertEqual(response.status_code, 200)
        desserts = Dessert.objects.all()
        self.assertEqual(
            list(response.context["dessert_list"]),
            list(desserts),
        )
        self.assertTemplateUsed(response, "desserts/dessert_list.html")

    def test_search_desserts(self):
        response = self.client.get(
            reverse("desserts:dessert-list"),
            {"name": "test_name_one"}
        )
        self.assertContains(response, self.first_dessert.name)
        self.assertNotContains(response, self.second_dessert.name)


class PublicCookTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(COOK_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateCookTest(TestCase):
    def setUp(self) -> None:
        self.user_one = get_user_model().objects.create_user(
            username="test_user_1",
            email="test@test.com",
            password="password",
            years_of_experience=2,
        )
        self.user_two = get_user_model().objects.create_user(
            username="test_user_2",
            email="test@test_2.com",
            password="password",
            years_of_experience=3,
        )
        dessert_type = DessertType.objects.create(
            name="test_dessert",
        )
        self.first_dessert = Dessert.objects.create(
            name="test_name_one",
            description="test_description_one",
            price=10,
            dessert_type=dessert_type,
        )
        self.second_dessert = Dessert.objects.create(
            name="test_name_two",
            description="test_description_two",
            price=15,
            dessert_type=dessert_type,
        )
        self.first_dessert.cooks.set([self.user_one, self.user_two])
        self.second_dessert.cooks.set([self.user_one])
        self.client.force_login(self.user_one)

    def test_retrieve_cooks(self):
        response = self.client.get(COOK_URL)
        self.assertEqual(response.status_code, 200)
        cooks = get_user_model().objects.all()
        self.assertEqual(
            list(response.context["cook_list"]),
            list(cooks),
        )
        self.assertTemplateUsed(response, "desserts/cook_list.html")

    def test_search_cooks(self):
        response = self.client.get(
            reverse("desserts:cook-list"),
            {"username": "test_user_1"}
        )
        self.assertContains(response, self.user_one.username)
        self.assertNotContains(response, self.user_two.username)
