from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from desserts.models import DessertType, Cook, Ingredient, Dessert
# from desserts.forms import (
#     DriverCreationForm,
#     DriverLicenseUpdateForm,
#     CarForm,
#     DriverSearchForm,
#     CarSearchForm,
#     ManufacturerSearchForm
# )


@login_required
def index(request):
    """View function for the home page of the site."""

    num_cooks = Cook.objects.count()
    num_desserts = Dessert.objects.count()
    num_dessert_types = DessertType.objects.count()
    num_ingredients = Ingredient.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_desserts": num_desserts,
        "num_dessert_types": num_dessert_types,
        "num_ingredients": num_ingredients,
        "num_visits": num_visits + 1,
    }

    return render(request, "desserts/index.html", context=context)