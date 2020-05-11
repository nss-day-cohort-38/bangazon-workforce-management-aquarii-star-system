from django.db import models
from django.urls import reverse

class EmployeeTrainingProgram (models.Model):
  
    title = models.CharField(max_length=55)
    start_date = models.DateField()
    end_date = models.DateField()
    capacity = models.IntegerField()
    
    class Meta:
        verbose_name = ("employee_training_program") 
        verbose_name_plural = ("employee_training_programs")
        
    def __str__(self):
        return self.title
      
    def get_absolute_url(self):
        return reverse("employee_training_programs _detail", kwargs={"pk": self.pk})
    