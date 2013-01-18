#!/usr/bin/env python
from __future__ import print_function

import sys, time, subprocess
import socket
from select import select

while True:
  s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
  try:
    s.connect('/var/run/lirc/lircd')
  except socket.error:
    s.close()
    time.sleep(1)
    continue
  select([], [s], [])

  try:
    readable, writable, exception = select([s], [], [])
    if s in readable:
      data = s.recv(1024)
      if not data:
        break
      data = data.strip().split()
      keyName = data[2]
      if keyName == 'KEY_BLUE':
        s.close()
        subprocess.call('steam', shell = True)
      elif keyName == 'KEY_YELLOW':
        s.close()
        subprocess.call('xbmc', shell = True)
  except KeyboardInterrupt:
    break
  finally:
    s.close()

