# Generated by Django 2.2.10 on 2020-03-11 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0003_auto_20200311_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='leaveapplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employee.employee')),
            ],
            options={
                'verbose_name_plural': 'Employee Leave Applications',
            },
        ),
    ]
