import asyncio

from confluent_kafka import Consumer

TOPIC_NAME="crime.broker1"

async def consume_configured_topic():
    consumer = Consumer({
        'bootstrap.servers': 'PLAINTEXT://localhost:9093',
        'group.id': 'group1',
    })
    
    consumer.subscribe([TOPIC_NAME])
    
    while True:
        messages = consumer.consume()
        
        for message in messages:
            if message is None:
                print('Message empty')
            else:
                print(f'{message.value()}')
                
        await asyncio.sleep(1.0)
                
def run_consumer():
    asyncio.run(consume_configured_topic())
        
if __name__ == '__main__':
    run_consumer()