# Generated by Django 2.2 on 2020-04-08 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20200407_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier_quotations',
            name='payment_terms',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='samplerequest',
            name='src',
            field=models.CharField(choices=[('IQ', 'Inquiry'), ('IN', 'Indent'), ('BD', 'Business Development')], max_length=2),
        ),
    ]
