import pika


def publish_to_queue(queue_name, rmq_url, message_body, rmq_exchange):
    # Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
    url = 'amqps://fqhfvihc:sw82SbsPeZ3Qq35qRztGQeFRK0xSmELE@puffin.rmq2.cloudamqp.com/fqhfvihc'
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel() # start a channel
    channel.queue_declare(queue=queue_name) # Declare a queue
    channel.basic_publish(exchange=rmq_exchange,
                        routing_key=queue_name,
                        body=message_body)

    print(" [x] Sent ", message_body)
    connection.close()