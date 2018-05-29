from rest_framework import serializers
from .models import AddDetails


class AddDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddDetails
        fields = ('username', 'emailaddress',)
        # To get all the fields of the relation yoou can use
        # fields = '__all__'
