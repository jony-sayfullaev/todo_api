from rest_framework.routers import DefaultRouter
from .views import ToDoViewSet
from django.urls import include, path

router = DefaultRouter()
router.register("todo", ToDoViewSet, basename='todo')


urlpatterns = [
    path('', include(router.urls))
]
