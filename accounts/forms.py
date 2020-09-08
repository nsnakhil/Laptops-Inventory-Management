from django import forms
from .models import Laptops

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptops
        fields = ('make',
            'model',
            'processor',
            'CPU',
            'Speed',
            'Gen',
            'RAM',
            'Harddrive',
            'Camera',
            'Battery',
            'serial_number',
            'customer',
            'comments',
            'condition',
            'vendor',
            'status')