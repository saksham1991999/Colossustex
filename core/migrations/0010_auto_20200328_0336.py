# Generated by Django 2.2.10 on 2020-03-27 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200328_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier_quotations',
            name='inquiry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.inquiry'),
        ),
    ]
