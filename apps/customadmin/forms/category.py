# -*- coding: utf-8 -*-

from django import forms

from Blog.models import Category


# -----------------------------------------------------------------------------
# Category
# -----------------------------------------------------------------------------

class CategoryCreationForm(forms.ModelForm):
    """Custom CategoryCreationForm"""

    class Meta():
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def clean(self):
    #     cleaned_data = super(BlogCreationForm, self).clean()
    #     group_name = cleaned_data.get("group_name")

    #     if not group_name :
    #         raise forms.ValidationError(
    #             "Please add a group name!."
    #         )
        
    #     if Blog.objects.filter(group_name__iexact=group_name).exists():
    #         raise forms.ValidationError(
    #             f"{group_name} is already exists!"
    #         )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class CategoryChangeForm(forms.ModelForm):
    """Custom form to change Creation"""

    class Meta():
        model = Category

        fields = '__all__'

    # def clean(self):
    #     cleaned_data = super(BlogChangeForm, self).clean()
    #     group_name = cleaned_data.get("group_name")

    #     if not group_name :
    #         raise forms.ValidationError(
    #             "Please add group name!"
    #         )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance