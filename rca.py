# from kafka import KafkaConsumer
# import pandas as pd

# # Connect to Kafka topic 'alarms'
# consumer = KafkaConsumer(
#     'alarms',
#     bootstrap_servers=['localhost:9092'],
#     auto_offset_reset='earliest'
# )

# # List to store all received alarms
# alarm_list = []

# print("Listening for alarms...")
# for msg in consumer:
#     alarm = msg.value.decode('utf-8')
#     print("Received Alarm:", alarm)
#     alarm_list.append(alarm)

#     # Simple RCA: remove duplicate alarms
#     df = pd.DataFrame(alarm_list, columns=['Alarm'])
#     root_causes = df.drop_duplicates()
#     print("\nRoot Causes:\n", root_causes.to_string(index=False))

from kafka import KafkaConsumer
import json

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    'alarms',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='rca-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Listening for alarms...")

for message in consumer:
    alarm = message.value
    print(f"\nReceived Alarm: ALERT: {alarm['device']} {alarm['message']}")
    
    # Basic RCA suppression logic
    if "Switch1" in alarm['device']:
        print("Root Cause: Switch failure detected → suppressing dependent alerts.\n")
    elif "Router1" in alarm['device']:
        print("Root Cause: Router issue detected.\n")
    elif "Server1" in alarm['device']:
        print("Root Cause: Disk issue detected.\n")
