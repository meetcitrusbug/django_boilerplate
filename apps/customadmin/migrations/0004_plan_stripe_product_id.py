# Generated by Django 3.2 on 2021-05-24 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0003_auto_20210520_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='stripe_product_id',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
    ]
