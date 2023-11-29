from django import forms
from .models import About, Contact
from django_summernote.widgets import SummernoteWidget


class AboutForm(forms.ModelForm):
    """ About form """
    class Meta:
        model = About
        fields = ('delivery_info', 'returns_info', 'faq', 'privacy_policy')
        widgets = {
            'delivery_info': SummernoteWidget(),
            'returns_info': SummernoteWidget(),
            'faq': SummernoteWidget(),
            'privacy_policy': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field """
        super().__init__(*args, **kwargs)
        placeholders = {
            'delivery_info': 'Delivery information',
            'returns_info': 'Returns information',
            'faq': 'FAQ',
            'privacy_policy': 'Privacy policy',
        }

        self.fields['delivery_info'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'border rounded-1 profile-form-input')
        self.fields[field].label = False


class ContactForm(forms.ModelForm):
    """
    This class is used to create a form for the ContactForm model.
    """
    class Meta:
        model = Contact
        fields = ['author', 'email', 'subject', 'message']
        labels = {
            'author': '',
            'email': '',
            'subject': '',
            'message': ''
        }
        widgets = {
          'author': forms.TextInput(attrs={'placeholder': 'Name *'}),
          'email': forms.EmailInput(attrs={'placeholder': 'Email *'}),
          'subject': forms.TextInput(attrs={'placeholder': 'Subject *'}),
          'message': forms.Textarea(attrs={
              'rows': 4, 'placeholder': 'Message *'}),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
