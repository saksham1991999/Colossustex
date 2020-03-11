from django.db import models

# Create your models here.
class leaveapplication(models.Model):
    employee = models.ForeignKey('employee.employee', on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.employee

    class Meta:
        verbose_name_plural = 'Employee Leave Applications'


