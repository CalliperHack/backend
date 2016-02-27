# CallibreHack backend

## Testing

We need three open terminals:

On the first one, create virtual connection:

```
$ socat -d -d pty,link=/tmp/a,raw,echo=0 pty,link=/tmp/b,raw,echo=0
```

On the second one, launch the fetcher:

```
$ python fetch.py /tmp/a
```

Finally launch the emulator:

```
$ python emulator.py /tmp/b
```


## Testing prerequisites

```
$ sudo apt-get install socat
$ virtualenv -ppython2.7 .venv
$ pip install -r requirements.txt
```


## License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
