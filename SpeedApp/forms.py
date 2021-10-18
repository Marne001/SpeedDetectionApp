from django.forms import ModelForm
from .models import SpeedModel
from django import forms

class SpeedModelForm(ModelForm):
    class Meta:
        model = SpeedModel
        fields = ['EngineKW', 'EngineRPM','Horsepower', 'Torque']
        labels = {
        "EngineKW": "Engine kW (At the wheels)(kW)",
        "EngineRPM": "Engine RPM(rpm)",
        "Horsepower": "Horsepower (At the wheels)(hp)",
        "Torque": "Torque(Nm)"
        }
        widgets = {
        'EngineKW': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter engine kilowatts here','rows':5,}),
        'EngineRPM': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter engine RPM here','rows':5,}),
        'Horsepower': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter horsepower here','rows':5,}),
        'Torque': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter torque in NM here','rows':5,}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)