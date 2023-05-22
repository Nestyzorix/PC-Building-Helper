from django import forms
from .models import *


class ConfigureForm(forms.Form):

    processor = forms.ModelChoiceField(queryset=Processor.objects.all())
    cooling_system = forms.ModelChoiceField(queryset=CoolingSystem.objects.all())
    motherboard = forms.ModelChoiceField(queryset=Motherboard.objects.all())
    ram = forms.ModelChoiceField(queryset=RAM.objects.all())
    videocard = forms.ModelChoiceField(queryset=Videocard.objects.all())
    hdd = forms.ModelChoiceField(queryset=HDD.objects.all())
    ssd = forms.ModelChoiceField(queryset=SSD.objects.all())
    power_unit = forms.ModelChoiceField(queryset=PowerUnit.objects.all())

    # processor = forms.ModelChoiceField()
    #
    # def __init__(self, *args, **kwargs):
    #     super(ConfigureProcessorForm, self).__init__(*args, **kwargs)
    #
    #     for item in Processor.objects.all():
    #         self.fields['processor'].choices.append((item.id, item.name))



