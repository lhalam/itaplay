from rest_framework import serializers
from projects.models import AdviserProject


class AdviserProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    # TODO Add id_company field
    name = serializers.CharField(max_length=30)
    description = serializers.CharField(max_length=150)
    # TODO Integrate with project_template

    def create(self, validated_data):
        """
        Create and return a new "AdviserProject" instance, given the validated data.
        """
        return AdviserProject.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing "AdviserProject" instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.project_template = validated_data.get('project_template', instance.project_template)
        instance.save()
        return instance
