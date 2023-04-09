import paho.mqtt.client as mqtt

import json

class Sensor:

    def __init__(self, id, name, description, dataType, unit, accuracy, dateCreated, apiKey):

        self.id = id

        self.name = name

        self.description = description

        self.dataType = dataType

        self.unit = unit

        self.accuracy = accuracy

        self.dateCreated = dateCreated

        self.apiKey = apiKey

        self.client = mqtt.Client()

        self.client.on_connect = self.on_connect

        self.client.on_message = self.on_message

        self.client.connect("iot.eclipse.org", 1883, 60)

        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):

        print("Connected with result code " + str(rc))

        topic = "sensors/{}/data".format(self.id)

        self.client.subscribe(topic)

    def on_message(self, client, userdata, message):

        data = json.loads(message.payload.decode())

        if data["name"] == "getName":

            self.client.publish("sensors/{}/data".format(self.id), json.dumps({"name": self.name}))

    def getName(self):

        self.client.publish("sensors/{}/data".format(self.id), json.dumps({"name": "getName"}))

        return self.name

def test_get_name():

    sensor = Sensor("1234", "myname", "", "Input", "Watts", 102, "2021-01-01", "deadbeef")

    assert sensor.getName() == "myname"

