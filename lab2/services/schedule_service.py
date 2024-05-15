from flask import jsonify
from db.schedule_db import schedule
from db.models import Discipline
from db.connection import connectDatabase

class ScheduleService : 
    def __init__(self):
        self.schedule = schedule
        self.session = connectDatabase()

    def get_schedule(self):
        return schedule

    def get_schedule_day(self, day):
        if day in self.schedule:
            return self.schedule[day]
        else:
            print("День", day, "не знайдено в розкладі.")
            return None


    def add_discipline(self, discipline):

        new_discipline = Discipline(name=discipline.name, professor=discipline.professor, credits=discipline.credits)
        self.session.add(new_discipline)
        self.session.commit()
        self.session.close()
        print(f"Додано нову дисципліну: {discipline.name}, {discipline.professor}, {discipline.credits}")

        return jsonify({
            "name": discipline.name,
            "professor": discipline.professor,
            "credits": discipline.credits
        }), 201