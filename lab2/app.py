from flask import jsonify, request, Flask
from middleware.ErrorHandler import handle_exception
from services.schedule_service import ScheduleService
from dto.discipline import disciplineDTO


app = Flask(__name__)
service = ScheduleService(app)
handle_exception(app)

@app.route('/discipline/<string:day>', methods=['GET'])
def getOneDisciplineByDay(day):
    return service.getManyDisciplineByDay(day)

@app.route('/disciplines', methods=['GET'])
def getAllDisciplines():
    return service.getManyDisciplines()

@app.route('/discipline/<int:id>', methods=['GET'])
def getOneDisciplines(id):
    return service.getOneDisciplineById(id)

@app.route('/discipline/add', methods=['POST'])
def addDiscipline():
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
