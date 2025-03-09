# urls.py
from django.urls import path
from .views import (
    MaintenanceCreateView,
    MaintenanceListView,
    MaintenanceDetailView,
    MaintenanceUpdateView,
    MaintenanceDeleteView
)

urlpatterns = [
    path('tasks/', MaintenanceListView.as_view(), name='task-list'),  # List of tasks with filtering
    path('tasks/<int:pk>/', MaintenanceDetailView.as_view(), name='task-detail'),  # Retrieve a specific task by ID
    path('tasks/create/', MaintenanceCreateView.as_view(), name='task-create'),  # Create a new task
    path('tasks/<int:pk>/update/', MaintenanceUpdateView.as_view(), name='task-update'),  # Update a task
    path('tasks/<int:pk>/delete/', MaintenanceDeleteView.as_view(), name='task-delete'),  # Delete a task
]
