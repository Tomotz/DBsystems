import MySQLdb as mdb


from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from rest_framework import serializers, permissions
from rest_framework.views import APIView

#from django.db import connection


def my_custom_sql():
    db = mdb.connect("127.0.0.1", "root", "Ru30299008012061989", "DbMysql17", port=3306)
    with db:
        cursor = db.cursor()
#    with connection.cursor() as cursor:
#        cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
#        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        cursor.execute("SELECT * FROM Addr")
        row = cursor.fetchone()

    return row


def index(request):
    return HttpResponse("Hello, world. Users Index!!!.")

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    # get user by username
    def get(self, request, user_name):
        row = my_custom_sql()
        print row
        return HttpResponseBadRequest()
        return HttpResponseForbidden()
        return HttpResponse("Hello, world.  %s" % row)

    # create new user
    def post(self, request, *args, **kwargs):
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        address = request.data.get("address")

        print( "Got data for new user: first name '%s', last name '%s', address %s" % (first_name, last_name, address))
        return HttpResponse("Hello, world. FNAME - %s" % first_name)
