# Generated by Django 3.2 on 2021-05-11 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0008_auto_20210511_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.group'),
        ),
    ]