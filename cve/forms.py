from django import forms

class CveSearchForm(forms.Form):
    cve = forms.CharField(label='')