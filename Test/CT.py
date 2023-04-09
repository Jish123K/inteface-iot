import paho.mqtt.client as mqtt

# Define the callback functions for the MQTT client

def on_connect(client, userdata, flags, rc):

    print("Connected with result code " + str(rc))

def on_message(client, userdata, message):

    print("Received message '" + str(message.payload) + "' on topic '" + message.topic + "'")

# Connect to the MQTT broker

client = mqtt.Client()

client.on_connect = on_connect

client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)

# Subscribe to a topic and start the message loop

client.subscribe("test/topic")

client.loop_forever()

