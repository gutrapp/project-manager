from rest_framework import serializers
from .models import Project
from ..developer.serializer import TeamSerializer

class ProjectSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True)
    
    class Meta:
        model = Project
        fields = '__all__'