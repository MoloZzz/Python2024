from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import Schedule, Discipline, DictionaryScheduleDay


def schedule_view(request):
    days_of_week = DictionaryScheduleDay.objects.filter(code__in=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
    schedules = Schedule.objects.all().select_related('discipline', 'day')
    time_slots = ["8:40 - 10:10", "10:35 - 12:05", "12:20 - 14:05", "14:20 - 16:00", "16:10 - 18:00"]
    return render(request, 'schedule.html', {
        'days_of_week': days_of_week,
        'schedules': schedules,
        'time_slots': time_slots,
        'disciplines': Discipline.objects.all()
    })


def add_discipline(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        professor = request.POST.get('professor')
        credits = request.POST.get('credits')
        try:
            Discipline.objects.create(name=name, professor=professor, credits=credits)
            return redirect('schedule')
        except IntegrityError as e:
            print(str(e))
            return render(request, 'schedule.html', {
                'error_message': "Дисципліна з таким ім'ям та викладачем вже існує",
                'disciplines': Discipline.objects.all()  # Передача дисциплін у контекст
            })
    return render(request, 'schedule.html', {
        'disciplines': Discipline.objects.all()  # Передача дисциплін у контекст
    })


def add_schedule(request):
    if request.method == 'POST':
        discipline_id = request.POST.get('discipline')
        time = request.POST.get('time')
        day_code = request.POST.get('day')
        try:
            day_obj = DictionaryScheduleDay.objects.get(code=day_code)
            discipline = Discipline.objects.get(pk=discipline_id)
            Schedule.objects.create(discipline=discipline, day=day_obj, time=time)
            return redirect('schedule')
        except IntegrityError as e:
            print(str(e))
            return render(request, 'schedule.html', {
                'error_message': 'Ця дисципліна вже додана до цього дня та часу.',
                'disciplines': Discipline.objects.all(),
                'schedules': Schedule.objects.all(),
                'days_of_week': DictionaryScheduleDay.objects.all(),
                'time_slots': ["8:40 - 10:10", "10:35 - 12:05", "12:20 - 14:05", "14:20 - 16:00", "16:10 - 18:00"]
            })
    return render(request, 'schedule.html', {
        'disciplines': Discipline.objects.all(),
        'schedules': Schedule.objects.all(),
        'days_of_week': DictionaryScheduleDay.objects.all(),
        'time_slots': ["8:40 - 10:10", "10:35 - 12:05", "12:20 - 14:05", "14:20 - 16:00", "16:10 - 18:00"]
    })


def your_view(request):
    schedules = Schedule.objects.all()
    days_of_week = DictionaryScheduleDay.objects.all()
    disciplines = Discipline.objects.all()
    return render(request, 'schedule.html', {'schedules': schedules, 'days_of_week': days_of_week, 'disciplines': disciplines})
