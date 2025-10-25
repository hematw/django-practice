from django import forms
from .models import Link

# class LinkForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     url = forms.CharField(max_length=200)
#     slug = forms.SlugField()


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ["name", "url", "slug"]