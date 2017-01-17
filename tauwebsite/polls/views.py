from django.http import HttpResponse
# from django.db import connection
#
#
# def my_custom_sql(self):
#     with connection.cursor() as cursor:
# #        cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
# #        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
#         cursor.execute("SELECT * FROM Addr")
#         row = cursor.fetchone()
#
#     return row

def Index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
