from django.conf.urls import url

from . import views


urlpatterns = [
    url('^login/$', views.LoginView.as_view(), name='login'),
    url('^logout/$', views.LogoutView.as_view(), name='logout'),
]
