from django import forms

from .models import Emergency,Alert

class EmergencyModelForm(forms.ModleForm):
    class Meta:
        model=Emergency
        fields=["admin","name","phone"]


class AlertModelForm(forms.ModleForm):
    class Meta:
        model=Alert
        fields=["admin","location"]


