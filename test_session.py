import subprocess
import time

socat = subprocess.Popen([
    'socat',
    '-d',
    '-d',
    'pty,link=/tmp/a,raw,echo=0',
    'pty,link=/tmp/b,raw,echo=0',
])

fetcher = subprocess.Popen([
    'python',
    'fetch.py',
    '/tmp/a',
])

emulator = subprocess.Popen([
    'python',
    'emulator.py',
    '/tmp/b',
])

time.sleep(0.1)
fetcher.kill()
socat.kill()
