from flask import jsonify
from sqlalchemy.exc import IntegrityError
from db.schedule_db import schedule
from db.models import Discipline, Schedule
from db.connection import connectDatabase
from middleware.ErrorHandler import handle_exception

class ScheduleService : 
    def __init__(self,app):
        self.schedule = schedule
        self.session = connectDatabase()
        self.app = app
        handle_exception(self.app)

    def getOneDisciplineById(self,id):
        try:
            discipline = self.session.query(Discipline).filter_by(id=id).first()  
            if discipline:  
                return jsonify({
                    "id": discipline.id,
                    "name": discipline.name,
                    "professor": discipline.professor,
                    "credits": discipline.credits
                }), 200  
            else:
                return jsonify({"error": "Discipline not found"}), 404 
        except Exception as e:
            return jsonify({"error": "Internal server error", "message": str(e)}), 500

    def getManyDisciplineByDay(self, day):
        try:
            scheduleRecords = self.session.query(Schedule).filter_by(day_code=day).all()  
            if scheduleRecords:
                scheduleRecordsList = [{
                    "id": scheduleRecord.id,
                    "discipline_id": scheduleRecord.discipline_id,
                    "day_code": scheduleRecord.day_code,
                    "time": scheduleRecord.time
                } for scheduleRecord in scheduleRecords]  
                return scheduleRecordsList, 200 
            else:
                return jsonify({"error": "Discipline not found"}), 404 
        except Exception as e:
            return jsonify({"error": "Internal server error", "message": str(e)}), 500
    
    def getManyDisciplines(self):
        try:
            disciplines = self.session.query(Discipline).all()
            disciplines_list = [{
                "id": discipline.id,
                "name": discipline.name,
                "professor": discipline.professor,
                "credits": discipline.credits
            } for discipline in disciplines]
            return jsonify(disciplines_list), 200
        except Exception as e:
            return jsonify({"error": "Internal server error", "message": str(e)}), 500


    def addDiscipline(self, discipline):
        try:
            new_discipline = Discipline(name=discipline.name, professor=discipline.professor, credits=discipline.credits)
            self.session.add(new_discipline)
            self.session.commit()
            self.session.refresh(new_discipline)  # можна прибрати, якщко потрібно оптимізувати
            self.session.close()

            return jsonify({
                "id": new_discipline.id,
                "name": new_discipline.name,
                "professor": new_discipline.professor,
                "credits": new_discipline.credits
            }), 201
        except IntegrityError as e:
            self.session.rollback() 
            return jsonify({"error": "Database error", "message": str(e)}), 500
        except Exception as e:
            return jsonify({"error": "Internal server error", "message": str(e)}), 500