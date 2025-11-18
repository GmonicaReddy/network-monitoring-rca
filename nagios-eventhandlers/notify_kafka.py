#!/usr/bin/env python3
# notify_kafka.py
# Usage: notify_kafka.py "<HOSTNAME>" "<SERVICE_DESC>" "<SERVICESTATE>" "<SERVICEOUTPUT>"

import sys, json
from kafka import KafkaProducer

# Kafka broker from host perspective (Docker Desktop): use host.docker.internal and the external port you exposed
KAFKA_BOOTSTRAP = "host.docker.internal:29092"  # use 29092 if you used that earlier

def main(args):
    if len(args) < 5:
        print("Usage: notify_kafka.py HOST SERVICE STATE OUTPUT")
        return
    host = args[1]
    service = args[2]
    state = args[3]
    output = args[4]

    payload = {
        "device": host,
        "service": service,
        "state": state,
        "message": output
    }

    producer = KafkaProducer(
        bootstrap_servers=[KAFKA_BOOTSTRAP],
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

    producer.send("alarms", payload)
    producer.flush()
    print("Sent to Kafka:", payload)

if __name__ == "__main__":
    main(sys.argv)

