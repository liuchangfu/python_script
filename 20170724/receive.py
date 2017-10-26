import pika

conn = pika.BlockingConnection(pika.ConnectionParameters
                               ('localhost'))

channel = conn.channel()

channel.queue_declare(queue='hello')

def callbakc(ch,method,properties,body):
    print(" [x] Received %r" % body)

channel.basic_consume(callbakc,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()