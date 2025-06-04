from django.http import HttpResponse


def index(request):
    return HttpResponse("LMS backend is running")
