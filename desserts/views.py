from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from desserts.models import DessertType, Cook, Ingredient, Dessert
from desserts.forms import (
    DessertTypeSearchForm,
    IngredientSearchForm,
    DessertSearchForm,
    DessertForm,
    CookSearchForm,
    CookCreationForm,
    CookExperienceUpdateForm,
    UserLoginForm,
)

# LOGIN AND LOGOUT VIEWS


class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    form_class = UserLoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get("remember_me")  # get remember me data from cleaned_data of form
        if remember_me:
            self.request.session.set_expiry(1209600)
        else:
            self.request.session.set_expiry(0)
        return super().form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('/accounts/login')


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


# COOK VIEWS


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    queryset = Cook.objects.prefetch_related("desserts__cooks")
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username")
        context["search_form"] = CookSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = Cook.objects.prefetch_related("desserts__cooks")
        form = CookSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("desserts__cooks")


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    # success_url = reverse_lazy("desserts:cook-list")


class CookExperienceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookExperienceUpdateForm
    success_url = reverse_lazy("desserts:cook-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("desserts:cook-list")
