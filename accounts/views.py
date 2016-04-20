from django.contrib import auth
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from authtools import views as at_views

from . import forms


class LoginView(at_views.LoginView):
    template_name = 'accounts/login.html'
    form_class = forms.AuthForm

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        if form.cleaned_data['remember'] is False:
            # expires at browser close
            self.request.session.set_expiry(0)
        return super().form_valid(form)


class LogoutView(at_views.LogoutView):
    url = reverse_lazy('accounts:login')


class ProfileView(generic.TemplateView):
    template_name = 'accounts/profile.html'


class PasswordChangeView(at_views.PasswordChangeView):
    pass


class PasswordChangeDoneView(at_views.PasswordChangeDoneView):
    pass


class PasswordResetView(at_views.PasswordResetView):
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    template_name = 'accounts/password_reset_view.html'


class PasswordResetDoneView(at_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class PasswordResetConfirmAndLoginView(at_views.PasswordResetConfirmAndLoginView):
    template_name = 'accounts/password_reset_confirm.html'
