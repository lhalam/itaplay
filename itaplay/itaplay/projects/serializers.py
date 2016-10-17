from rest_framework import serializers

from player.models import Player
from company.models import Company
from projects.models import AdviserProject


class AdviserProjectSerializer(serializers.Serializer):
    """
    Serializer for AdviserProject
    """
    id = serializers.IntegerField(read_only=True)
    id_company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    name = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=150)

    def create(self, validated_data):
        """
        Create and return a new "AdviserProject" instance, given the validated data.
        Also send created AdviserProject to selected players
        """
        new_project = AdviserProject.objects.create(**validated_data)
        players = self.initial_data.get("players", [])
        Player.send_project(players, new_project)
        return new_project

    def update(self, instance, validated_data):
        """
        Update and return an existing "AdviserProject" instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.project_template = validated_data.get('project_template', instance.project_template)
        instance.save()
        return instance
