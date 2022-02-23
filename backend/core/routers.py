from rest_framework.routers import SimpleRouter
from core.viewsets import UserViewSet
from core.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet


routes = SimpleRouter()

# AUTHENTICATION
routes.register(r"login", LoginViewSet, basename="auth-login")
routes.register(r"register", RegistrationViewSet, basename="auth-register")
routes.register(r"refresh", RefreshViewSet, basename="auth-refresh")

# USER
routes.register(r"user", UserViewSet, basename="user")


urlpatterns = [*routes.urls]
