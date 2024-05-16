from flask import jsonify, request, Flask
from middleware.ErrorHandler import handle_exception
from services.schedule_service import ScheduleService
from dto.discipline import disciplineDTO
from dto.scheduleRecordDTO import scheduleRecordDTO

app = Flask(__name__)
service = ScheduleService(app)
handle_exception(app)

@app.route('/disciplines/<int:id>', methods=['GET'])
def getOneDisciplineById(id):
    return service.getOneDisciplineById(id)

@app.route('/disciplines', methods=['GET'])
def getAllDisciplines():
    return service.getManyDisciplines()

@app.route('/schedule/add', methods=['POST'])
def newScheduleRecord():
    try:
        data = request.json
        discipline_id = data.get('discipline_id')
        day_code = data.get('day_code')
        time = data.get('time')

        scheduleRecord_dto = scheduleRecordDTO(disciplineId=discipline_id, dayCode=day_code, time=time)
        
        return service.addScheduleRecord(scheduleRecord_dto)
    except ValueError as e:
        return jsonify({"error": "Invalid input", "message": str(e)}), 400
    
@app.route('/schedule/<string:day>', methods=['GET'])
def getAllDisciplineByDay(day):
    return service.getManyDisciplineByDay(day)

@app.route('/disciplines/add', methods=['POST'])
def newDisciplineRecord():
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

if __name__ == '__main__':
    app.run(debug=True, port=9001)
