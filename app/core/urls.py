# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, ScheduleViewSet, AssignmentViewSet, NotificationViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


