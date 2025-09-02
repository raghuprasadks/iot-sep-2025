import paho.mqtt.client as mqtt

# Define the on_message callback
def on_message(client, userdata, message):
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}' with QoS {message.qos}")

# Create an MQTT client instance
client = mqtt.Client()

# Assign the on_message callback
client.on_message = on_message

# Connect to the MQTT broker
#client.connect("broker.hivemq.com", 1883, 60)

client.connect("localhost", 1883, 60)
# Subscribe to a topic
client.subscribe("test/topic")

# Start the loop to process received messages
client.loop_start()

# Keep the script running
import time
while True:
    time.sleep(1)