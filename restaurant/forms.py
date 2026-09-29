from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'reservation_date', 'reservation_slot']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Your Name', 'required': True}),
            'reservation_date': forms.DateInput(attrs={'type': 'date', 'required': True}),
            'reservation_slot': forms.Select(choices=[(h, f'{h}:00') for h in range(10, 21)], attrs={'required': True}),
        }

    def clean_reservation_slot(self):
        slot = self.cleaned_data['reservation_slot']
        if not 10 <= int(slot) <= 20:
            raise forms.ValidationError('Please choose a valid reservation time.')
        return slot

    def clean(self):
        cleaned = super().clean()
        date = cleaned.get('reservation_date')
        slot = cleaned.get('reservation_slot')
        if date and slot and Booking.objects.filter(reservation_date=date, reservation_slot=slot).exists():
            raise forms.ValidationError('This reservation time is already booked for the selected date.')
        return cleaned
