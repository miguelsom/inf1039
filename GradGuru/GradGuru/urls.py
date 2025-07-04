from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path("disciplinas/", include("disciplinas.urls", namespace="disciplinas")),
    path("avaliacoes/", include("avaliacoes.urls", namespace="avaliacoes")),
    path("account/", include("account.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]
