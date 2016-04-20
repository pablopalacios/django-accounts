from django.conf.urls import url

from . import views


urlpatterns = [
    url('^users/$', views.UsersView.as_view(), name='users'),
    url('^admin/$', views.AdminView.as_view(), name='admin'),
]
