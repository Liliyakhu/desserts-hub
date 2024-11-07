from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from desserts.models import DessertType, Cook, Ingredient, Dessert
from desserts.forms import (
    DessertTypeSearchForm,
    IngredientSearchForm,
    DessertSearchForm,
    DessertForm,
)

# from desserts.forms import (
#     DriverCreationForm,
#     DriverLicenseUpdateForm,
#     CarForm,
#     DriverSearchForm,
#     CarSearchForm,
#     ManufacturerSearchForm
# )


# INDEX VIEW


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


# DESSERT TYPE VIEWS


class DessertTypeListView(LoginRequiredMixin, generic.ListView):
    model = DessertType
    context_object_name = "dessert_type_list"
    template_name = "desserts/dessert_type_list.html"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DessertTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["search_form"] = DessertTypeSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = DessertType.objects.all()
        form = DessertTypeSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class DessertTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DessertType
    fields = "__all__"
    success_url = reverse_lazy("desserts:dessert-type-list")
    template_name = "desserts/dessert_type_form.html"


class DessertTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DessertType
    fields = "__all__"
    success_url = reverse_lazy("desserts:dessert-type-list")
    template_name = "desserts/dessert_type_form.html"


class DessertTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DessertType
    success_url = reverse_lazy("desserts:dessert-type-list")
    template_name = "desserts/dessert_type_confirm_delete.html"


# INGREDIENT VIEWS


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    context_object_name = "ingredient_list"
    template_name = "desserts/ingredient_list.html"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IngredientListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["search_form"] = IngredientSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Ingredient.objects.all().prefetch_related("desserts__ingredients")
        form = IngredientSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("desserts:ingredient-list")
    template_name = "desserts/ingredient_form.html"


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("desserts:ingredient-list")
    template_name = "desserts/ingredient_form.html"


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("desserts:ingredient-list")
    template_name = "desserts/ingredient_confirm_delete.html"


# DESSERT VIEWS


class DessertListView(LoginRequiredMixin, generic.ListView):
    model = Dessert
    paginate_by = 3
    queryset = Dessert.objects.select_related("dessert_type")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DessertListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["search_form"] = DessertSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Dessert.objects.select_related("dessert_type")
        form = DessertSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class DessertDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dessert


class DessertCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dessert
    form_class = DessertForm
    success_url = reverse_lazy("desserts:dessert-list")


class DessertUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dessert
    form_class = DessertForm
    success_url = reverse_lazy("desserts:dessert-list")


class DessertDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dessert
    success_url = reverse_lazy("desserts:dessert-list")


@login_required
def toggle_add_dessert_to_cook_list(request, pk):
    cook = Cook.objects.get(id=request.user.id)
    if (
        Dessert.objects.get(id=pk) in cook.desserts.all()
    ):  # probably could check if car exists
        cook.desserts.remove(pk)
    else:
        cook.desserts.add(pk)
    return HttpResponseRedirect(reverse_lazy("desserts:dessert-detail", args=[pk]))
