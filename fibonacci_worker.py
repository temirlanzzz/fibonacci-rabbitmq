import pika

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_worker(ch, method, properties, body):
    n = int(body)
    result = fibonacci(n)
    print("Числа фиббоначи для {0}: {1}".format(n, result))

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='fibonacci')

channel.basic_publish(exchange='', routing_key='fibonacci', body='10')
channel.basic_publish(exchange='', routing_key='fibonacci', body='100')
channel.basic_publish(exchange='', routing_key='fibonacci', body='56')

channel.basic_consume(queue='fibonacci', on_message_callback=fibonacci_worker, auto_ack=True)

print('Ожидание сообщений...')
channel.start_consuming()
