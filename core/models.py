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
    source = models.CharField(max_length=100)
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
    other_product = models.CharField(max_length=200, blank=True, null=True)
    qty = models.IntegerField()
    price_unit = models.IntegerField()
    office = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100)
    supplier_mob = models.CharField(max_length=15, blank=True, null=True)
    remarks = models.TextField( blank=True, null=True)

    def __str__(self):
        if self.product:
            return self.product
        else:
            return self.other_product

    class Meta:
        verbose_name_plural = 'Suplus Product Details'