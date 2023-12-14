from django.urls import path
from . import views

urlpatterns = [
    path("signup", views.register),
    path("signin", views.register),
    path("logout", views.register),
]
