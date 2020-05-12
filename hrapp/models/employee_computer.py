from django.db import models

class EmployeeComputer(models.Model):
    """
    Creates the join table for the many to many relationship between computers and employees
    Author: Joe Shep
    methods: none
    """

    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    computer = models.ForeignKey("Computer", on_delete=models.CASCADE)
    assign_date = models.DateField()
    unassign_date = models.DateField(null=True, blank=True, default=None)
