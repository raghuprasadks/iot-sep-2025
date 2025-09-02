import paho.mqtt.client as mqtt
import time

# Define the callback functions
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
        #client.subscribe("test/topic")
    else:
        print(f"Connect failed with result code {rc}")

def on_message(client, userdata, msg):
    print(f"Message received: {msg.topic} {msg.payload.decode()}")

# Create an MQTT client instance
client = mqtt.Client()

# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect("localhost", 1883, 60)
#client.connect("broker.hivemq.com", 1883, 60)

# Start the loop to process network traffic and dispatch callbacks
client.loop_start()

# Publish a message to the topic
client.publish("test/topic", "message_payload")

# Add a delay to give the client time to receive the message
time.sleep(2)

# Stop the loop and disconnect
client.loop_stop()
client.disconnect()