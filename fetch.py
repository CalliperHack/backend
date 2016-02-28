from __future__ import print_function

from functools import partial

import sys

import serial

try:
    import paho.mqtt.client as paho
    MQTT_CLIENT_CLASS = paho.Client
except ImportError:
    import mosquitto
    MQTT_CLIENT_CLASS = mosquitto.Mosquitto


MQTT_SERVER = 'test.mosquitto.org'
MQTT_TOPIC = 'CallibreHack'


def process_stream(stream):
    print('Received', repr(stream))


def publish_to_mqtt(client, stream):
    print('Publishing', repr(stream))
    client.publish(MQTT_TOPIC, 42)


def read(port, handler):
    conf = dict(port=port, baudrate=115200, timeout=0, rtscts=True, dsrdtr=True)
    print('Connecting', port)
    with serial.Serial(**conf) as ser:
        while True:
            received = ser.read(1024)
            if received:
                handler(received)


if __name__ == '__main__':
    port =  sys.argv[1]  # /dev/ttymxc0
    client = MQTT_CLIENT_CLASS()
    client.connect(MQTT_SERVER)
    handler = partial(publish_to_mqtt, client)
    read(port, handler)
