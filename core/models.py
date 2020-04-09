from django.db import models
from django.contrib.auth.models import AbstractUser
from supplier.models import supplier
from agent.models import agent
from buyer.models import buyer
from employee.models import employee
from hr.models import *

Product_PolymerFiber_Choices = (
    ('P', 'Polyster'),
    ('F', 'fiber'),
    ('PA6', 'pa - 6'),
    ('Blnd', 'blend'),
)


Product_Luster_Choices = (
    ('sd', 'Semi Dull'),
    ('brt', 'Bright'),
    ('fd', 'Full Dull'),
)


Product_FilamentCrossSection_Choices = (
    ('C', 'Circular'),
    ('TL', 'Trilobal'),
    ('TA', 'Triangular'),
    ('OL', 'Octalobal'),
    ('S', 'Star'),
    ('R', 'Rice'),
    ('O', 'Orange'),
    ('C', 'Coolmax'),
)


# (sample
#  required / under
#  discussion / feedback
#  awaited / find
#  supplier / couldn
#  't conclude/ confirmed)


Shipment_Status_Choices = (
    ('S','Shipped'),
    ('Di','Dispatch'),
    ('P','Pending'),
    ('Dl','Delivered'),
)

class User(AbstractUser):
    is_supplier = models.BooleanField(default=0)
    is_customer = models.BooleanField(default=0)
    is_agent = models.BooleanField(default=0)
    is_employee = models.BooleanField(default=0)

class office(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    addr1 = models.CharField(max_length=100)
    addr2 = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    country = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Responsible Offices'

#Product Models
class category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Category'

class subcategory1(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Sub-Category 1'

class subcategory2(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Sub-Category 2'

class product_shade(models.Model):
    shade_name =  models.CharField(max_length=50)
    shade_code =  models.CharField(max_length=50)

class intermingle(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Intermingle'

class required_no_of_nips(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Required No of Nips'

class product(models.Model):
    product_code = models.SlugField()
    name = models.CharField(max_length=200)
    category = models.ForeignKey(category, on_delete=models.DO_NOTHING)
    sub_category_1 = models.ForeignKey(subcategory1, on_delete=models.DO_NOTHING)
    sub_category_2 = models.ForeignKey(subcategory2, on_delete=models.DO_NOTHING)
    application = models.CharField(max_length=50)
    polymer_fiber = models.CharField(max_length=4, choices=Product_PolymerFiber_Choices, verbose_name='Polymer/Fiber')
    luster = models.CharField(max_length=4, choices=Product_Luster_Choices)
    filament_cross_section =  models.CharField(max_length=4, choices=Product_FilamentCrossSection_Choices)
    intermingle =  models.ForeignKey(intermingle, on_delete=models.DO_NOTHING)
    required_no_of_nips = models.ForeignKey(required_no_of_nips, on_delete=models.DO_NOTHING)
    lycra_percent_or_any_additional_additive = models.CharField(max_length=4)
    shade = models.ForeignKey(product_shade, on_delete=models.DO_NOTHING)
    additional_info = models.TextField()
    remarks = models.TextField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'

inquiry_source_choices = (
    ('M', 'Mail'),
    ('WC', 'WeChat'),
    ('WP', 'Whatsapp'),
    ('C', 'Call'),
)
inquiry_status_choices = (
    ('O', 'Open'),
    ('CM', 'Confirmed'),
    ('CD', 'Closed'),
)
close_choices = (
    ('HP', 'Prices are High'),
    ('QS', 'Quality Not from nominated Supplier'),
    ('AF', 'Awaiting Feedback'),
    ('UD', 'Under Discussion or Development'),
    ('NO', 'Not Offered'),
)
#INQUIRY DETAILS
class inquiry(models.Model):
    buyer = models.ForeignKey('buyer.buyer', on_delete=models.DO_NOTHING)
    source = models.CharField(max_length=2, choices=inquiry_source_choices)
    status = models.CharField(max_length=2, choices=inquiry_status_choices, default='O')
    close_choice = models.CharField(max_length=2, choices=close_choices, blank=True, null=True)
    inquiry_user = models.ForeignKey('employee.employee', on_delete=models.DO_NOTHING, related_name='inquiry_user')
    confirming_user = models.ForeignKey('employee.employee', on_delete=models.DO_NOTHING, blank=True, null=True, related_name='closing_user')
    agent = models.ForeignKey('agent.agent',on_delete=models.DO_NOTHING, blank=True, null=True, related_name='closing_user')
    remarks = models.TextField(blank=True, null=True)

    received_datetime = models.DateTimeField(auto_now_add=True)
    reply_datetime = models.DateTimeField(blank=True, null=True)
    received_quotation_datetime = models.DateTimeField(blank=True, null=True)
    selected_quotation_datetime = models.DateTimeField(blank=True, null=True)
    customer_feedback_datetime = models.DateTimeField(blank=True, null=True)
    confirmation_datetime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'CTI-' + str(self.id)

    class Meta:
        verbose_name_plural = 'Inquiry Details'

    def inquiry_id(self):
        return 'CTI-'+ str(self.id)

    def suppliers_notified(self):
        print('--------------------------------------NOTIFIED SUPPLIERS--------------')
        notified_suppliers_qs = notified_suppliers.objects.get(inquiry=self)
        suppliers = notified_suppliers_qs.suppliers.all()
        print(suppliers)
        return suppliers

    # def suppliers_notified_otif(self):
    #     timedelta = self.reply_datetime - self.received_datetime
    #     if timedelta.hour > 48:
    #         return False
    #     else:
    #         return True
    #
    # def received_quotation_otif(self):
    #     timedelta = self.received_quotation_datetime - self.received_datetime
    #     if timedelta.hour > 48:
    #         return False
    #     else:
    #         return True
    #
    # def selected_quotation_otif(self):
    #     timedelta = self.selected_quotation_datetime - self.received_datetime
    #     if timedelta.hour > 48:
    #         return False
    #     else:
    #         return True
    #
    # def customer_feedback_otif(self):
    #     timedelta = self.customer_feedback_datetime - self.received_datetime
    #     if timedelta.hour > 15:
    #         return False
    #     else:
    #         return True

class inquiry_product(models.Model):
    inquiry = models.ForeignKey('core.inquiry', on_delete=models.DO_NOTHING)
    product = models.ForeignKey('core.product', on_delete=models.DO_NOTHING)
    qty = models.PositiveSmallIntegerField()
    inco_terms = models.CharField(max_length=56)
    delivery_date = models.DateField()
    payment = models.CharField(max_length=100)
    packing_requirement = models.CharField(max_length=56)
    destination_port = models.CharField(max_length=100)

    def __str__(self):
        return str(self.inquiry) + ' ' + str(self.product)

    class Meta:
        verbose_name_plural = 'Inquiry Products'

class notified_suppliers(models.Model):
    inquiry = models.OneToOneField('core.inquiry', on_delete=models.DO_NOTHING)
    suppliers = models.ManyToManyField('supplier.supplier')

    def __str__(self):
        return str(self.inquiry)

    class Meta:
        verbose_name_plural = 'Inquiry Notified Suppliers'

class supplier_quotations(models.Model):
    inquiry = models.ForeignKey('core.inquiry', on_delete=models.DO_NOTHING)
    supplier = models.ForeignKey('supplier.supplier', on_delete=models.DO_NOTHING)
    product = models.ForeignKey('core.inquiry_product', on_delete=models.DO_NOTHING)
    price_kg = models.PositiveIntegerField()
    payment_terms = models.CharField(max_length=100)

    def __str__(self):
        return str(self.product) + ': ' + str(self.supplier) + ' - ' + str(self.price_kg)

    class Meta:
        verbose_name_plural = 'Inquiry Supplier Quotations'

class forwarded_quotation(models.Model):
    inquiry = models.OneToOneField('core.inquiry', on_delete=models.DO_NOTHING)
    quotations = models.ManyToManyField('core.supplier_quotations')

    def __str__(self):
        return str(self.inquiry)

    class Meta:
        verbose_name_plural = 'Inquiry Customer Forwarded Quotations'

class inquiry_update(models.Model):
    inquiry = models.ForeignKey('core.inquiry', on_delete=models.DO_NOTHING)
    employee = models.ForeignKey('employee.employee', on_delete=models.DO_NOTHING)
    update_date_time = models.DateField(auto_now_add=True)
    subject = models.CharField(max_length=256)
    content = models.TextField()
    document = models.FileField(blank=True, null=True)

    def __str__(self):
        return str(self.inquiry)

    class Meta:
        verbose_name_plural = 'Inquiry Customer Feedback'

sample_request_choices = (
    ('IQ', 'Inquiry'),
    ('IN', 'Indent'),
    ('BD', 'Business Development'),
)
#Sample Requirement
class SampleRequest(models.Model):
    src = models.CharField(max_length=2, choices=sample_request_choices)
    receiving_date = models.DateField(auto_now_add=True)
    inquiry = models.ForeignKey('core.inquiry', on_delete=models.DO_NOTHING, blank=True, null=True)
    # indent = models.ForeignKey('core.inquiry', on_delete=models.DO_NOTHING, blank=True, null=True)
    # bd_activity = models.ForeignKey('core.inquiry', on_delete=models.DO_NOTHING, blank=True, null=True)

    supplier = models.ForeignKey('supplier.supplier', on_delete=models.DO_NOTHING)
    delivered_date = models.DateField(blank=True, null=True)

    def get_products(self):
        products = SampleRequestProduct.objects.filter(sample_request=self)
        return products

    def get_customer_sample_ref(self):
        sample_refs = CustomerSampleRef.objects.filter(sample_request=self)
        return sample_refs

    def get_dispatch_details(self):
        dispatch_details = SampleRequestDispatch.objects.filter(sample_request=self)
        return dispatch_details

    def get_feedbacks(self):
        feedbacks = SampleRequestFeedback.objects.filter(sample_request = self)
        return feedbacks

    def get_customer_sample_ref_date(self):
        try:
            sample_refs = CustomerSampleRef.objects.filter(sample_request=self).last()
            date = sample_refs.date
            return date
        except:
            return None

    def get_dispatch_detail_date(self):
        try:
            dispatch_details = SampleRequestDispatch.objects.filter(sample_request=self)[0]
            return dispatch_details.date
        except:
            return None

    def get_feedback_date(self):
        try:
            feedbacks = SampleRequestFeedback.objects.filter(sample_request = self)[0]
            return feedbacks.date
        except:
            return None


class SampleRequestProduct(models.Model):
    sample_request = models.ForeignKey('core.SampleRequest', on_delete=models.DO_NOTHING)
    product = models.ForeignKey('core.product', on_delete=models.DO_NOTHING)
    quality_detail = models.CharField(max_length=256)
    quality_instruction = models.CharField(max_length=256)
    number_of_cones = models.PositiveSmallIntegerField()
    weight_cone = models.FloatField()
    packing_detail = models.CharField(max_length=256)
    date = models.DateField(auto_now_add=True)

class CustomerSampleRef(models.Model):
    sample_request = models.ForeignKey('core.SampleRequest', on_delete=models.DO_NOTHING)
    ref = models.CharField(max_length=256)
    file_1 = models.FileField()
    file_2 = models.FileField(blank=True, null=True)
    file_3 = models.FileField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

class SampleRequestDispatch(models.Model):
    sample_request = models.ForeignKey('core.SampleRequest', on_delete=models.DO_NOTHING)
    file_1 = models.FileField()
    courier_details = models.CharField(max_length=256)
    date = models.DateField(auto_now_add=True)
    estimate_delivery = models.DateField()

class SampleRequestFeedback(models.Model):
    sample_request = models.ForeignKey('core.SampleRequest', on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()
    file_1 = models.FileField(blank=True, null=True)
    file_2 = models.FileField(blank=True, null=True)
    file_3 = models.FileField(blank=True, null=True)







#Indent Details

class order(models.Model):
    enquiry_no = models.SlugField()
    date_of_inquiry = models.DateField()
    responsible_office = models.ForeignKey(office ,on_delete=models.DO_NOTHING)
    product = models.ForeignKey(product, on_delete=models.DO_NOTHING)
    final_supplier = models.ForeignKey(supplier, on_delete=models.DO_NOTHING, related_name='final_supplier')
    customer = models.ForeignKey(buyer, on_delete=models.DO_NOTHING)
    agent = models.ForeignKey(agent, on_delete=models.DO_NOTHING)
    po_no = models.CharField(max_length=20)
    contract_no = models.CharField(max_length=20)
    price_kg = models.IntegerField()
    quantity = models.IntegerField()
    dispatch_qty = models.IntegerField()
    contract_value = models.IntegerField()
    quantity_discount = models.IntegerField()
    insurance = models.IntegerField()
    remarks = models.CharField(max_length=100)
    extra_remarks = models.TextField()

    financial_year = models.CharField(max_length=4)
    month = models.CharField(max_length=10)
    status = models.BooleanField(default=0)
    order_confirmation = models.CharField(max_length = 4)

    indenting_commission = models.IntegerField()
    agent_commission = models.IntegerField()
    suppliers_quotation = models.ManyToManyField(supplier, related_name='initial_suppliers')

    def __str__(self):
        return self.enquiry_no

    class Meta:
        verbose_name_plural = 'Enquiry Details'

class bill(models.Model):
    enquiry = models.ForeignKey(order, on_delete=models.DO_NOTHING)
    currency = models.CharField(max_length=10)
    invoice_date = models.DateField()
    invoice_number = models.CharField(max_length=10)
    invoice_value = models.FloatField()
    commission = models.FloatField()
    cash_discount = models.FloatField()
    freight = models.FloatField()
    insurance = models.FloatField()
    gst = models.FloatField()
    total_amount = models.FloatField()
    total_amount_payable = models.FloatField()
    remarks = models.CharField(max_length=50)
    additional_remark = models.TextField()

    def __str__(self):
        return self.invoice_number

    class Meta:
        verbose_name_plural = 'Bill/Invoice'

class payment(models.Model):
    bill = models.ForeignKey(bill, on_delete=models.DO_NOTHING)
    currency = models.CharField(max_length=10)
    payment_terms = models.CharField(max_length=100)
    payment_due_date = models.DateField()
    remarks = models.CharField(max_length=200)
    additional_remarks = models.TextField()
    payment_status = models.BooleanField(default=0)


    def __str__(self):
        return '1'

    class Meta:
        verbose_name_plural = 'Payment Details'

class shipment(models.Model):
    enquiry = models.ForeignKey(order, on_delete=models.DO_NOTHING)
    freight = models.FloatField()
    dispatch_by = models.CharField(max_length=100)
    delivery_date = models.DateField()
    otif = models.BooleanField(default=0)
    inco_terms = models.CharField(max_length=100)
    place_of_delivery = models.CharField(max_length=100)
    remarks = models.CharField(max_length=50)
    additional_remarks = models.TextField()

    port_of_discharge = models.CharField(max_length=50)
    courier_details = models.CharField(max_length=100)
    email_date = models.DateField()
    dispatch_summary_otif = models.BooleanField(default=0)
    post_shipment_otif = models.BooleanField(default=0)
    copy_of_shipment = models.BooleanField(default=0)
    documents_otif = models.BooleanField(default=0)
    status = models.CharField(max_length=4, choices=Shipment_Status_Choices)

    def __str__(self):
        return self.enquiry

    class Meta:
        verbose_name_plural = 'Shipment Details'












# ---------------------------------------------------------------------------------------------------

class to_do(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    is_important = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = 'To Do\'s'

note_tag_choices = (
    ('P', 'Personal'),
    ('W', 'Work'),
    ('S', 'Social'),
    ('I', 'Important'),
)

class note(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    is_favourite = models.BooleanField(default=0)
    tag = models.CharField(max_length=1, choices=note_tag_choices)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = 'Notes'


event_tag_choices = (
    ('P', 'Personal'),
    ('W', 'Work'),
    ('T', 'Travel'),
    ('I', 'Important'),
)

class event(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    content = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    tag = models.CharField(max_length=1, choices=event_tag_choices)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = 'Calendar Events'

update_choices = (
    ('IU', 'Industry Updates'),
    ('TA', 'Technological Advancements'),
    ('IDT', 'International Duties and Trade'),
    ('PTA', 'Price Trend Analysis'),
)


class updates(models.Model):
    category = models.CharField(max_length=3, choices=update_choices)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Updates/News'

class notifications(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null= True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'User Notisfications'

class suplus_product(models.Model):
    product = models.ForeignKey(product, on_delete=models.DO_NOTHING,  blank=True, null=True)
    supplier = models.ForeignKey('supplier.supplier', on_delete=models.DO_NOTHING)
    other_product = models.CharField(max_length=200, blank=True, null=True)
    qty = models.IntegerField()
    price_unit = models.IntegerField()
    employee = models.ForeignKey('employee.employee', on_delete=models.DO_NOTHING)
    location = models.CharField(max_length=256)
    document = models.FileField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.product:
            return self.product
        else:
            return self.other_product

    class Meta:
        verbose_name_plural = 'Suplus Product Details'