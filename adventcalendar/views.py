from django.shortcuts import render
from .models import AdventDay
# Create your views here.
# advent calendar view function
def calendar_view(request):

    try:
        advent_day = AdventDay.objects.filter(user=request.user)
    except:
        return render(request, 'adventcalendar/calendar.html')
    return render(request, 'adventcalendar/calendar.html', {'advent_day': advent_day})