from django import forms

VENDOR = [
    ('Microsoft', 'Microsoft'),
    ('Google', 'Google'),
]

class CveSearchForm(forms.Form):
    cve = forms.CharField(label='')


class CveProductForm(forms.Form):
    def __init__(self, vendor_choices, *args, **kwargs):
        super(CveProductForm, self).__init__(*args, **kwargs)
        self.fields['vendor'].choices = vendor_choices
    vendor = forms.ChoiceField(choices=())