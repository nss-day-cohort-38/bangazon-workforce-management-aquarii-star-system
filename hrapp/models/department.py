from django.db import models
from django.urls import reverse

class Department(models.Model):

    dept_name = models.CharField(max_length=50)
    budget = models.FloatField()

    class Meta:
        verbose_name = ("department")
        verbose_name_plural = ("departments")

    def __str__(self):
        return self.dept_name

    def get_absolute_url(self):
        return reverse("department_detail", kwargs={"pk": self.pk})
