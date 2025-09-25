from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser # import your custom user model
from django.contrib.auth import get_user_model

User = get_user_model()

class Cu2stomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    contact = forms.CharField(max_length=15, required=True)

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'contact', 'id_no', 'gender', 'password1', 'password2')

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
