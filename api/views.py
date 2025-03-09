from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from maintenance.models import Maintenance
from .serializers import MaintenanceSerializer

# Create a new maintenance task
class MaintenanceCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MaintenanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve a list of all maintenance tasks
class MaintenanceListView(APIView):
    def get(self, request, *args, **kwargs):
        vehicle_reg = request.query_params.get('vehicle_registration_number', None)
        
        if vehicle_reg:
            tasks = Maintenance.objects.filter(vehicle_registration_number=vehicle_reg)
        else:
            tasks = Maintenance.objects.all()
        
        serializer = MaintenanceSerializer(tasks, many=True)
        return Response(serializer.data)

# Retrieve a specific maintenance task by ID
class MaintenanceDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            task = Maintenance.objects.get(pk=pk)
        except Maintenance.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MaintenanceSerializer(task)
        return Response(serializer.data)

# Update an existing maintenance task
class MaintenanceUpdateView(APIView):
    def patch(self, request, pk, *args, **kwargs):
        try:
            task = Maintenance.objects.get(pk=pk)
        except Maintenance.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MaintenanceSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a maintenance task
class MaintenanceDeleteView(APIView):
    def delete(self, request, pk, *args, **kwargs):
        try:
            task = Maintenance.objects.get(pk=pk)
        except Maintenance.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response({"detail": "Task deleted."}, status=status.HTTP_204_NO_CONTENT)

