from django import forms
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


User = auth.get_user_model()


class AuthForm(AuthenticationForm):
    """ Authentication form with remember me functionality """

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Email'),
        }),
        max_length=25)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Password'),
        })
    )
    remember_me = forms.BooleanField(
        required=False,
        label=_('Remember me'),
        attrs={
            'class': 'icheck',
        },
    )


class ProfileUpdate(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name', 'email')
