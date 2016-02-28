import subprocess
import time

socat = subprocess.Popen([
    'socat',
    '-d',
    '-d',
    'pty,link=/tmp/a,raw,echo=0',
    'pty,link=/tmp/b,raw,echo=0',
])

fetcher = subprocess.Popen(
    [
        'python',
        'fetch.py',
        '/tmp/a',
        'test.mosquitto.org',
    ]
)

# Wait for fetcher
time.sleep(1)

emulator = subprocess.Popen([
    'python',
    'emulator.py',
    '/tmp/b',
])

emulator.wait()
time.sleep(0.2)
fetcher.terminate()
socat.terminate()
