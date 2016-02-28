from __future__ import print_function

import argparse
from functools import partial

import serial

try:
    import paho.mqtt.client as paho
    MQTT_CLIENT_CLASS = paho.Client
except ImportError:
    import mosquitto
    MQTT_CLIENT_CLASS = mosquitto.Mosquitto


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


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('port', help='Serial port', default='/dev/ttymxc0')
    parser.add_argument('broker', help='MQTT server', default='localhost')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    port =  args.port
    client = MQTT_CLIENT_CLASS()
    client.connect(args.broker)
    handler = partial(publish_to_mqtt, client)
    read(port, handler)
