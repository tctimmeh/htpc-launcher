#!/usr/bin/env python
from __future__ import print_function

import sys, time, subprocess
import socket
from select import select

class Command(object):
  def __init__(self, command, kill):
    self.command = command
    self.kill = kill

  def __str__(self):
    return self.command

class Process(object):
  def __init__(self, command):
    self.command = command
    self.proc = None

  def start(self):
    print('Running', self.command)
    self.proc = subprocess.Popen(self.command.command, shell = True)
    print('PID = %d' % self.proc.pid)

  def stop(self):
    if not self.proc:
      return

    print('Killing', self.command, '[%d]' % self.proc.pid)
    print('Searching for Process to kill:', self.command.kill)
    findProc = subprocess.Popen('ps -ef | grep -P "%s" | grep -v grep' % self.command.kill, shell = True, stdout = subprocess.PIPE)
    findOut = findProc.communicate()[0]
    if not findOut:
      return

    print('Found proccess to kill:', findOut)
    pid = findOut.split()[1]
    print('Killing pid %s' % pid)
    subprocess.call('kill %s' % pid, shell = True)
    print('Waiting for process death')
    self.proc.wait()

class IrSwitchApp(object):
  def __init__(self):
    self.lircSocket = None
    self.currentProcess = None

    self.commands = {
      'KEY_BLUE' : Command('steam', '.local/share/Steam/.+/steam'), 
      'KEY_YELLOW': Command('xbmc', 'xbmc.bin'),
    }

  def run(self):
    while True:
      if not self.lircSocket:
        self.lircSocket = self.connectToLirc()
      if not self.lircSocket:
        self.lircSocket.close()
        self.lircSocket = None
        time.sleep(1)
        continue
      
      try:
        readable, writable, exception = select([self.lircSocket], [], [])
        if self.lircSocket in readable:
          data = self.lircSocket.recv(1024)
          if not data:
            break

          data = data.strip().split()
          keyName = data[2]
          print('Received', keyName)
          command = self.commands.get(keyName)
          if (self.currentProcess) and (command is self.currentProcess.command):
            print('Already running... go away')
            continue

          if self.currentProcess:
            self.currentProcess.stop()
            self.currentProcess = None

          self.currentProcess = Process(command)
          self.currentProcess.start()

          self.lircSocket.close()
          self.lircSocket = None
      except KeyboardInterrupt:
        break

    self.lircSocket.close()

  def connectToLirc(self):
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
      s.connect('/var/run/lirc/lircd')
    except socket.error:
      s.close()
      return None
    select([], [s], [])
    return s

if __name__ == '__main__':
  IrSwitchApp().run()

