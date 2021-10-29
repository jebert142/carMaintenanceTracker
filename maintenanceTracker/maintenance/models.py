from django.db import models

# This class defines the model for each new vehicle that the user can add
class Vehicle(models.Model):
    # vehicle_id
    name = models.CharField(max_length=150)
    model_year  = models.IntegerField()
    mileage = models.IntegerField()
    last_service = models.DateField()

    def __str__(self):
        return self.name


# This class defines the model for each log that can be appended to a vehicle's maintenance history
class Log(models.Model):
    # log_id
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    date = models.DateField()


    def __str__(self):
        return self.title