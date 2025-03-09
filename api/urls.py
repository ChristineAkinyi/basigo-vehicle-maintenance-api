from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.MaintenanceListView.as_view(), name='task-list'),
    path('tasks/create/', views.MaintenanceCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', views.MaintenanceDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', views.MaintenanceUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', views.MaintenanceDeleteView.as_view(), name='task-delete'),
]
