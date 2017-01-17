from django.conf.urls import url

from .views import index, LoginView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/(?P<user_name>\w+)/$', LoginView.as_view()),
]
