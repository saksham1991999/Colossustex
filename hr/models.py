from django.db import models

leaveapplication_status_choices = (
    ('P','Pending'),
    ('D','Declined'),
    ('A','Approved'),
)
# Create your models here.
class leaveapplication(models.Model):
    employee = models.ForeignKey('employee.employee', on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    status = models.CharField(choices=leaveapplication_status_choices, max_length=1, default='P')

    def __str__(self):
        return self.employee

    class Meta:
        verbose_name_plural = 'Employee Leave Applications'


