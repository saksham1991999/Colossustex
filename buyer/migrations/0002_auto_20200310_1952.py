# Generated by Django 2.2.10 on 2020-03-10 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('buyer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='sample_request',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.order'),
        ),
        migrations.AddField(
            model_name='complaint_response',
            name='complaint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='buyer.buyer_complaints'),
        ),
        migrations.AddField(
            model_name='complaint_response',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='buyer_complaint_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='buyer_general_feedback',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='buyer.buyer'),
        ),
        migrations.AddField(
            model_name='buyer_general_feedback',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='buyer.buyer_general_feedback_categories'),
        ),
        migrations.AddField(
            model_name='buyer_complaints',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='buyer.buyer'),
        ),
        migrations.AddField(
            model_name='buyer_complaints',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.order'),
        ),
        migrations.AddField(
            model_name='buyer_complaints',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='buyer.buyer_complaint_categories'),
        ),
        migrations.AddField(
            model_name='buyer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
