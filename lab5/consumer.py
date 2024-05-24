import pika
import json
from services.schedule_service import ScheduleService
from dto.scheduleRecordDTO import scheduleRecordDTO
from dto.updateScheduleRecordDTO import ScheduleRecordUpdateDTO
from dto.discipline import disciplineDTO
from dto.disciplineUpdateDTO import disciplineUpdateDTO
from app import app

def callback(ch, method, properties, body):
    data = json.loads(body)
    service = ScheduleService(app) 
    
    if method.routing_key == 'add_schedule':
        service.addScheduleRecord(scheduleRecordDTO(**data))
    elif method.routing_key == 'update_schedule':
        service.updateSheduleRecordById(data['id'], ScheduleRecordUpdateDTO(**data['payload']))
    elif method.routing_key == 'add_discipline':
        service.addDiscipline(disciplineDTO(**data))
    elif method.routing_key == 'update_discipline':
        service.updateDisciplineById(data['id'], disciplineUpdateDTO(**data['payload']))

    ch.basic_ack(delivery_tag=method.delivery_tag)

def consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    binding_keys = ['add_schedule', 'update_schedule', 'add_discipline', 'update_discipline']

    for binding_key in binding_keys:
        channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=binding_key)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    channel.start_consuming()

if __name__ == '__main__':
    consume()
