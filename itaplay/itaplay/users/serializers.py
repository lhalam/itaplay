from rest_framework import serializers
from django.contrib.auth.models import User
from player.models import Player
from company.models import Company
from authentication.models import AdviserUser, AdviserInvitations

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for User
    """
    class Meta:
        model = User
        fields = ('id', 'username','email', 'last_name', 'first_name')

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Company
    """
    class Meta:
        model = Company
        fields = ('id', 'name')

class AdviserUsersSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for AdviserUsers
    """
    id = serializers.IntegerField(read_only=True)
    id_company = CompanySerializer()
    avatar = serializers.URLField(default="default-user-logo.png")
    user = UserSerializer()

    class Meta:
        model = AdviserUser
        fields = ('id', 'avatar', 'id_company', 'user')


class AdviserInvitationsSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for AdviserInvitations
    """
    id = serializers.IntegerField(read_only=True)
    id_company = CompanySerializer()
    email = serializers.EmailField()
    verification_code = serializers.CharField()
    is_active = serializers.BooleanField()

    class Meta:
        model = AdviserInvitations
        fields = ('id', 'email', 'id_company', 'verification_code', 'is_active')
