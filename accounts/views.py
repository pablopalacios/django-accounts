from authtools.views import LoginView as ATLoginView


class LoginView(ATLoginView):
    template_name = 'accounts/login.html'
