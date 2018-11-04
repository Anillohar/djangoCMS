from .models import Settings
from django import forms

class SettingsForm(forms.ModelForm):

    class Meta:
        model = Settings
        fields = ('title' , 'key' , 'value' , 'Editable' , 'type')