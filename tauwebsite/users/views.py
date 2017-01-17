# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework import permissions
from rest_framework.views import APIView
from tauwebsite.utils import DBUtils
from tauwebsite.serializers import Serializers

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
        print "Got data for new user: username '%s', first name '%s', last name '%s', address %s" % (user_name, first_name, last_name, address)
        user = DBUtils.createNewUser(user_name, first_name, last_name, address)
        if user is None:
            return HttpResponseBadRequest()
        else:
            return HttpResponse(Serializers.UserSerizlizer(user))


class FoodView(APIView):
    permission_classes = (permissions.AllowAny,)

    # get user by username
    def get(self, request, user_name):
        pass

class BarView(APIView):
    permission_classes = (permissions.AllowAny,)

    # get user by username
    def get(self, request, user_name):
        pass

class ClubView(APIView):
    permission_classes = (permissions.AllowAny,)

    # get user by username
    def get(self, request, user_name):
        pass

class HotelView(APIView):
    permission_classes = (permissions.AllowAny,)

    # get user by username
    def get(self, request, user_name):
        pass
