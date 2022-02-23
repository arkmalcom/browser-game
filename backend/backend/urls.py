"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework.routers import DefaultRouter
from core.viewsets import *
from game.viewsets import *
from game.auth.viewsets import *

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"characters", CharacterViewSet, basename="character")
router.register(r"enemies", EnemyViewSet, basename="enemy")
router.register(r"items", ItemViewSet, basename="item")
router.register(r"player-classes", PlayerClassViewSet, basename="player-class")
router.register(r"skills", SkillViewSet, basename="skill")

schema_view = get_schema_view(
    openapi.Info(
        title="Game API",
        default_version="v0.0.1",
        description="This is the API for an as-of-yet untitled RPG.",
    ),
    public=True,
    patterns=router.urls,
)


urlpatterns = [
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="game-api-root"),
    path("admin/", admin.site.urls),
    path("auth/", include(("core.routers", "core"), namespace="auth-api")),
] + router.urls
