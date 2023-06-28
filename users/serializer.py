from rest_framework import serializers
from .models import Project, Developer, Bug, Task

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    bugs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Task
        fields = '__all__'

class DeveloperSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, required=False)
    tasks = TaskSerializer(many=True, required=False)

    class Meta:
        model = Developer
        fields = '__all__'