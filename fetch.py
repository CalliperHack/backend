from __future__ import print_function

import argparse
import re
import time
import uuid

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
    BUTTON = re.compile(r'BTN ([A-Z])')
    MEASUREMENT = re.compile(r'M (\d+)')

    def __init__(self, client):
        self.client = client
        self.last_measurement = 0

    def publish(self, data):
        message = {
            'ts': time.time(),
            'uuid': uuid.uuid4()
        }
        message.update(data)
        print('Publishing', repr(stream))
        self.client.publish(MQTT_TOPIC, message)
    def is_measurement(self, stream):

        match = self.MEASUREMENT.match(stream)
        if not match:
            return None
        else:
            return int(match.group(1))

    def is_button(self, stream):
        match = self.BUTTON.match(stream)
        if not match:
            return None
        else:
            return match.group(1)

    def process_stream(self, stream):
        stream = stream.strip()
        command = self.is_measurement(stream)
        if command:
            self.publish({'measurement': command})


if __name__ == '__main__':
    args = parse_args()
    port = args.port
    client = paho.Client()
    controller = Controller(client)
    client.connect(args.broker)
    read(port, controller.process_stream)
