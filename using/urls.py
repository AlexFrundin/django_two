from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[

        path('sign-in', auth_views.login,{'template_name':'login.html'},name="sign-in"),

]
