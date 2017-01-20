from django.shortcuts import render

# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework import permissions
from rest_framework.views import APIView
from tauwebsite.utils import DBUtils
from tauwebsite.serializers import Serializers


class PLACE_TYPES:
    FOOD  = "Restaurant"
    BAR   = "Bar"
    SHOP  = "Shop"
    CLUB  = "Club"
    HOTEL = "Hotel"

class GeneralPlacesView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        lat = request.data.get("lat")
        lng = request.data.get("lng")

        data = DBUtils.topNotch(lat, lng)

        return HttpResponse(Serializers.PlaceSerializer(data))

class FoodView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        lat = request.data.get("lat")
        lng = request.data.get("lng")
        radius = request.data.get("radius")

        data = DBUtils.aroundMe(lat, lng, PLACE_TYPES.FOOD, radius)

        return HttpResponse(Serializers.PlaceSerializer(data))


class BarView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        lat = request.data.get("lat")
        lng = request.data.get("lng")
        radius = request.data.get("radius")

        data = DBUtils.aroundMe(lat, lng, PLACE_TYPES.BAR, radius)

        return HttpResponse(Serializers.PlaceSerializer(data))


class ClubView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        lat = request.data.get("lat")
        lng = request.data.get("lng")
        radius = request.data.get("radius")

        data = DBUtils.aroundMe(lat, lng, PLACE_TYPES.CLUB, radius)

        return HttpResponse(Serializers.PlaceSerializer(data))


class HotelView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        lat = request.data.get("lat")
        lng = request.data.get("lng")
        radius = request.data.get("radius")

        data = DBUtils.aroundMe(lat, lng, PLACE_TYPES.HOTEL, radius)

        return HttpResponse(Serializers.PlaceSerializer(data))


class ShopView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        lat = request.data.get("lat")
        lng = request.data.get("lng")
        radius = request.data.get("radius")

        data = DBUtils.aroundMe(lat, lng, PLACE_TYPES.SHOP, radius)

        return HttpResponse(Serializers.PlaceSerializer(data))

