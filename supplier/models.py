from django.db import models
# Create your models here.

class supplier(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.DO_NOTHING, blank=True, null = True)
    cts = models.SlugField()
    products = models.ManyToManyField('core.product')
    name = models.CharField(max_length=100)
    consignee = models.CharField(max_length=100)
    addr1 = models.CharField(max_length=100)
    addr2 = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    country = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    document = models.FileField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Suppliers'


class supplierquotation(models.Model):
    supplier = models.ForeignKey(supplier, on_delete=models.DO_NOTHING)
    enquiry = models.ForeignKey('core.order', on_delete=models.DO_NOTHING)
    available_quantity = models.FloatField()
    price_kg = models.FloatField()
    total_amount = models.FloatField()
    gst = models.FloatField()
    freight = models.FloatField()
    discount = models.FloatField()
    total_amount_payable = models.FloatField()
    document = models.FileField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        name = str(self.enquiry) + ' ' + str(self.supplier)
        return name

    class Meta:
        verbose_name_plural = 'Supplier Quotations'


class supplier_feedback_categories(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Supplier Order Feedback Categories'


class supplier_feedback(models.Model):
    supplier = models.ForeignKey(supplier, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(supplier_feedback_categories, on_delete=models.DO_NOTHING)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + str(self.subject)

    class Meta:
        verbose_name_plural = 'Supplier Enquiry Feedbacks'

    def get_feedback_id(self):
        return 'SOC' + str(id)

class supplier_complaint_categories(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Supplier Enquiry Complaint Categories'

class supplier_complaints(models.Model):
    enquiry = models.ForeignKey('core.order', on_delete=models.DO_NOTHING)
    supplier = models.ForeignKey(supplier, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(supplier_feedback_categories, on_delete=models.DO_NOTHING)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def get_complaint_id(self):
        return 'SOC' + str(id)

    def __str__(self):
        return str(self.enquiry) + self.get_complaint_id()

    class Meta:
        verbose_name_plural = 'Supplier Enquiry Complaints'


class complaint_response(models.Model):
    complaint = models.ForeignKey(supplier_complaints, on_delete=models.DO_NOTHING)
    user = models.ForeignKey('core.User', on_delete=models.DO_NOTHING, related_name='supplier_complaint_user')
    message = models.TextField()

    def __str__(self):
        return self.complaint

    class Meta:
        verbose_name_plural = 'Complaint Responses'
