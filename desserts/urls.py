from django.urls import path

from desserts.views import (
    index,
)

urlpatterns = [
    path("", index, name="index"),
]

app_name = "desserts"
