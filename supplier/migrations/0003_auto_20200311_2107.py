# Generated by Django 2.2.10 on 2020-03-11 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_auto_20200311_2050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supplier_complaint_categories',
            options={'verbose_name_plural': 'Supplier Enquiry Complaint Categories'},
        ),
        migrations.AlterModelOptions(
            name='supplier_feedback',
            options={'verbose_name_plural': 'Supplier Enquiry Feedbacks'},
        ),
    ]
