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
    DessertListView,
    DessertDetailView,
    DessertCreateView,
    DessertUpdateView,
    DessertDeleteView,
    toggle_add_dessert_to_cook_list,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
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
    path(
        "desserts/",
        DessertListView.as_view(),
        name="dessert-list",
    ),
    path(
        "desserts/<int:pk>/",
        DessertDetailView.as_view(),
        name="dessert-detail",
    ),
    path(
        "desserts/create/",
        DessertCreateView.as_view(),
        name="dessert-create",
    ),
    path(
        "desserts/<int:pk>/update/",
        DessertUpdateView.as_view(),
        name="dessert-update",
    ),
    path(
        "desserts/<int:pk>/delete/",
        DessertDeleteView.as_view(),
        name="dessert-delete",
    ),
    path(
        "desserts/<int:pk>/toggle-add/",
        toggle_add_dessert_to_cook_list,
        name="toggle-add-dessert",
    ),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path(
        "cooks/<int:pk>/update/",
        CookUpdateView.as_view(),
        name="cook-update",
    ),
    path(
        "cooks/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete",
    ),
]

app_name = "desserts"
