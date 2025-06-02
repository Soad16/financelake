from kafka import KafkaProducer
import json
import time
import logging

logging.basicConfig(
    filename="../logs/finance_ingestion.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    try:
        data = {"symbol": "AAPL", "price": 187.21, "timestamp": time.time()}
        producer.send("finance-topic", value=data)
        producer.flush()
        logging.info(f"Sent data to finance-topic: {data}")
        time.sleep(5)
    except Exception as e:
        logging.error(f"Failed to send data: {e}")
        time.sleep(5)
