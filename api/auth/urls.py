from django.urls import path, include
from . import views

urlpatterns = [
    path("signup", views.register),
    path("signin", views.login),
    path("logout", views.logout),
]
