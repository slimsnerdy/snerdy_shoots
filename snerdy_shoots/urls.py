"""
URL configuration for snerdy_shoots project.

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

from django.conf import settings
from django.conf.urls.static import static

from environs import Env

env = Env()
env.read_env()

#PRODUCTION/LIVE
urlpatterns = [
    path(env.str('BOSSY'), admin.site.urls), #HIDDEN 🐯
    path('', include('contact.urls')),
    path('', include('photography.urls')),  # Include the app's URLs with the new app name
    path('captcha/', include('captcha.urls')),
]

#LOCAL
if settings.DEBUG:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('contact.urls')),
        path('', include('photography.urls')),  # Include the app's URLs with the new app name
        path('captcha/', include('captcha.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'snerdy_shoots.views.custom_404'