from rest_framework import serializers
from django.contrib.auth.models import User
from player.models import Player
from company.models import Company
from authentication.models import AdviserUser

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username','email', 'last_name', 'first_name')

class CompanySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'company_name')

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
