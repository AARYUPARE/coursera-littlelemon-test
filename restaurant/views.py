import json
from datetime import date

from django.db import IntegrityError, transaction
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_http_methods

from .forms import BookingForm
from .models import Booking


@require_GET
def home(request):
    return render(request, 'restaurant/home.html')


@require_http_methods(['GET', 'POST'])
def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
            except IntegrityError:
                form.add_error(None, 'That date and time was just booked. Please choose another slot.')
            else:
                return redirect('book')
    else:
        form = BookingForm(initial={'reservation_date': date.today()})

    return render(request, 'restaurant/book.html', {'form': form, 'today': date.today().isoformat()})


@require_GET
def reservations(request):
    return render(request, 'restaurant/reservations.html')


@require_GET
def bookings_api(request):
    requested_date = request.GET.get('date')
    qs = Booking.objects.all()

    if requested_date:
        try:
            selected = date.fromisoformat(requested_date)
        except ValueError:
            return JsonResponse({'error': 'Invalid date. Use YYYY-MM-DD.'}, status=400)
        qs = qs.filter(reservation_date=selected)

    data = [
        {
            'id': booking.id,
            'first_name': booking.first_name,
            'reservation_date': booking.reservation_date.isoformat(),
            'reservation_slot': booking.reservation_slot,
        }
        for booking in qs
    ]
    return JsonResponse(data, safe=False)
