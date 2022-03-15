"""
IPEDS API serializers.
"""

from rest_framework import serializers
from .models import IPEDSDictionary, InstitutionProfile

class IPEDSDictionarySerializer(serializers.ModelSerializer):
    """
    Serializer for the IPEDSDictionary model.
    """
    class Meta:
        model = IPEDSDictionary
        fields = '__all__'

class InstitutionProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the InstitutionalProfile model.
    """
    class Meta:
        model = InstitutionProfile
        fields = '__all__'
