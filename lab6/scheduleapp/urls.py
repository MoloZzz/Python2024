from django.urls import path

from scheduleapp import views

urlpatterns = [
    path('schedule/', views.schedule_view, name='schedule'),
    path('add_discipline/', views.add_discipline, name='add_discipline'),
    path('add_schedule/', views.add_schedule, name='add_schedule'),
]
