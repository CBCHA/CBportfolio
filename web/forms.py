from django import forms
from .models import MailBox

class MailBoxForm(forms.ModelForm):

    class Meta:
        model = MailBox
        fields = ['name', 'email', 'memo' ]