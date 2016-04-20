from authtools import views as at_views
from django.core.urlresolvers import reverse_lazy


class LoginView(at_views.LoginView):
    template_name = 'accounts/login.html'


class LogoutView(at_views.LogoutView):
    url = reverse_lazy('accounts:login')
