from django.test import TestCase

# Create your tests here.

from rest_framework.test import APITestCase
from rest_framework import status
from .models import Maintenance
from django.urls import reverse

class MaintenanceTests(APITestCase):

    def setUp(self):
        # Set up test data: create a Maintenance task
        self.task_data = {
            "vehicle_registration_number": "ABC123",
            "task_description": "Oil Change",
            "next_due_date": "2025-03-30T10:00:00Z",
            "is_completed": False
        }
        self.task = Maintenance.objects.create(**self.task_data)
        self.url = reverse('task-list')  # This is the URL for listing tasks

    def test_create_task(self):
        """Test creating a maintenance task"""
        url = reverse('task-create')  # URL for creating a task
        data = {
            "vehicle_registration_number": "XYZ789",
            "task_description": "Tire Replacement",
            "next_due_date": "2025-05-30T10:00:00Z",
            "is_completed": False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Maintenance.objects.count(), 2)

    def test_list_tasks(self):
        """Test retrieving the list of maintenance tasks"""
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Initially 1 task in the DB

    def test_retrieve_task(self):
        """Test retrieving a specific maintenance task by ID"""
        url = reverse('task-detail', args=[self.task.id])  # Get the specific task by its ID
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['vehicle_registration_number'], self.task.vehicle_registration_number)

    def test_update_task(self):
        """Test updating an existing maintenance task"""
        url = reverse('task-update', args=[self.task.id])
        data = {
            "vehicle_registration_number": "ABC123",
            "task_description": "Oil Change (Updated)",
            "next_due_date": "2025-04-01T10:00:00Z",
            "is_completed": True
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()  # Refresh the task object from DB to check updated values
        self.assertEqual(self.task.task_description, "Oil Change (Updated)")

    def test_delete_task(self):
        """Test deleting a maintenance task"""
        url = reverse('task-delete', args=[self.task.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Maintenance.objects.count(), 0)  # No tasks left in the DB after deletion

