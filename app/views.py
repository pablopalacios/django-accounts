from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

from braces.views import GroupRequiredMixin


class BaseView(GroupRequiredMixin, TemplateView):
    template_name = 'app/index.html'

    def get_menu(self):
        groups = self.request.user.groups.values_list('name', flat=True)
        menu = []
        admin = reverse('app:admin'), 'admin'
        users = reverse('app:users'), 'users'
        if 'users' in groups:
            menu.append(users)
        elif 'admin' in groups:
            menu.append(admin)
        elif self.request.user.is_superuser:
            menu.append(admin)
            menu.append(users)
        return menu

    def get_context_data(self, **kw):
        context = super().get_context_data(**kw)
        context['menu'] = self.get_menu()
        return context


class UsersView(BaseView):
    group_required = ['users']


class AdminView(BaseView):
    group_required = ['admin']
