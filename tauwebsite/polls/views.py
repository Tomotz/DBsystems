from django.http import HttpResponse


def Index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
