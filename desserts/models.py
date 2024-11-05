from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from desserts_hub import settings


class DessertType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["username"]
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return f"{self.username} ({self.first_name}) {self.last_name})"

    def get_absolute_url(self):
        return reverse("desserts:cook-detail", kwargs={"pk": self.pk})


class Dessert(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dessert_type = models.ForeignKey(
        DessertType,
        on_delete=models.CASCADE,
        related_name="desserts",
    )
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="desserts")

    ingredients = models.ManyToManyField("Ingredient", related_name="desserts")

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
