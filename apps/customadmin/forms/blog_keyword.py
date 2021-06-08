# -*- coding: utf-8 -*-

from django import forms

from Blog.models import BlogKeyword


# -----------------------------------------------------------------------------
# BlogKeywordCreationForm
# -----------------------------------------------------------------------------

class BlogKeywordCreationForm(forms.ModelForm):
    """Custom BlogKeywordCreationForm"""

    class Meta():
        model = BlogKeyword
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def clean(self):
    #     cleaned_data = super(BlogKeywordCreationForm, self).clean()
    #     group_name = cleaned_data.get("group_name")

    #     if not group_name :
    #         raise forms.ValidationError(
    #             "Please add a group name!."
    #         )
        
    #     if BlogKeyword.objects.filter(group_name__iexact=group_name).exists():
    #         raise forms.ValidationError(
    #             f"{group_name} is already exists!"
    #         )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class BlogKeywordChangeForm(forms.ModelForm):
    """Custom form to change BlogKeyword"""

    class Meta():
        model = BlogKeyword

        fields = '__all__'

    # def clean(self):
    #     cleaned_data = super(BlogKeywordChangeForm, self).clean()
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