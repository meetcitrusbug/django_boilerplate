from django.contrib import admin

from django.utils.translation import ugettext_lazy as _

from .models import Plan, PlanFeature, Card, SubscriptionOrder, UserProfile

# Register your models here.

admin.site.register(Plan)
admin.site.register(PlanFeature)
admin.site.register(Card)
admin.site.register(UserProfile)
admin.site.register(SubscriptionOrder)
