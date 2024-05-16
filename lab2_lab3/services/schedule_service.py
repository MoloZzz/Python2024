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

    def getOneDisciplineById(self, id, jsonify_result=True):
        try:
            discipline = self.session.query(Discipline).filter_by(id=id).first()  
            if discipline:
                result = {
                    "id": discipline.id,
                    "name": discipline.name,
                    "professor": discipline.professor,
                    "credits": discipline.credits
                }
                if jsonify_result:
                    return jsonify(result), 200
                else:
                    return result
            else:
                return jsonify({"error": "Discipline not found"}), 404 if jsonify_result else None
        except Exception as e:
            return jsonify({"error": "Internal server error", "message": str(e)}), 500 if jsonify_result else None

    def getManyDisciplinesByDay(self, day):
        try:
            scheduleRecords = self.session.query(Schedule).filter_by(day_code=day).all()  
            if scheduleRecords:
                scheduleRecordsList = [{
                    "id": scheduleRecord.id,
                    "discipline": self.getOneDisciplineById(scheduleRecord.discipline_id,False)["name"],
                    "professor": self.getOneDisciplineById(scheduleRecord.discipline_id,False)["professor"],
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
    
    def addScheduleRecord(self, record):
        try:
            newRecord = Schedule(discipline_id=record.discipline_id, day_code=record.day_code, time=record.time)
            self.session.add(newRecord)
            self.session.commit()
            self.session.refresh(newRecord)
            self.session.close()

            return jsonify({
                "id": newRecord.id,
                "discipline_id": newRecord.discipline_id,
                "day_code": newRecord.day_code,
                "time": newRecord.time
            }), 201
        except IntegrityError as e:
            self.session.rollback() 
            return jsonify({"error": "Database error", "message": str(e)}), 500
        except Exception as e:
            return jsonify({"error": "Internal server error", "message": str(e)}), 500
    
    def deleteDiscipline(self,id):
        try:
            discipline = self.session.query(Discipline).filter_by(id=id).first()
            if discipline:
                self.session.delete(discipline)
                self.session.commit()
                self.session.close()
                return jsonify({"message": "Discipline deleted successfully"}), 200
            else:
                return jsonify({"error": "Discipline not found"}), 404
        except IntegrityError as e:
            self.session.rollback() 
            return jsonify({"error": "Database error", "message": str(e)}), 500
        except Exception as e:
            return jsonify({"error": "Internal server error", "message": str(e)}), 500 
    
    def deleteScheduleRecordById(self,id):
        try:
            schedule = self.session.query(Schedule).filter_by(id=id).first()
            if schedule:
                self.session.delete(schedule)
                self.session.commit()
                self.session.close()
                return jsonify({"message": "Schedule record deleted successfully"}), 200
            else:
                return jsonify({"error": "Schedule record not found"}), 404
        except IntegrityError as e:
            self.session.rollback() 
            return jsonify({"error": "Database error", "message": str(e)}), 500
        except Exception as e:
            return jsonify({"error": "Internal server error", "message": str(e)}), 500

    def deleteScheduleRecordsByDayCode(self, day_code):
        try:
            schedules = self.session.query(Schedule).filter_by(day_code=day_code).all()
            
            if schedules:
                deleted_count = 0
                for schedule in schedules:
                    self.session.delete(schedule)
                    deleted_count += 1
                self.session.commit()
                self.session.close()
                return jsonify({
                    "message": f"All {deleted_count} schedule records with day_code {day_code} deleted successfully",
                    "deleted_count": deleted_count
                }), 200
            else:
                return jsonify({"error": f"No schedule records found with day_code {day_code}"}), 404
        except IntegrityError as e:
            self.session.rollback() 
            return jsonify({"error": "Database error", "message": str(e)}), 500
        except Exception as e:
            return jsonify({"error": "Internal server error", "message": str(e)}), 500
    
    def deleteDisciplinesByProfessor(self, professor):
        try:  
            disciplines = self.session.query(Discipline).filter_by(professor=professor).all()
            if disciplines:
                deletedCount = 0
                for discipline in disciplines:
                    self.session.delete(discipline)
                    deletedCount += 1
                self.session.commit()
                self.session.close()
                return jsonify({
                    "message": f"All {deletedCount} disciplines and records in schedule, taught by professor {professor} deleted successfully",
                    "deleted_count": deletedCount 
                }), 200
            else:
                return jsonify({"error": f"No disciplines found taught by professor {professor}"}), 404
        except IntegrityError as e:
            self.session.rollback() 
            return jsonify({"error": "Database error", "message": str(e)}), 500
        except Exception as e:
            return jsonify({"error": "Internal server error", "message": str(e)}), 500

    def deleteScheduleRecordsByProfessor(self, professor):
        try:
            disciplines = self.session.query(Discipline).filter_by(professor=professor).all()
            if disciplines:
                deleted_count = 0
                for discipline in disciplines:
                    schedule_records = self.session.query(Schedule).filter_by(discipline_id=discipline.id).all()
                    for record in schedule_records:
                        self.session.delete(record)
                        deleted_count += 1
                self.session.commit()
                self.session.close()
                return jsonify({
                    "message": f"All {deleted_count} schedule records for professor {professor} deleted successfully",
                    "deleted_count": deleted_count
                }), 200
            else:
                return jsonify({"error": f"No disciplines found taught by professor {professor}"}), 404
        except IntegrityError as e:
            self.session.rollback() 
            return jsonify({"error": "Database error", "message": str(e)}), 500
        except Exception as e:
            return jsonify({"error": "Internal server error", "message": str(e)}), 500

    def getSheduleRecordsByProfessor(self, professor):
        try:
            schedule_records = self.session.query(Schedule).join(Discipline).filter(Discipline.professor == professor).all()
            if schedule_records:
                schedule_records_list = []
                for record in schedule_records:
                    discipline_name = self.session.query(Discipline.name).filter_by(id=record.discipline_id).scalar()
                    schedule_records_list.append({
                        "discipline": discipline_name,
                        "day": record.day_code,
                        "time": record.time
                    })
                return jsonify(schedule_records_list), 200
            else:
                return jsonify({"error": f"No schedule records found for professor {professor}"}), 404
        except Exception as e:
            return jsonify({"error": "Internal server error", "message": str(e)}), 500
