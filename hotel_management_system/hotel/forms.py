from django import forms
from .models import Guest, Reservation, Feedback

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['guest', 'room', 'check_in_date', 'check_out_date']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['guest', 'reservation', 'feedback']