from rest_framework.response import Response
from rest_framework import status
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


# class AuthMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         excluded_paths = ["/signin/", "/signup/"]

#         if request.path_info in excluded_paths:
#             response = self.get_response(request)
#         else:
#             if not request.user.is_authenticated:
#                 return Response(
#                     {"detail": "Authentication credentials were not provided."},
#                     status=status.HTTP_401_UNAUTHORIZED,
#                 )

#         return response


class AuthMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        user = request.user
        print(user)
        excluded_paths = ["/api/signin", "/api/signup"]

        if request.path_info in excluded_paths:
            return None
        elif user.is_authenticated:
            return HttpResponse(status=200)
        else:
            return HttpResponse("Unauthorised", status=401)
