from django import forms
from mediacategory_api.models import MediaCategory


# -----------------------------------------------------------------------------
# MediaCategory
# -----------------------------------------------------------------------------

class MediaCategoryCreationForm(forms.ModelForm):
    """Custom MediaCategoryCreationForm"""

    class Meta():
        model = MediaCategory
        fields = [
            "category",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(MediaCategoryCreationForm, self).clean()
        category = cleaned_data.get("category")

        if not category :
            raise forms.ValidationError(
                "Please add a category name!"
            )
        
        if MediaCategory.objects.filter(category__iexact=category).exists():
            raise forms.ValidationError(
                f"{category} is already exists!"
            )
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance


class MediaCategoryChangeForm(forms.ModelForm):
    """Custom form to change MediaCategory"""

    class Meta():
        model = MediaCategory
        fields = [
            "category",
        ]

    def clean(self):
        cleaned_data = super(MediaCategoryChangeForm, self).clean()
        category = cleaned_data.get("category")

        if not category :
            raise forms.ValidationError(
                "Please add a category name!"
            )

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance