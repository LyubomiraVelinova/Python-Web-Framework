from django import forms

from charityapp.common.models import AboutUsInfo


class AboutUsInfoForm(forms.ModelForm):
    class Meta:
        model = AboutUsInfo
        fields = ['header', 'description']
