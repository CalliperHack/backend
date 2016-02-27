from __future__ import print_function

import sys

import serial


def process_stream(stream):
    print('Received ', repr(stream))


def read(port, handler):
    conf = dict(port=port, baudrate=115200, timeout=0, rtscts=True, dsrdtr=True)
    print('Connecting ', port)
    with serial.Serial(**conf) as ser:
        while True:
            received = ser.read(1024)
            if received:
                handler(received)


if __name__ == '__main__':
    port =  sys.argv[1]  # /dev/ttymxc0
    read(port, process_stream)
