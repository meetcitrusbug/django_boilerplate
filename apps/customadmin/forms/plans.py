# -*- coding: utf-8 -*-

from django import forms

from ..models import Plan, PlanFeature
# -----------------------------------------------------------------------------
# Plans
# -----------------------------------------------------------------------------
class PlanCreationForm(forms.ModelForm):
    """Custom OneToOneSessionCreationForm."""

    class Meta:
        model = Plan
        fields = [
            "name",
            "plan_amount",
            "discount_amount",
            "duration_in_months",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['duration_in_months'].required = False

    def clean(self):
        cleaned_data = super(PlanCreationForm, self).clean()
        name = cleaned_data.get("name")
        plan_amount = cleaned_data.get("plan_amount")
        discount_amount = cleaned_data.get("discount_amount")
        duration_in_months = cleaned_data.get("duration_in_months")
        instance = Plan.objects.filter(name=name, plan_amount=plan_amount,duration_in_months=duration_in_months).first()

        if instance:
            raise forms.ValidationError(
                "Plan already exists."
            )

        if not name:
            raise forms.ValidationError(
                "Please enter plan name."
            )
        if float(plan_amount) < 0.0:
            raise forms.ValidationError(
                "Amount must be grater than zero."
            )
        if int(duration_in_months) < 1:
            raise forms.ValidationError(
                "Duration of Plan is greater than and equal to 1."
            )
        if int(duration_in_months) > 12:
            raise forms.ValidationError(
                "Duration of Plan is less than and equal to 12."
            )
        if not discount_amount:
            raise forms.ValidationError(
                "Discount amount is required."
            )
        if float(discount_amount)<0.0:
            raise forms.ValidationError(
                "Discount amount must be greater than zero."
            )
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance



class PlanChangeForm(forms.ModelForm):
    """Custom OneToOneSessionChangeForm."""
    class Meta:
        model = Plan
        fields = (
            "name",
            "plan_amount",
            "discount_amount",
            "duration_in_months",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['duration_in_months'].required = False


    def clean(self):
        cleaned_data = super(PlanChangeForm, self).clean()
        name = cleaned_data.get("name")
        plan_amount = cleaned_data.get("plan_amount")
        discount_amount = cleaned_data.get("discount_amount")
        duration_in_months = cleaned_data.get("duration_in_months")

        if Plan.objects.filter(name=name, plan_amount=plan_amount, duration_in_months=duration_in_months).exclude(pk=self.instance.id).count() > 0:
            raise forms.ValidationError(
                "Plan already exists."
            )
        if not name:
            raise forms.ValidationError(
                "Please enter plan name."
            )
        if float(plan_amount) < 0.0:
            raise forms.ValidationError(
                "Amount must be grater than zero."
            )
        if float(discount_amount) < 0.0:
            raise forms.ValidationError(
                "Amount must be grater than zero."
            )
        if int(duration_in_months) < 1:
            raise forms.ValidationError(
                "Duration of Plan is more than 1."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance

# -----------------------------------------------------------------------------
# Plan's Covers
# -----------------------------------------------------------------------------


class PlanFeatureCreationForm(forms.ModelForm):
    """Custom TimeSlotCreationForm."""

    class Meta:
        model = PlanFeature
        fields = [
            "features",
            "plan"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance


class PlanFeatureChangeForm(forms.ModelForm):
    """Custom TimeSlotChangeForm."""
    class Meta:
        model = PlanFeature
        fields = (
            "features",
            "plan",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance