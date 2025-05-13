from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from uploader.router import router as uploader_router

from rest_framework.routers import DefaultRouter

from livraria.views import CategoriaViewSet, EditoraViewSet, AutorViewSet, LivroViewSet
from usuario.router import router as usuario_router

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

# Initialize the router and register viewsets
router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"editoras", EditoraViewSet)
router.register(r"autores", AutorViewSet)
router.register(r"livros", LivroViewSet)

# Define URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/",
         SpectacularSwaggerView.as_view(url_name="schema"),
         name="swagger-ui"),
    path("api/redoc/",
         SpectacularRedocView.as_view(url_name="schema"),
         name="redoc"),
]

# Add static file serving for media
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
