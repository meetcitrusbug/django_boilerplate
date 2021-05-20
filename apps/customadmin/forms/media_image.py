from django import forms
from mediacategory_api.models import MediaImage


# -----------------------------------------------------------------------------
# MediaImage
# -----------------------------------------------------------------------------

class MediaImageCreationForm(forms.ModelForm):
    """Custom MediaImageCreationForm"""

    class Meta():
        model = MediaImage
        fields = [
            "image",
            "category",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(MediaImageCreationForm, self).clean()
        image = cleaned_data.get("image")
        category = cleaned_data.get("category")

        if not image :
            raise forms.ValidationError(
                "Please upload a image!."
            )

        if not category :
            raise forms.ValidationError(
                "Please select a category!"
            )
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance


class MediaImageChangeForm(forms.ModelForm):
    """Custom form to change MediaImage"""

    class Meta():
        model = MediaImage
        fields = [
            "image",
            "category",
        ]

    def clean(self):
        cleaned_data = super(MediaImageChangeForm, self).clean()
        image = cleaned_data.get("image")
        category = cleaned_data.get("category")
        
        if not image :
            raise forms.ValidationError(
                "Please upload a image!."
            )

        if not category :
            raise forms.ValidationError(
                "Please select a category!"
            )

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance