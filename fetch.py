from __future__ import print_function

import argparse

import paho.mqtt.client as paho
import serial


MQTT_TOPIC = 'CallibreHack'


def process_stream(stream):
    print('Received', repr(stream))


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
    parser.add_argument('broker', help='MQTT server', nargs='?', default='localhost')
    return parser.parse_args()


class Controller:
    def __init__(self, client):
        self.client = client
        self.last_measurement = 0

    def process_stream(self, stream):
        print('Publishing', repr(stream))
        self.client.publish(MQTT_TOPIC, 42)


if __name__ == '__main__':
    args = parse_args()
    port = args.port
    client = paho.Client()
    controller = Controller(client)
    client.connect(args.broker)
    read(port, controller.process_stream)
