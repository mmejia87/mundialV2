"""mundial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from re import U
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from equipos import views
from equipos.views import equipos
from grupos.views import grupos
from django.contrib.staticfiles.urls import staticfiles_urlpatterns





urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipos/', equipos),
    path('grupos/', grupos),
    path('busqueda/',views.busqueda_equipos),

]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

