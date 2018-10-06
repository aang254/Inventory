from django import forms
from .models import gate_pass


class GatepassForm(forms.ModelForm):

    class Meta:
        model = gate_pass
        fields = ('passNo','date','driver_name','Auto_No','lot','Name','commodity','gstin','bill_no','bags','boxes')