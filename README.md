# Little Lemon Django Booking App

Project directory: `littlelemon`
App: `restaurant`
Database: MySQL
Frontend form behavior: JavaScript Fetch API

## Setup

```bash
cd littlelemon
pipenv install
pipenv shell
```

Create a MySQL database named `littlelemon`, then set the MySQL environment variables described in `notes.txt`.

Run:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Main pages

- `/` - Home
- `/book/` - Booking form
- `/reservations/` - All reservations as JSON displayed in the browser
- `/bookings?date=YYYY-MM-DD` - JSON API for bookings on a specific date
- `/admin/` - Django admin

## Features

- Booking form with first name, reservation date, and reservation slot.
- Native HTML date selector.
- Current date is selected automatically.
- Existing reservations are fetched with JavaScript Fetch API.
- Booked time slots are disabled for the selected date.
- Changing the date refreshes the booking list and available slots.
- Duplicate date/time bookings are prevented both in the form validation and database constraint.
- Reservations are available as JSON.
- Date-specific JSON API is supported.
- Displays `No Booking` when a selected date has no reservations.
