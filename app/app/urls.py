from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    # Admin App
    path("admin/", admin.site.urls),
    # Core app
    path("", include("core.urls")),
    # Accounts app
    path("accounts/", include("accounts.urls")),
    # API Docs
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/dev/schema/swagger",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/dev/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
