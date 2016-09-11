from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


def index(request):
    return HttpResponse("Hello there! Remember to Don't fix bug!")


class TestAPIView(APIView):

    def get(self, request, format=None):
        return Response({"it": "works!"}, status=status.HTTP_200_OK)
