from .models import AppointmentInfo
from django.forms import ModelForm


class AppointmentInfoForm(ModelForm):
    class Meta:
        model = AppointmentInfo
        fields = ['your_name','your_phone','your_email','your_address','your_time','your_date','your_message']
    