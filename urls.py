from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^profile/$', views.ProfileDetailView.as_view(), name='profile'),
    url(r'^profile/edit/$',
        views.ProfileUpdateView.as_view(),
        name='profile_update'
    ),
    url(r'^password-change/$',
        views.PasswordChangeView.as_view(),
        name='password_change'
    ),
    url(r'^password-reset/$',
        views.PasswordResetView.as_view(),
        name='password_reset'
    ),
    url(r'^password-reset/done/$',
        views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.PasswordResetConfirmAndLoginView.as_view(),
        name='password_reset_confirm'
    ),
]
