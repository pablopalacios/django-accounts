from django.contrib import auth
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from authtools import views as at_views
from braces import views as braces_views

from . import forms


User = auth.get_user_model()


class LoginView(at_views.LoginView):
    template_name = 'accounts/login.html'
    form_class = forms.AuthForm
    success_url = reverse_lazy('accounts:profile')

    def set_session_expiration(self, form):
        if form.cleaned_data['remember_me'] is False:
            # expires at browser close
            self.request.session.set_expiry(0)

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        self.set_session_expiration(form)
        return super().form_valid(form)


class LogoutView(at_views.LogoutView):
    url = reverse_lazy('accounts:login')


class ProfileView(braces_views.LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/profile.html'


class PasswordChangeView(at_views.PasswordChangeView):
    success_url = reverse_lazy('accounts:profile')
    template_name = 'accounts/password_change.html'


class PasswordResetView(at_views.PasswordResetView):
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    template_name = 'accounts/password_reset_view.html'


class PasswordResetDoneView(at_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class PasswordResetConfirmAndLoginView(at_views.PasswordResetConfirmAndLoginView):
    template_name = 'accounts/password_reset_confirm.html'


class ProfileUpdate(braces_views.LoginRequiredMixin, generic.UpdateView):
    form_class = forms.ProfileUpdate
    model = User
    success_url = reverse_lazy('accounts:profile')
    template_name = 'accounts/profile_update.html'

    def get_object(self):
        return self.request.user
