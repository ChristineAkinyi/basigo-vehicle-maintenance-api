# maintenance/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from api.serializers import MaintenanceSerializer  # Import from the 'api' app
from .models import Maintenance

# View for creating a new maintenance task
class MaintenanceCreateView(APIView):
    @swagger_auto_schema(
        operation_description="Create a new maintenance task",
        responses={201: MaintenanceSerializer, 400: 'Bad Request'}
    )

    def post(self, request, *args, **kwargs):
        serializer = MaintenanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View for retrieving all maintenance tasks with filtering by vehicle registration number
class MaintenanceListView(APIView):

    @swagger_auto_schema(
        operation_description="Retrieve a list of all maintenance tasks",
        responses={200: MaintenanceSerializer(many=True)}
    )
    
    def get(self, request, *args, **kwargs):
        vehicle_reg = request.query_params.get('vehicle_registration_number', None)
        if vehicle_reg:
            tasks = Maintenance.objects.filter(vehicle_registration_number=vehicle_reg)
        else:
            tasks = Maintenance.objects.all()

        serializer = MaintenanceSerializer(tasks, many=True)
        return Response(serializer.data)

# View for retrieving a specific maintenance task by ID
class MaintenanceDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            task = Maintenance.objects.get(pk=pk)
        except Maintenance.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MaintenanceSerializer(task)
        return Response(serializer.data)

# View for updating a maintenance task
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

# View for deleting a maintenance task
class MaintenanceDeleteView(APIView):
    def delete(self, request, pk, *args, **kwargs):
        try:
            task = Maintenance.objects.get(pk=pk)
        except Maintenance.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response({"detail": "Task deleted."}, status=status.HTTP_204_NO_CONTENT)
