from rest_framework import serializers
from .models import AddDetails


class AddDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddDetails
        fields = ('username', 'emailaddress',)
