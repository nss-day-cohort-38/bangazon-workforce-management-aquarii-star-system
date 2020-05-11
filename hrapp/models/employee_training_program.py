from django.db import models
from django.urls import reverse

class EmployeeTrainingProgram (models.Model):
  
    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    training_program = models.ForeignKey("TrainingProgram", on_delete=models.CASCADE)
    