from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[

        path('sign-in', auth_views.login,{'template_name':'login.html'},name="sign-in"),
        path('sign-up', views.sign_up, name="sign-up"),
        path('logout', auth_views.logout,{'next_page':'/'}, name="logout"),
]
