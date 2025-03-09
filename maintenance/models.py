from django.db import models

class Maintenance(models.Model):
    vehicle_registration_number = models.CharField(max_length=100)
    task_description = models.TextField()
    date_performed = models.DateTimeField(auto_now_add=True)
    next_due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Task for {self.vehicle_registration_number} on {self.date_performed}"
