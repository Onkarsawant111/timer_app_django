from django.shortcuts import render
import datetime

# Create your views here.
def greet(request):
    current_time = datetime.datetime.now().time()
    
    morning_start = datetime.time(6, 0)
    morning_end = datetime.time(11, 59, 59)
    afternoon_start = datetime.time(12, 0)
    afternoon_end = datetime.time(17, 59, 59)
    evening_start = datetime.time(18, 0)
    evening_end = datetime.time(23, 59, 59)

    if morning_start <= current_time <= morning_end:
        greeting = "Good morning."
    elif afternoon_start <= current_time <= afternoon_end:
        greeting = "Good afternoon."
    elif evening_start <= current_time <= evening_end:
        greeting = "Good evening."
    else:
        greeting = "Good night." 

    return render(request, 'greet.html', {'greeting': greeting})