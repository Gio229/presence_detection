import json
from kafka import KafkaProducer
from config import KAFKA_BROKER, KAFKA_CLASS_DETECTION_STREAM_TOPIC

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    retries=0,
    acks='all',
)


def publish_presence(presence: bool, people_count: int):
    from datetime import datetime
    message = {
        "timestamp": datetime.now().isoformat() + "Z",
        "presence": presence,
        "peopleCount": people_count
    }
 
    producer.send(KAFKA_CLASS_DETECTION_STREAM_TOPIC, value=message)
    producer.flush()
    print("[Kafka] Published:", message)
