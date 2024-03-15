from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {'email': 'Email'}


class EditUserProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'email',
                  'date_joined', 'last_login']
        labels = {'email': 'Email'}


class EditAdminProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = '__all__'
        labels = {'email': 'Email'}
