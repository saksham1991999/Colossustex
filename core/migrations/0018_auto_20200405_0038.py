# Generated by Django 2.2.10 on 2020-04-04 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20200403_2027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='samplerequest',
            old_name='cti',
            new_name='inquiry',
        ),
        migrations.RemoveField(
            model_name='samplerequest',
            name='courier_details',
        ),
        migrations.AddField(
            model_name='samplerequest',
            name='delivered_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='SampleRequestProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality_detail', models.CharField(max_length=256)),
                ('quality_instruction', models.CharField(max_length=256)),
                ('number_of_cones', models.PositiveSmallIntegerField()),
                ('weight_cone', models.FloatField()),
                ('packing_detail', models.CharField(max_length=256)),
                ('sample_request', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.SampleRequest')),
            ],
        ),
        migrations.CreateModel(
            name='SampleRequestFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('content', models.TextField()),
                ('file_1', models.FileField(upload_to='')),
                ('file_2', models.FileField(upload_to='')),
                ('file_3', models.FileField(upload_to='')),
                ('sample_request', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.SampleRequest')),
            ],
        ),
        migrations.CreateModel(
            name='SampleRequestDispatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_1', models.FileField(upload_to='')),
                ('courier_details', models.CharField(max_length=256)),
                ('date', models.DateField(auto_now_add=True)),
                ('estimate_delivery', models.DateField(blank=True, null=True)),
                ('sample_request', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.SampleRequest')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerSampleRef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=256)),
                ('file_1', models.FileField(upload_to='')),
                ('file_2', models.FileField(upload_to='')),
                ('file_3', models.FileField(upload_to='')),
                ('date', models.DateField(auto_now_add=True)),
                ('sample_request', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.SampleRequest')),
            ],
        ),
    ]
