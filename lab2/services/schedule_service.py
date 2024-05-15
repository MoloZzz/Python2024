from flask import jsonify
from db.schedule_db import schedule

class ScheduleService : 
    def __init__(self):
        self.schedule = schedule

    def get_schedule(self):
        return schedule

    def get_schedule_day(self, day):
        if day in self.schedule:
            return self.schedule[day]
        else:
            print("День", day, "не знайдено в розкладі.")
            return None


    def add_course(self,request):
        data = request.get_json()
        new_course = {"id": len(schedule) + 1, "course": data["course"], "professor": data["professor"]}
        schedule.append(new_course)
        return jsonify(new_course), 201