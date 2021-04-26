# Generated by Django 3.2 on 2021-04-22 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notification', '0003_auto_20210420_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.group'),
        ),
        migrations.AddField(
            model_name='notification',
            name='is_singleuser',
            field=models.BooleanField(default=False, help_text='Is Single User?', verbose_name='Is Single User?'),
        ),
        migrations.AddField(
            model_name='notification',
            name='status',
            field=models.CharField(blank=True, choices=[('SENT', 'SENT'), ('PENDING', 'PENDING')], help_text='Notification Status', max_length=255, null=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(blank=True, choices=[('OTHER', 'OTHER'), ('BOOKING', 'BOOKING')], help_text='Notification Type', max_length=255, null=True, verbose_name='Types'),
        ),
    ]
