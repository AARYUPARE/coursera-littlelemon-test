const dateInput = document.getElementById('id_reservation_date');
const slotSelect = document.getElementById('id_reservation_slot');
const bookingList = document.getElementById('booking-list');
const selectedDate = document.getElementById('selected-date');

const initialDate = '{{ today }}';

function loadBookings(dateValue) {
    if (!dateValue) return;
    selectedDate.textContent = dateValue;
    fetch(`/bookings?date=${encodeURIComponent(dateValue)}`)
        .then(response => response.json())
        .then(bookings => {
            const bookedSlots = new Set(bookings.map(b => Number(b.reservation_slot)));
            [...slotSelect.options].forEach(option => {
                if (!option.value) return;
                const booked = bookedSlots.has(Number(option.value));
                option.disabled = booked;
                option.textContent = booked ? `${option.value}:00 - Booked` : `${option.value}:00`;
            });

            if (bookings.length === 0) {
                bookingList.innerHTML = '<p>No Booking</p>';
                return;
            }
            bookingList.innerHTML = bookings
                .map(b => `<p><strong>${escapeHtml(b.first_name)}</strong> - ${b.reservation_slot}:00</p>`)
                .join('');
        })
        .catch(() => {
            bookingList.innerHTML = '<p class="error">Could not load bookings.</p>';
        });
}

function escapeHtml(value) {
    return String(value).replace(/[&<>'"]/g, char => ({
        '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;'
    }[char]));
}

dateInput.addEventListener('change', () => loadBookings(dateInput.value));
loadBookings(dateInput.value || initialDate);
