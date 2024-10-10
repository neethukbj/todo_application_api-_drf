from rest_framework import serializers
from .models import Task

#Model Serializer
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=['id','title','completed','created_at','updated_at']

'''
#Serializer:
class TaskSerializer(serializers.Serializer):
    title= serializers.CharField(max_length=200)
    description=serializers.TextField(blank=True,null=True)
    completed=serializers.BooleanField(default=False)
    created_at=serializers.DateTimeField(auto_now_add=True)
    updated_at=serializers.DateTimeField(auto_now=True)
'''
'''
#HyperlinkModel Serializer
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Task
        fields=['url','title','completed','created_at','updated_at']
'''
