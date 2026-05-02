from django.shortcuts import render
from rest_framework import viewsets
from .models import Task, Category, Tag
from .serializers import (TaskListSerializer, TaskDetailSerializer,  TaskCreateUpdateSerializer)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskListSerializer
        if self.action in ['create', 'update', 'partial_update']:
            return TaskCreateUpdateSerializer
        return TaskDetailSerializer