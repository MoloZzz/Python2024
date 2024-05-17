class ScheduleRecordUpdateDTO:
    def __init__(self, discipline_id=None, day_code=None, time=None):
        self.discipline_id = discipline_id
        self.day_code = day_code
        self.time = time