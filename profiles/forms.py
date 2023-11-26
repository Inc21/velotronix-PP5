from django import forms
from .models import UserProfile
from django_countries.widgets import CountrySelectWidget


class UserProfileForm(forms.ModelForm):
    """ User profile form """
    class Meta:
        model = UserProfile
        fields = ('full_name', 'email', 'phone_number', 'street_address1',
                  'street_address2', 'postcode', 'town_or_city',
                  'county', 'country',)
        widgets = {"country": CountrySelectWidget()}

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'county': 'County',
            'country': 'Select Country',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = (
                    'border rounded-1 profile-form-input')
            self.fields[field].label = False
