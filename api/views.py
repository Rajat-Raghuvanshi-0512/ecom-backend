from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from .models import User
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view(["POST"])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(email=request.data["email"])
        user.set_password(request.data["password"])
        user.save()
        token = Token.objects.create(user=user)
        response = Response({"token": token.key, "user": serializer.data}, status=200)
        response.set_cookie("token", token.key, httponly=True)
        return response

    return Response(serializer.errors, status=400)


@api_view(["POST"])
def login(request):
    user = get_object_or_404(User, email=request.data["email"])
    if not user.check_password(request.data["password"]):
        return Response({"message": "Invalid email or password"}, status=404)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    response = Response({"token": token.key, "user": serializer.data}, status=200)
    response.set_cookie("token", token.key, httponly=True)
    return response


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    print(request.user.email)
    try:
        request.user.auth_token.delete()
        request.user = None
    except AttributeError:
        return Response({"message": "Can't log out"}, status=400)

    return Response({"message": "Logged out"}, status=200)
