from django.shortcuts import render

# Create your views here.
# advent calendar view function
def calendar_view(request):
    return render(request, 'adventcalendar/calendar.html')