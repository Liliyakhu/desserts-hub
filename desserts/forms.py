from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


from desserts.models import Ingredient, Dessert, Cook, DessertType


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
                "class": "form-control form-control-lg",
                "placeholder": "Search by name"
            }
        )
    )


class DessertTypeForm(forms.ModelForm):
    name = forms.CharField(
        label=_("Name*:"),
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg mb-3",
                "placeholder": "Name"
            }
        )
    )

    class Meta:
        model = DessertType
        fields = "__all__"


# INGREDIENT FORMS


class IngredientSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Search by name"
            }
        )
    )


class IngredientForm(forms.ModelForm):
    name = forms.CharField(
        label=_("Name*:"),
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg mb-3",
                "placeholder": "Name"
            }
        )
    )

    class Meta:
        model = Ingredient
        fields = "__all__"


# DESSERT FORMS


class DessertSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Search by name"
            }
        )
    )


class DessertForm(forms.ModelForm):
    name = forms.CharField(
        label=_("Name*:"),
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg mb-3",
                "placeholder": "Name"
            }
        )
    )

    description = forms.CharField(
        label=_("Description*:"),
        widget=forms.Textarea(
            attrs={
                "class": "form-control form-control-lg mb-3",
                "placeholder": "A few words about this dessert"
            }
        )
    )

    price = forms.DecimalField(
        label=_("Price*:"),
        widget=forms.NumberInput(
            attrs={
                "min": "0",
                "max": "100",
                "step": "0.01",
                "class": "form-control form-control-lg mb-3",
                "placeholder": "Price for 100g, $"
            }
        )
    )

    dessert_type = forms.ModelChoiceField(
        label=_("Dessert Type*:"),
        queryset=DessertType.objects.all(),
        empty_label="Select a dessert type",
        widget=forms.Select(
            attrs={
                "class": "form-select form-select-lg mb-3",
                "placeholder": "Choose a dessert type."
            }
        )
    )

    cooks = forms.ModelMultipleChoiceField(
        label="Cooks:",
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "form-check-input mb-3",
            }
        ),
    )

    ingredients = forms.ModelMultipleChoiceField(
        label="Ingredients:",
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "form-check-input mb-3",
            }
        ),
    )

    image = forms.ImageField(
        label=_("Image:"),
        required=False,
        widget=forms.FileInput(
            attrs={"class": "form-control form-control-lg mb-3", "placeholder": "Image"}
        )
    )

    class Meta:
        model = Dessert
        fields = "__all__"


# COOK FORMS


class CookCreationForm(UserCreationForm):
    username = UsernameField(
        # THIS LABEL'S STYLES WILL ONLY WORK WITH |save IN HTML TEMPLATE
        # label="<span style='color: red;'>Name</span>",
        label=_("Username*"),
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg mb-3", "placeholder": "Username"}
        ),
        # help_text=_("150 characters or fewer. Letters, digits, and @/./+/-/_ only."),
    )
    years_of_experience = forms.IntegerField(
        initial=0,
        required=False,
        widget=forms.NumberInput(
            attrs={"class": "form-control form-control-lg mb-3", "placeholder": "Years of Experience"}
        )
    )

    image = forms.ImageField(
        # initial="Image",
        required=False,
        widget=forms.FileInput(
            attrs={"class": "form-control form-control-lg mb-3", "placeholder": "Image"}
        )
    )

    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg mb-3", "placeholder": "First Name"}
        )
    )

    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg mb-3", "placeholder": "Last Name"}
        )
    )

    password1 = forms.CharField(
        label=_("Password*:"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"class": "form-control form-control-lg mb-3", "placeholder": "Password"}
        ),
        # help_text=""
        # help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=_("Confirm Password*:"),
        # strip=False,
        widget=forms.PasswordInput(
            attrs={"class": "form-control form-control-lg mb-3", "placeholder": "Password"}
        ),
        # help_text="Enter the same password as before, for verification."
    )

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
            "image",
        )

    def clean_years_of_experience(self):  # this logic is optional, but possible
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])

    def clean_image(self):  # this logic is optional, but possible
        return validate_image(self.cleaned_data["image"])


class CookUpdateForm(forms.ModelForm):
    years_of_experience = forms.IntegerField(
        initial=0,
        required=False,
        widget=forms.NumberInput(
            attrs={"class": "form-control form-control-lg mb-3", "placeholder": "Years of Experience"}
        )
    )

    image = forms.ImageField(
        # initial="Image",
        required=False,
        widget=forms.FileInput(
            attrs={"class": "form-control form-control-lg mb-3", "placeholder": "Image"}
        )
    )

    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg mb-3", "placeholder": "First Name"}
        )
    )

    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg mb-3", "placeholder": "Last Name"}
        )
    )

    class Meta:
        model = Cook
        fields = ["years_of_experience", "image", "first_name", "last_name"]

    def clean_years_of_experience(self):
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])

    def clean_image(self):
        return validate_image(self.cleaned_data["image"])


# class CookImageUpdateForm(forms.ModelForm):
#     image = forms.ImageField(
#         widget=forms.FileInput()
#     )
#
#     class Meta:
#         model = Cook
#         fields = ["image"]
#
#     def clean_image(self):
#         return validate_image(self.cleaned_data["image"])


def validate_years_of_experience(
    years_of_experience,
):  # regex validation is also possible here
    if len(str(years_of_experience)) >= 3:
        raise ValidationError("Years of experience should be 1 or 2 digital number")
    elif years_of_experience < 0:
        raise ValidationError("Years of experience can't be negative")

    return years_of_experience


def validate_image(
    image,
):
    return image


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Search by username"
            }
        )
    )

