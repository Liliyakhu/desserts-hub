from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import Lower
from django.urls import reverse

from desserts_hub.settings import base


class DessertType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = [Lower("name")]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(default=0)
    image = models.ImageField(
        default="images/default_cook.png", upload_to="images/"
    )

    class Meta:
        ordering = ["username"]
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("desserts:cook-detail", kwargs={"pk": self.pk})


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Dessert(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(
        default="images/default_dessert.png", upload_to="images/"
    )
    dessert_type = models.ForeignKey(
        DessertType,
        on_delete=models.CASCADE,
        related_name="desserts",
    )
    cooks = models.ManyToManyField(
        base.AUTH_USER_MODEL, related_name="desserts"
    )

    ingredients = models.ManyToManyField(Ingredient, related_name="desserts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("desserts:dessert-detail", kwargs={"pk": self.pk})
