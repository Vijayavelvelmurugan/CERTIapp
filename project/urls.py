"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include 
from app.views import custom_login, homepage, logout_view, about, signup
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from app import views






urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='signup/'), name='home'),
    path('login/', custom_login, name='custom_login'),
    path('logout/', logout_view, name='logout'),
    path('about/', about, name='about'),
    path('signup/', signup, name='signup'),
    path('homepage/', homepage, name='homepage'),
    path('generate_certificate/', views.generate_certificate, name='generate_certificate'),
]

