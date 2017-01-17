from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import serializers, permissions

def index(request):
    return HttpResponse("Hello, world. Users Index!!!.")

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, user_name):
        return HttpResponse("Hello, world. UNAME - %s" % user_name)
