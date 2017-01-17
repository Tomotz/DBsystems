from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from rest_framework.views import APIView
from rest_framework import serializers, permissions

def index(request):
    return HttpResponse("Hello, world. Users Index!!!.")

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    # get user by username
    def get(self, request, user_name):
        return HttpResponseBadRequest()
        return HttpResponseForbidden()
        return HttpResponse("Hello, world. UNAME - %s" % user_name)

    # create new user
    def post(self, request, *args, **kwargs):
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        address = request.data.get("address")

        print "Got data for new user: first name '%s', last name '%s', address %s" % (first_name, last_name, address)
        return HttpResponse("Hello, world. FNAME - %s" % first_name)
