# Generated by Django 2.2.10 on 2020-03-11 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supplier_complaint_categories',
            options={'verbose_name_plural': 'Supplier enquiry Complaint Categories'},
        ),
        migrations.AlterModelOptions(
            name='supplier_complaints',
            options={'verbose_name_plural': 'Supplier Enquiry Complaints'},
        ),
        migrations.AlterModelOptions(
            name='supplier_feedback',
            options={'verbose_name_plural': 'Supplier enquiry Feedbacks'},
        ),
        migrations.RenameField(
            model_name='supplier_complaints',
            old_name='order',
            new_name='enquiry',
        ),
        migrations.RenameField(
            model_name='supplierquotation',
            old_name='order',
            new_name='enquiry',
        ),
        migrations.AlterField(
            model_name='supplier',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
