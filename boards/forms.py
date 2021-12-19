from django import forms
from .models import Saint

class NewSaintForm(forms.ModelForm):
    class Meta:
        model = Saint
        fields = '__all__'