from django.db import models
from django_boilerplate.models import ActivityTracking

class UserCard(ActivityTracking):
    user = models.ForeignKey("django_boilerplate.User", on_delete=models.CASCADE)
    card_number = models.CharField(max_length=200, blank=True, null=True)
    object = models.CharField(max_length=200, blank=True, null=True)
    address_city = models.CharField(max_length=200, blank=True, null=True)
    address_country = models.CharField(max_length=200, blank=True, null=True)
    address_line1 = models.CharField(max_length=200, blank=True, null=True)
    address_line1_check = models.CharField(max_length=200, blank=True, null=True)
    address_line2 = models.CharField(max_length=200, blank=True, null=True)
    address_state = models.CharField(max_length=200, blank=True, null=True)
    address_zip = models.CharField(max_length=200, blank=True, null=True)
    address_zip_check = models.CharField(max_length=200, blank=True, null=True)
    brand = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    customer = models.CharField(max_length=200, blank=True, null=True)
    cvc_check = models.CharField(max_length=200, blank=True, null=True)
    dynamic_last4 = models.CharField(max_length=200, blank=True, null=True)
    exp_month = models.CharField(max_length=200, blank=True, null=True)
    exp_year = models.CharField(max_length=200, blank=True, null=True)
    fingerprint = models.CharField(max_length=200, blank=True, null=True)
    funding = models.CharField(max_length=200, blank=True, null=True)
    last4 = models.CharField(max_length=200, blank=True, null=True)
    metadata = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    tokenization_method = models.CharField(max_length=200, blank=True, null=True)
    is_default = models.BooleanField(default=False)
    

    def __str__(self):
        return self.card_number

    class Meta:
        verbose_name = "User Card Detail"
        verbose_name_plural = "User Card Details"
        ordering = ["-created_at"]