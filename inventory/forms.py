from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from inventory.models import Product
from inventory.models import UserProfile


class UserRegistry(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["artist", "location", "title", "description", "inventoryNum"]

class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = UserProfile
        fields = ['picture']

