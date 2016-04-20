from django import forms
from django.contrib.auth.forms import AuthenticationForm


class AuthForm(AuthenticationForm):
    """ Authentication form with remember me functionality """
    remember = forms.BooleanField(required=False)
