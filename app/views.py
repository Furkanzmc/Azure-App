from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello there! Remember to Don't fix bug!")
