from flask import jsonify, request, Flask
from services.schedule_service import ScheduleService
from db.connection import engine, Session
app = Flask(__name__)
service = ScheduleService()

@app.route('/hello', methods=['GET'])
def get_hello_controller():
    print("hello")
    return jsonify('hello')

@app.route('/schedule', methods=['GET'])
def get_schedule_controller():
    return jsonify(service.get_schedule())

@app.route('/schedule/<string:day>', methods=['GET'])
def get_course_controller(day):
    return jsonify(service.get_schedule_day(day))

@app.route('/schedule', methods=['POST'])
def add_course_controller():
    return service.add_course(request)

if __name__ == '__main__':
    app.run(debug=True, port=9001)
