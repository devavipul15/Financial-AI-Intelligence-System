from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

transaction = {
    "customer_id": 1001,
    "amount": 1200,
    "location": "Texas"
}

producer.send("transactions", transaction)

producer.flush()