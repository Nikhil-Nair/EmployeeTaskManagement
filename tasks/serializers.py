from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    user  = serializers.CharField(source='user.username',read_only=True)
    class Meta:
        model = Task
        fields = ('user','created','task_name', 'task_description', 'task_due')
