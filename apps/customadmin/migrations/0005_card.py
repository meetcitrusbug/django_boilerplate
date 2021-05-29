# Generated by Django 3.2 on 2021-05-26 06:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customadmin', '0004_plan_stripe_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_card_id', models.CharField(blank=True, max_length=255, verbose_name='Stripe customer Id')),
                ('last4', models.CharField(blank=True, max_length=255, verbose_name='Last 4 digits')),
                ('card_expiration_date', models.CharField(blank=True, max_length=222, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
    ]