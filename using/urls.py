from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[

        path('sign-in/', auth_views.login,{'template_name':'login.html'},name="sign-in"),
        path('sign-up', views.sign_up, name="sign-up"),
        path('logout', auth_views.logout,{'next_page':'/'}, name="logout"),
        path('profile', views.profile, name='profile'),
        
        path('change-password', auth_views.PasswordChangeView.as_view(template_name='change-password.html'),name='change-password'),
        path('change-password-done', auth_views.password_change_done, {'template_name':'done-password.html'}, name="password_change_done"),
]
