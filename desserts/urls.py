from django.urls import path

from desserts.views import (
    index,
    DessertTypeListView,
    DessertTypeCreateView,
    DessertTypeUpdateView,
    DessertTypeDeleteView,
    IngredientListView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "dessert-types/",
        DessertTypeListView.as_view(),
        name="dessert-type-list",
    ),
    path(
        "dessert-types/create/",
        DessertTypeCreateView.as_view(),
        name="dessert-type-create",
    ),
    path(
        "dessert-types/<int:pk>/update/",
        DessertTypeUpdateView.as_view(),
        name="dessert-type-update",
    ),
    path(
        "dessert-types/<int:pk>/delete/",
        DessertTypeDeleteView.as_view(),
        name="dessert-type-delete",
    ),
    path(
        "ingredients/",
        IngredientListView.as_view(),
        name="ingredient-list",
    ),
    path(
        "ingredients/create/",
        IngredientCreateView.as_view(),
        name="ingredient-create",
    ),
    path(
        "ingredients/<int:pk>/update/",
        IngredientUpdateView.as_view(),
        name="ingredient-update",
    ),
    path(
        "ingredients/<int:pk>/delete/",
        IngredientDeleteView.as_view(),
        name="ingredient-delete",
    ),
]

app_name = "desserts"
