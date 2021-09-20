"""Socialmediagram views."""

# Django
from django.http import HttpResponse
from django.shortcuts  import render

# Utilities
from datetime import datetime
import json

# Forms
from users.forms import ProfileSerch

# Models
from users.models import Profile


def atletico_nacional(request):
    """Return a greeting."""
    return HttpResponse('El Verde! El más grande de colombia!. Hora del servidor donde corre la app {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def sort_integers(request):
    """Return a JSON response with sorted integers."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )


def say_hi(request, name, equipo):
    """Return a greeting."""
    if str(equipo).lower() != 'nacional':
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to socialmediagram'.format(name)
    return HttpResponse(message)


