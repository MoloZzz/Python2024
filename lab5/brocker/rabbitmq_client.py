import pika
import json

class RabbitMQClient:
    def __init__(self, queue):
        self.queue = queue
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue, durable=True)

    def send_message(self, message):
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue,
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=2,  
            )
        )

    def close_connection(self):
        self.connection.close()
