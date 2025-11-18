# from pysnmp.hlapi.v1arch import SnmpDispatcher
# from pysnmp.hlapi.v1arch.asyncore import UdpTransportTarget
# from pysnmp.entity.rfc3413.oneliner import cmdgen

# # Create SNMP command generator
# cmdGen = cmdgen.CommandGenerator()

# target = '127.0.0.1'
# community = 'public'

# oid_list = [
#     ('sysDescr', '1.3.6.1.2.1.1.1.0'),
#     ('sysUpTime', '1.3.6.1.2.1.1.3.0'),
#     ('sysName', '1.3.6.1.2.1.1.5.0')
# ]

# print("📡 NMS Monitoring Dashboard")
# print("----------------------------")

# for name, oid in oid_list:
#     errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
#         cmdgen.CommunityData(community),
#         cmdgen.UdpTransportTarget((target, 161)),
#         cmdgen.ObjectType(cmdgen.ObjectIdentity(oid))
#     )

#     if errorIndication:
#         print(f"{name}: Error - {errorIndication}")
#     elif errorStatus:
#         print(f"{name}: Error - {errorStatus.prettyPrint()}")
#     else:
#         for varBind in varBinds:
#             print(f"{name}: {varBind.prettyPrint()}")

from kafka import KafkaProducer
import json
import time

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Simulated network alarms
alarms = [
    {"device": "Router1", "message": "CPU usage is HIGH"},
    {"device": "Switch1", "message": "Interface DOWN"},
    {"device": "Server1", "message": "Disk FULL"}
]

while True:
    for alarm in alarms:
        print(f"Sending alarm: {alarm}")
        producer.send('alarms', alarm)
        producer.flush()
        time.sleep(5)  # send one every 5 seconds
