from django.contrib import admin
from django.urls import path

from thirdApp.views import seisPerfectos
from thirdApp.views import Diccionario

urlpatteerns = [
    path('admin/', admin.site.urls),
    path("perfects/", seisPerfectos),
    path("Dicc/", Diccionario)
]