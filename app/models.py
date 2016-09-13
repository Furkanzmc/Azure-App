from django.db import models
from rest_framework import serializers


class TestModel(models.Model):
    test_name = models.CharField(max_length=128, blank=False, default="Test Name #1")


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestModel
        fields = (
            'test_name',
        )
