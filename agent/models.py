from django.db import models
# Create your models here.

class agent(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.DO_NOTHING, blank=True, null=True)
    cta = models.SlugField()
    name = models.CharField(max_length=100)
    addr1 = models.CharField(max_length=100)
    addr2 = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    country = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    commission = models.IntegerField(blank=True, null = True)
    email = models.EmailField()
    document = models.FileField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Agents'



class agent_complaint_categories(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'agent Order Complaint Categories'


class agent_complaints(models.Model):
    enquiry = models.ForeignKey('core.order', on_delete=models.DO_NOTHING)
    agent = models.ForeignKey(agent, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(agent_complaint_categories, on_delete=models.DO_NOTHING)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.enquiry

    class Meta:
        verbose_name_plural = 'agent Order Complaints'

class agent_general_feedback_categories(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'agent General Order Feedback Categories'


class agent_general_feedback(models.Model):
    agent = models.ForeignKey(agent, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(agent_general_feedback_categories, on_delete=models.DO_NOTHING)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.agent) + '-' + str(self.subject)

    class Meta:
        verbose_name_plural = 'agent General Order Feedbacks'

class complaint_response(models.Model):
    complaint = models.ForeignKey(agent_complaints, on_delete=models.DO_NOTHING)
    user = models.ForeignKey('core.User', on_delete=models.DO_NOTHING, related_name='agent_complaint_user')
    message = models.TextField()

    def __str__(self):
        return self.complaint

    class Meta:
        verbose_name_plural = 'Complaint Responses'
