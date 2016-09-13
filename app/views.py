from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from app.models import TestModel, TestSerializer


def index(request):
    return HttpResponse("Hello there! Remember to Don't fix bug!")


class TestAPIView(APIView):

    def get(self, request, format=None):
        return Response({"it": TestSerializer(TestModel.objects.all(), many=True, read_only=True).data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """
        This only supports single entry. To add data post a value like this:
        {
            "test_name": "Test Name #1"
        }
        """

        test_name = request.data.get("test_name")
        TestModel.objects.create(test_name=test_name)
        return Response("Done!", status=status.HTTP_200_OK)
