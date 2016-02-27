from __future__ import print_function

import serial


def write(stream):
    port = '/tmp/b'
    conf = dict(port=port, baudrate=115200, timeout=0, rtscts=True, dsrdtr=True)
    print('Connecting', port)
    with serial.Serial(**conf) as ser:
        print('Sending', repr(stream))
        ser.write(stream)


if __name__ == '__main__':
    write('M1\n')
