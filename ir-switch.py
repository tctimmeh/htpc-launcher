#!/usr/bin/env python
import sys, time, subprocess, logging, logging.handlers
import socket
from select import select

log = logging.getLogger()
log.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
log.addHandler(handler)
handler = logging.handlers.RotatingFileHandler('ir-switch.log', maxBytes = 1024000, backupCount = 5)
handler.setFormatter(formatter)
log.addHandler(handler)

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
    log.info('Running %s', self.command)
    self.proc = subprocess.Popen(self.command.command, shell = True)
    log.info('PID = %d', self.proc.pid)

  def stop(self):
    if not self.proc:
      return

    log.info('Killing %s, pid = [%d]', self.command, self.proc.pid)
    pid = self._findPidToKill()
    if not pid:
      log.error('Failed to find pid to kill')
      return

    log.info('Killing pid %s', pid)
    subprocess.call('kill %s' % pid, shell = True)
    log.info('Waiting for process death')
    self.proc.wait()

  def _findPidToKill(self):
    log.info('Searching for Process to kill regex: %s', self.command.kill)
    findProc = subprocess.Popen('ps -ef | grep -P "%s" | grep -v grep' % self.command.kill, shell = True, stdout = subprocess.PIPE)
    findOut = findProc.communicate()[0]
    if not findOut:
      return None

    log.info('Found proccess to kill: %s', findOut)
    return findOut.split()[1]

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
          log.info('Received IR key: %s', keyName)
          command = self.commands.get(keyName)
          if (self.currentProcess) and (command is self.currentProcess.command):
            log.info('This process is already running')
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

