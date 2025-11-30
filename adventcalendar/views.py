from django.shortcuts import render
from datetime import datetime

# Create your views here.
# advent calendar view function
def calendar_view(request):
    days = range(1, 25)  # creates a list from 1 to 24
    today = datetime.now().day  # gets the current day of the month
    return render(request, 'adventcalendar/calendar.html', {'days': days})
