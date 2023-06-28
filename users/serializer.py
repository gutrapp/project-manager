from rest_framework import serializers
from .models import Project, Developer, Team


class DeveloperSerializer(serializers.ModelSerializer):
    teams = serializers.PrimaryKeyRelatedField(many=True)
    
    class Meta:
        model = Developer
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    teams = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name']