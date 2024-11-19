from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin",
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="cook",
            password="testcook",
            years_of_experience=2,
        )

    def test_cook_years_of_experience_listed(self):
        """
        Test that cook's experience is
        in list_display on cook admin page
        :return:
        """
        url = reverse("admin:desserts_cook_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)

    def test_cook_detail_years_of_experience_listed(self):
        """
        Test that cook's experience is on cook detail admin page
        :return:
        """
        url = reverse("admin:desserts_cook_change", args=[self.cook.id])
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)
