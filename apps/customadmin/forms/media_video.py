from django import forms
from mediacategory_api.models import MediaVideo


# -----------------------------------------------------------------------------
# MediaVideo
# -----------------------------------------------------------------------------

class MediaVideoCreationForm(forms.ModelForm):
    """Custom MediaVideoCreationForm"""

    class Meta():
        model = MediaVideo
        fields = [
            "video",
            "category",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(MediaVideoCreationForm, self).clean()
        video = cleaned_data.get("video")
        category = cleaned_data.get("category")

        if not video :
            raise forms.ValidationError(
                "Please upload a video!."
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


class MediaVideoChangeForm(forms.ModelForm):
    """Custom form to change MediaVideo"""

    class Meta():
        model = MediaVideo
        fields = [
            "video",
            "category",
        ]

    def clean(self):
        cleaned_data = super(MediaVideoChangeForm, self).clean()
        video = cleaned_data.get("video")
        category = cleaned_data.get("category")

        if not video :
            raise forms.ValidationError(
                "Please upload a video!."
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