# Generated by Django 2.2 on 2020-04-10 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0004_remove_supplier_consignee'),
        ('core', '0023_auto_20200409_0513'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry_product',
            name='suppliers',
            field=models.ManyToManyField(to='supplier.supplier'),
        ),
    ]
