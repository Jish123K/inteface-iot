import paho.mqtt.client as mqtt

import json

class IotInterface:

    def __init__(self, host, port):

        self.host = host

        self.port = port

        self.client = mqtt.Client()

        self.client.connect(host, port=port)

        

    def get_sensor_data(self, sensor_id):

        topic = f"iot/{sensor_id}/data"

        self.client.subscribe(topic)

        

        # Wait for data to arrive

        def on_message(client, userdata, message):

            self.data = json.loads(message.payload)

        self.client.on_message = on_message

        self.client.loop(timeout=10)

        

        return self.data

