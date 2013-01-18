#!/usr/bin/env python
from __future__ import print_function

import sys, time, subprocess
import socket
from select import select

class Command(object):
  def __init__(self, command, kill):
    self.command = command
    self.kill = kill

commands = {
  'KEY_BLUE' : Command('steam', '.local/share/Steam/.+/steam'), 
  'KEY_YELLOW': Command('xbmc', 'xbmc.bin'),
}

def connectToLirc():
  s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
  try:
    s.connect('/var/run/lirc/lircd')
  except socket.error:
    s.close()
    return None
  select([], [s], [])
  return s

def killLastProcess():
  global lastProcess, process
  if lastProcess is None:
    return

  print('Killing', lastProcess.command, '[%d]' % process.pid)
  print('Searching for Process to kill:', lastProcess.kill)
  findProc = subprocess.Popen('ps -ef | grep -P "%s" | grep -v grep' % lastProcess.kill, shell = True, stdout = subprocess.PIPE)
  findOut = findProc.communicate()[0]
  if not findOut:
    return

  print('Found proccess to kill:', findOut)
  pid = findOut.split()[1]
  print('Killing pid %s' % pid)
  subprocess.call('kill %s' % pid, shell = True)
  print('Waiting for process death')
  process.wait()
  process = None
  lastProcess = None

lastProcess = None
process = None
lircSocket = None
while True:
  if not lircSocket:
    lircSocket = connectToLirc()
  if not lircSocket:
    lircSocket.close()
    lircSocket = None
    time.sleep(1)
    continue
  
  try:
    readable, writable, exception = select([lircSocket], [], [])
    if lircSocket in readable:
      data = lircSocket.recv(1024)
      if not data:
        break

      data = data.strip().split()
      keyName = data[2]
      print('Received', keyName)
      command = commands.get(keyName)
      if command is lastProcess:
        print('Already running... go away')
        continue

      killLastProcess()

      print('Running', command.command)
      lastProcess = command
      process = subprocess.Popen(command.command, shell = True)
      print('PID = %d' % process.pid)

      lircSocket.close()
      lircSocket = None
  except KeyboardInterrupt:
    break

lircSocket.close()
