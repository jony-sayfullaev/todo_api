from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from todo.serializers import TodoSerializer
from .models import Todo
# Create your views here.


class ToDoViewSet(ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    # queryset = Todo.objects.all() => 
    def get_queryset(self):
        return Todo.objects.all()
