from rest_framework import serializers
from .models import Users, Organization


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'phone', 'is_active', 'valid_until')
        # exclude = ('password', 'created_at', 'updated_at', '')
        # read_only_fields = ['password']
        # read_only_fields = ['first_name', 'last_name','phone','is_active']
        


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Organization
        fields = ('first_name', 'last_name', 'company_name', 'phone', 'email', 'address', 'valid_until', 'is_active', 'org_id')
        # exclude = ('created_at', 'updated_at', 'created_by')
