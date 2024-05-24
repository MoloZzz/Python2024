from flask import jsonify, request, Flask
from dto.updateScheduleRecordDTO import ScheduleRecordUpdateDTO
from dto.disciplineUpdateDTO import disciplineUpdateDTO
from middleware.ErrorHandler import handle_exception
from services.schedule_service import ScheduleService
from dto.discipline import disciplineDTO
from dto.scheduleRecordDTO import scheduleRecordDTO

app = Flask(__name__)
service = ScheduleService(app)
handle_exception(app)

@app.route('/disciplines/<int:id>', methods=['GET'])
def get_discipline_by_id(id):
    return service.getOneDisciplineById(id)

@app.route('/disciplines', methods=['GET'])
def get_all_disciplines():
    return service.getManyDisciplines()

@app.route('/schedule', methods=['POST'])
def add_schedule_record():
    try:
        data = request.json
        return service.addScheduleRecord(scheduleRecordDTO(disciplineId=data.get('discipline_id'), dayCode=data.get('day_code'), time=data.get('time')))
    except ValueError as e:
        return jsonify({"error": "Invalid input", "message": str(e)}), 400
    
@app.route('/schedule/<string:day>', methods=['GET'])
def get_disciplines_by_day(day):
    return service.getManyDisciplinesByDay(day)

@app.route('/disciplines/add', methods=['POST'])
def add_discipline():
    try:
        data = request.json
        name, professor, credits = data.get('name'), data.get('professor'), data.get('credits')
        if name and professor and credits:
            course_dto = disciplineDTO(name, professor, credits)
            return service.addDiscipline(course_dto)
        else:
            return jsonify({"error": "Invalid input", "message": "Name, professor, and credits are required."}), 400
    except ValueError as e:
        return jsonify({"error": "Invalid input", "message": str(e)}), 400

@app.route('/disciplines/<int:id>', methods=['DELETE'])
def delete_discipline(id):
    response, status_code = service.deleteDiscipline(id)
    return response, status_code

@app.route('/schedule/<int:id>', methods=['GET'])
def get_shedule_record_by_id(id):
    response, status_code = service.getSheduleRecordById(id)
    return response, status_code

@app.route('/schedule/<int:id>', methods=['DELETE'])
def delete_shedule_record_by_id(id):
    response, status_code = service.deleteScheduleRecordById(id)
    return response, status_code

@app.route('/schedule/day/<string:day>', methods=['DELETE'])
def delete_shedule_records_by_day(day):
    response, status_code = service.deleteScheduleRecordsByDayCode(day)
    return response, status_code

@app.route('/schedule/professor', methods=['DELETE'])
def delete_shedule_records_by_professor():
    response, status_code = service.deleteScheduleRecordsByProfessor(request.json["professor"])
    return response, status_code

@app.route('/disciplines/professor', methods=['DELETE'])
def delete_disciplines_by_professor():
    response, status_code = service.deleteDisciplinesByProfessor(request.json["professor"])
    return response, status_code

@app.route('/schedule/professor', methods=['GET'])
def get_shedule_records_by_professor():
    return service.getSheduleRecordsByProfessor(request.json["professor"])

@app.route('/schedule/<int:id>', methods=['PATCH'])
def update_shedule_record_by_id(id):
    try:
        data = request.json
        return service.updateSheduleRecordById(id, ScheduleRecordUpdateDTO(
            discipline_id = data.get('discipline_id'),
            day_code = data.get('day_code'),
            time = data.get('time')
        ))
    except ValueError as e:
        return jsonify({"error": "Invalid input", "message": str(e)}), 400

@app.route('/disciplines/<int:id>', methods=['PATCH'])
def update_discipline_by_id(id):
    try:
        data = request.json
        return service.updateDisciplineById(id, disciplineUpdateDTO(
            name=data.get('name'),
            professor=data.get('professor'),
            credits=data.get('credits')
        ))
    except ValueError as e:
        return jsonify({"error": "Invalid input", "message": str(e)}), 400
    
if __name__ == '__main__':
    app.run(debug=True, port=9001)


    