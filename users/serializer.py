from rest_framework import serializers
from .models import Project, Developer, Bug, Task


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class BugSerializer(serializers.ModelSerializer):
    bugs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Bug
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'