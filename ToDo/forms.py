from .models import Affairs
from django.forms import ModelForm, BooleanField, CheckboxInput

class AffairsForm(ModelForm):
    checkbox = BooleanField(widget=CheckboxInput(attrs={
        'id' : 'checkbox{{el.id}}',
        'name' : 'checkbox'
    }))
    class Meta:
        model = Affairs
        fields = ['done']