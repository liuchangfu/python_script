import pika
conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = conn.channel()

channel.queue_declare(queue='Hello')

channel.basic_publish(
    exchange = '',
    routing_key ='hello',
    body ='Hello World!'
)
print("[x] Sent 'Hello World!'")
conn.close()
