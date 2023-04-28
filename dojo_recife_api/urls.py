from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/eventos/", include("dojo_recife_api.eventos.urls")),
    path("api/participantes/", include("dojo_recife_api.participantes.urls")),
    path("admin/", admin.site.urls),
]
