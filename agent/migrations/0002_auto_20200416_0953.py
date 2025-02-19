# Generated by Django 2.2 on 2020-04-16 04:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agent', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint_response',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='agent_complaint_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agent_general_feedback',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='agent.agent'),
        ),
        migrations.AddField(
            model_name='agent_general_feedback',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='agent.agent_general_feedback_categories'),
        ),
        migrations.AddField(
            model_name='agent_complaints',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='agent.agent'),
        ),
        migrations.AddField(
            model_name='agent_complaints',
            name='enquiry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.order'),
        ),
        migrations.AddField(
            model_name='agent_complaints',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='agent.agent_complaint_categories'),
        ),
        migrations.AddField(
            model_name='agent',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
