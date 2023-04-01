from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/eventos/", include("eventos.urls")),
    path("api/participantes/", include("participantes.urls")),
    path("admin/", admin.site.urls),
]
