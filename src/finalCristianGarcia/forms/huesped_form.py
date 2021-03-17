from django import forms
from finalCristianGarcia.models import Huesped



class HuespedForm(forms.ModelForm):

    class Meta:
        model = Huesped
        fields = "__all__"
        
        
