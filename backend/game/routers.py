from rest_framework.routers import SimpleRouter
from game.viewsets import UserViewSet
from game.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet


routes = SimpleRouter()

# AUTHENTICATION
routes.register(r"login", LoginViewSet, basename="auth-login")
routes.register(r"register", RegistrationViewSet, basename="auth-register")
routes.register(r"refresh", RefreshViewSet, basename="auth-refresh")

# USER
routes.register(r"user", UserViewSet, basename="user")


urlpatterns = [*routes.urls]
