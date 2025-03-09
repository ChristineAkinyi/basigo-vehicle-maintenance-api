from rest_framework import serializers
from maintenance.models import Maintenance

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'

    # Adding help text and validation
    vehicle_registration_number = serializers.CharField(
        max_length=100,
        help_text="The registration number of the vehicle being serviced."
    )
    service_type = serializers.CharField(
        max_length=50,
        help_text="Type of service performed (e.g., oil change, tire replacement)."
    )
    service_date = serializers.DateField(
        help_text="The date when the maintenance service was performed."
    )
    mileage = serializers.IntegerField(
        help_text="The mileage of the vehicle when the service was performed."
    )
    # Custom validation for vehicle_registration_number
    def validate_vehicle_registration_number(self, value):
        if not value:
            raise serializers.ValidationError("Vehicle registration number is required.")
        return value

    # Custom validation for service_type
    def validate_service_type(self, value):
        if not value:
            raise serializers.ValidationError("Service type is required.")
        return value

    # You can add similar validations for other fields if necessary
    def validate_service_date(self, value):
        if value is None:
            raise serializers.ValidationError("Service date is required.")
        return value

    def validate_mileage(self, value):
        if value is None:
            raise serializers.ValidationError("Mileage is required.")
        return value
