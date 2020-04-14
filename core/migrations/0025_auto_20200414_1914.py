# Generated by Django 2.2 on 2020-04-14 13:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20200414_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier_quotations',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier_quotations',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
