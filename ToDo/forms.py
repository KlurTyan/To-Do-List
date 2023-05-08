from .models import Affairs
from django.forms import ModelForm, TextInput

class AffairsForm(ModelForm):
    class Meta:
        model = Affairs
        fields = ['text']

        widgets = {
            'text': TextInput(attrs={
                'class' : "form-control",
                'placeholder' : "Add new task"
            })
        }