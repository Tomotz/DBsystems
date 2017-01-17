from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from rest_framework import serializers, permissions
from rest_framework.views import APIView
from tauwebsite.tauwebsite.utils import DBUtils


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    # get user by username
    def get(self, request, user_name):
        user = DBUtils.get_user_by_uname(user_name)
        if user is None:
            return HttpResponseBadRequest()
        else:
            return HttpResponse(user)

    # create new user
    def post(self, request, *args, **kwargs):
        user_name = request.data.get("user_name")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        address = request.data.get("address")

        print( "Got data for new user: first name '%s', last name '%s', address %s" % (first_name, last_name, address))
        return HttpResponse("Hello, world. FNAME - %s" % first_name)
