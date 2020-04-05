from django.db import models



# Create your models here.



class buyer(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.DO_NOTHING, blank=True, null=True)
    ctc = models.SlugField()
    name = models.CharField(max_length=100)
    buyer_name = models.CharField(max_length=100)
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
        verbose_name_plural = 'Buyers'



class buyer_complaint_categories(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Buyer Order Complaint Categories'

class buyer_complaints(models.Model):
    order = models.ForeignKey('core.order', on_delete=models.DO_NOTHING)
    buyer = models.ForeignKey(buyer, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(buyer_complaint_categories, on_delete=models.DO_NOTHING)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name_plural = 'Buyer Order Complaints'

class buyer_general_feedback_categories(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Buyer General Order Feedback Categories'


class buyer_general_feedback(models.Model):
    buyer = models.ForeignKey(buyer, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(buyer_general_feedback_categories, on_delete=models.DO_NOTHING)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.buyer) + '-' + str(self.subject)

    class Meta:
        verbose_name_plural = 'Buyer General Order Feedbacks'

class complaint_response(models.Model):
    complaint = models.ForeignKey(buyer_complaints, on_delete=models.DO_NOTHING)
    user = models.ForeignKey('core.User', on_delete=models.DO_NOTHING, related_name='buyer_complaint_user')
    message = models.TextField()

    def __str__(self):
        return str(self.complaint)

    class Meta:
        verbose_name_plural = 'Complaint Responses'
