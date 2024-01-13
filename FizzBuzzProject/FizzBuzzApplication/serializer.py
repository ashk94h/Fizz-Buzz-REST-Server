from .models import Parameter
from rest_framework import serializers

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        # fields = "__all__"
        exclude = ['hits']