from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns=[
    path('base/<str:pid>', views.base),
    path("",views.base),

    path('sign-in', auth_views.login, {'template_name':'user_auth/sign-in.html'}, name='user-sign-in'),
    path('sign-out', auth_views.logout, {'next_page':"/"}, name='user-sign-out'),
    path('sign-up', views.sign_up, name="user-sign-up"),


    path('index.html', RedirectView.as_view(url='base/')),
    path('add/<str:pid>', views.add_product, name="add_product"),
]
