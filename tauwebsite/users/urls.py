from django.conf.urls import url

from .views import LoginView

urlpatterns = [
    url(r'^login/(?P<user_name>\w+)/$', LoginView.as_view()),
    url(r'^signup/$', LoginView.as_view()),
]
