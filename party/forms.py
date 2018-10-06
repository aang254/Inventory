from django import forms
from .models import party_Ledger

class partyForm(forms.ModelForm):

    class Meta:
        model = party_Ledger
        fields = ('Name','Address','gstin','Contact')
