from django.db import models
# Create your models here.





class department(models.Model):
    title = models.CharField(max_length=5)

    def __str__(self):
        return self.title


class employee(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(department, on_delete=models.DO_NOTHING, blank=True, null=True)
    dob = models.DateField()
    addr1 = models.CharField(max_length=100)
    addr2 = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    country = models.CharField(max_length=20)
    country_code = models.CharField(max_length=3, default='91')
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    image = models.ImageField(blank=True, null=True)
    document = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Employees'


employee_visit_categories = (
    ('S', 'Supplier'),
    ('A', 'Sub-Agent'),
    ('B', 'Buyer'),
)

class employee_visit(models.Model):
    employee = models.ForeignKey(employee, on_delete=models.DO_NOTHING)
    visiting = models.CharField(max_length=1, choices=employee_visit_categories)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    remark = models.TextField(blank=True, null = True)
    email = models.EmailField(blank=True, null = True)
    long = models.IntegerField(blank=True, null = True)
    lat = models.IntegerField(blank=True, null = True)
    file1 = models.FileField(blank=True, null = True)
    file2 = models.FileField(blank=True, null = True)
    file3 = models.FileField(blank=True, null = True)


    def __str__(self):
        return self.employee

    class Meta:
        verbose_name_plural = 'Employee Notes (Visit Details)'

class inspection(models.Model):
    inspection_officer = models.CharField(max_length=100)
    inspection_officer_contact = models.CharField(max_length=15)
    enquiry = models.ForeignKey('core.order', on_delete=models.DO_NOTHING)
    document = models.FileField()
    inspection_confirmation = models.BooleanField(default=0)
    inspection_remarks = models.CharField(max_length=100)
    inspection_additional_remarks = models.TextField()

    def __str__(self):
        return self.enquiry

    class Meta:
        verbose_name_plural = 'Inspection Details'
