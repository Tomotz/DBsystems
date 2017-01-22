from rest_framework import permissions
from rest_framework.views import APIView
from tauwebsite.utils import DBUtils
from tauwebsite.serializers import Serializers
from django.http import HttpResponse, HttpResponseBadRequest

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    # get user by username
    def get(self, request, user_name):
        user = DBUtils.getUserByUname(user_name)
        if user is None:
            return HttpResponseBadRequest()
        else:
            return HttpResponse(Serializers.UserSerizlizer(user))

    # create new user
    def post(self, request, *args, **kwargs):
        user_name = request.data.get("user_name")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        address = request.data.get("address")
        is_update = request.data.get("is_update")

        print "Got data for new user: username '%s', first name '%s', last name '%s', address %s" % (user_name, first_name, last_name, address)

        if is_update:
            user = DBUtils.updateUser(user_name, first_name, last_name, address)
        else:
            user = DBUtils.createNewUser(user_name, first_name, last_name, address)

        if user is None:
            print "user is NONE!!"
            return HttpResponseBadRequest()
        else:
            print "finished, user - %s" % str(user)
            return HttpResponse(Serializers.UserSerizlizer(user))
