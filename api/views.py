from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(["POST"])
def register(request):
    return Response({"message": "Successfully registered"}, status=200)


@api_view(["POST"])
def login(request):
    return Response({"message": "Successfully registered"}, status=200)


@api_view(["GET"])
def logout(request):
    return Response({"message": "Successfully registered"}, status=200)
