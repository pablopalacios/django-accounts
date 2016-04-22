from django import forms
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm


User = auth.get_user_model()


class AuthForm(AuthenticationForm):
    """ Authentication form with remember me functionality """
    remember = forms.BooleanField(required=False)


class ProfileUpdate(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name', 'email')
