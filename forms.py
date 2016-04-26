from django import forms
from django.contrib.auth import forms as auth_forms
from django.utils.translation import ugettext_lazy as _

from . import models


class LoginForm(auth_forms.AuthenticationForm):
    """ Login form with remember me functionality """

    username = forms.CharField(
        label=_('Email'),
        max_length=25,
    )
    password = forms.CharField(
        label=_('Password'),
    )
    remember_me = forms.BooleanField(
        required=False,
        label=_('Remember me'),
    )


class ProfileForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = ('name', 'email')
