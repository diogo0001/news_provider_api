from django import forms
from .models import Author
  
class HotelForm(forms.ModelForm):
  
    class Meta:
        model = Author
        fields = ['name', 'photo']