from django import forms
from .models import contacts
from django.core.exceptions import ValidationError

comm_pref_options = (
            ('E','Email'),
            ('M','Mail'),
            ('P','Phone'),
            ('T','Text Messages'),
            )

class ContactForm(forms.ModelForm):
    class Meta:
        model = contacts
        fields = [
            'fname', 'lname', 'email', 'street_addr', 'city', 'state', 'zip_code', 'phone', 'years_participated', 'project_updates', 'news_events', 'comm_pref', 'unsubscribe'
        ]
        widgets = {
            'fname' : forms.TextInput(attrs={'class': 'form-control'}),
            'lname' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'street_addr' : forms.TextInput(attrs={'class': 'form-control'}),
            'city' : forms.TextInput(attrs={'class': 'form-control'}),
            'state' : forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code' : forms.TextInput(attrs={'class': 'form-control'}),
            'phone' : forms.TextInput(attrs={'class': 'form-control'}),
            'years_participated' : forms.TextInput(attrs={'class': 'form-control'}),
            'comm_pref' : forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_years_participated(self, *args, **kwargs):
        years_participated = self.cleaned_data.get("years_participated")
        if not isinstance(years_participated, int):
            raise forms.ValidationError("Please enter a whole number")
        return years_participated
