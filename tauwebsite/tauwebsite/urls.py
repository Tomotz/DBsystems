"""tauwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
import settings
from users.views import LoginView
from places.views import FoodView, BarView, ClubView, HotelView, ShopView, GeneralPlacesView

urlpatterns = [
    # url(r'^admin/', admin.site.urls),

    # Users API
    url(r'^users/login/(?P<user_name>\w+)/$', LoginView.as_view()),
    url(r'^users/signup/$', LoginView.as_view()),

    # Places API
    url(r'^places/general/$', GeneralPlacesView.as_view()),
    url(r'^places/food/$', FoodView.as_view()),
    url(r'^places/bars/$', BarView.as_view()),
    url(r'^places/hotels/$', HotelView.as_view()),
    url(r'^places/clubs/$', ClubView.as_view()),
    url(r'^places/shops/$', ShopView.as_view()),
]
