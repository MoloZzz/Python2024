from flask import jsonify, request, Flask
from services.schedule_service import ScheduleService
from dto.discipline import disciplineDTO


app = Flask(__name__)
service = ScheduleService()


@app.route('/schedule/<string:day>', methods=['GET'])
def get_course_controller(day):
    return jsonify(service.get_schedule_day(day))

@app.route('/add-course', methods=['POST'])
def add_discipline_controller():
    data = request.json
    course_dto = disciplineDTO(data.get('name'), data.get('professor'), data.get('credits'))
    return service.add_discipline(course_dto)

if __name__ == '__main__':
    app.run(debug=True, port=9001)
