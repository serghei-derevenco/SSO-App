"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path('login/', views.login, name="login"),
    path('login/discord', views.discord_login, name="discord_login"),
    path('login/discord/redirect', views.discord_login_redirect, name="discord_login_redirect"),
    path('login/mail', views.mail_login, name="mail_login"),
    path('login/mail/redirect', views.mail_login_redirect, name="mail_login_redirect"),
    path('login/bitbucket', views.bitbucket_login, name="bitbucket_login"),
    path('login/bitbucket/redirect', views.bitbucket_login_redirect, name="bitbucket_login_redirect"),
]
