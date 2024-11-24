from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


from desserts.models import Ingredient, Dessert, Cook


# LOGIN FORM


class UserLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "Username"}
        )
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control form-control-lg", "placeholder": "Password"}),
    )
    remember_me = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input"
            }
        )
    )

# DESSERT TYPE FORMS


class DessertTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )


# INGREDIENT FORMS


class IngredientSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )


# DESSERT FORMS


class DessertSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )


class DessertForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dessert
        fields = "__all__"


# COOK FORMS


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )

    def clean_years_of_experience(self):  # this logic is optional, but possible
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])


class CookExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["years_of_experience"]

    def clean_years_of_experience(self):
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])


def validate_years_of_experience(
    years_of_experience,
):  # regex validation is also possible here
    if len(str(years_of_experience)) >= 3:
        raise ValidationError("Years of experience should be 1 or 2 digital number")
    elif years_of_experience < 0:
        raise ValidationError("Years of experience can't be negative")

    return years_of_experience


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username"
            }
        )
    )

