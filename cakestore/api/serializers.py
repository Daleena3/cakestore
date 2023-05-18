from rest_framework import serializers
from  api.models import Cakes


class CakeSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)

    class Meta:
        model=Cakes
        fields="__all__"
         