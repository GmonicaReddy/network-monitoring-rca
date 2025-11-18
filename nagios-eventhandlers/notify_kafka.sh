#!/bin/bash
# Event handler for Nagios → Kafka

KAFKA_BROKER="localhost:9092"
TOPIC="alarms"

DEVICE="$1"
SERVICE="$2"
STATE="$3"
MESSAGE="$4"

PAYLOAD="{\"device\":\"$DEVICE\",\"service\":\"$SERVICE\",\"state\":\"$STATE\",\"message\":\"$MESSAGE\"}"

echo "$PAYLOAD" | docker exec -i kafka \
/opt/kafka/bin/kafka-console-producer.sh \
--broker-list $KAFKA_BROKER --topic $TOPIC

