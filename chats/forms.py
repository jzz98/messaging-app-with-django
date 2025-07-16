from django.forms import ModelForm
from .models import ContactsModel

class ContactForm(ModelForm):
    class Meta:
        model = ContactsModel
        fields = ['userd_id', 'username']
        