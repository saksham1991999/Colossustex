from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
Product_Category_Choices = (
    ('P', 'Polyster'),
)

Product_PolymerFiber_Choices = (
    ('P', 'Polyster'),
    ('F', 'fiber'),
    ('PA6', 'pa - 6'),
    ('Blnd', 'blend'),
)


Product_Luster_Choices = (
    ('sd', 'Semi Dull'),
    ('brt', 'Bright'),
    ('sbrt', 'superbrt'),
)


Product_FilamentCrossSection_Choices = (
    ('C', 'Circular'),
    ('cir', 'cir'),
    ('tbl', 'tbl'),
    ('T', 'triangular'),
)

Product_TexSpecification_Choices = (
    ('210', '210mm'),
    ('z-t', 'z - twist'),
    ('na', 'Not Applicable'),
)

Product_NoOfNips_Choices = (
    ('40-50', '40 - 50'),
    ('85-90', '85 - 90'),
    ('sim', 'sim'),
    ('na', 'Not Applicable'),
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
    tex_specification =  models.CharField(max_length=4, choices=Product_TexSpecification_Choices)
    required_no_of_nips =  models.CharField(max_length=4, choices=Product_NoOfNips_Choices)
    lycra_percent_or_any_additional_additive = models.CharField(max_length=4)
    shade_name =  models.CharField(max_length=50)
    shade_code =  models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'

class supplier(models.Model):
    cts = models.SlugField()
    products = models.ManyToManyField(product)
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

class customer(models.Model):
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
        verbose_name_plural = 'Customers'

class agent(models.Model):
    cta = models.SlugField()
    name = models.CharField(max_length=100)
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
        verbose_name_plural = 'Agents'

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

class employee(models.Model):
    cti = models.SlugField()
    name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    dob = models.DateField()
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
        verbose_name_plural = 'Employees'

class order(models.Model):
    inquiry_no = models.SlugField()
    date_of_inquiry = models.DateField()
    responsible_office = models.ForeignKey(office ,on_delete=models.DO_NOTHING)
    product = models.ForeignKey(product, on_delete=models.DO_NOTHING)
    final_supplier = models.ForeignKey(supplier, on_delete=models.DO_NOTHING, related_name='final_supplier')
    customer = models.ForeignKey(customer, on_delete=models.DO_NOTHING)
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
    commission = models.IntegerField()
    net_commission = models.IntegerField()
    commission_on_invoice_beneficiary = models.IntegerField()
    suppliers_quotation = models.ManyToManyField(supplier, related_name='initial_suppliers')

    def __str__(self):
        return self.inquiry_no

    class Meta:
        verbose_name_plural = 'Order Details'

class supplierquotation(models.Model):
    supplier = models.ForeignKey(supplier, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(order, on_delete=models.DO_NOTHING)
    available_quantity = models.FloatField()
    price_kg = models.FloatField()
    total_amount = models.FloatField()
    gst = models.FloatField()
    freight = models.FloatField()
    discount = models.FloatField()
    total_amount_payable = models.FloatField()
    document = models.FileField()

    def __str__(self):
        name = str(self.order) + ' ' + str(self.supplier)
        return name

    class Meta:
        verbose_name_plural = 'Supplier Quotations'

class bill(models.Model):
    order = models.ForeignKey(order, on_delete=models.DO_NOTHING)
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
    cuurency = models.CharField(max_length=10)
    payment_terms = models.CharField(max_length=100)
    payment_due_date = models.DateField()
    remarks = models.CharField(max_length=200)
    additional_remarks = models.TextField()
    payment_status = models.BooleanField(default=0)


    def __str__(self):
        return self.bill

    class Meta:
        verbose_name_plural = 'Payment Details'

class shipment(models.Model):
    order = models.ForeignKey(order, on_delete=models.DO_NOTHING)
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
        return self.order

    class Meta:
        verbose_name_plural = 'Shipment Details'

class customerfeedback(models.Model):
    order = models.ForeignKey(order, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(customer, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.order

    class Meta:
        verbose_name_plural = 'Customer Feedbacks'




