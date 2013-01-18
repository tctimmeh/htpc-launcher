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
  def __init__(self, command, search, needsNine = False):
    self.command = command
    self.search = search
    self.needsNine = needsNine

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

    self._killChild()
    log.info('Waiting for process death')
    self.proc.wait()

  def focus(self):
    log.info('Focusing %s' % self.command)
    subprocess.call('wmctrl -a %s' % self.command, shell = True)
    
  def _killChild(self):
    log.info('Killing %s, pid = [%d]', self.command, self.proc.pid)
    pid = self._findPid()
    if not pid:
      log.error('Failed to find pid to kill - couldn\'t find running process')
      return

    killCmd = 'kill '
    if self.command.needsNine:
      killCmd += '-9 '
    killCmd += pid
    log.info('Running kill command: %s', killCmd)
    subprocess.call(killCmd, shell = True)

  def _findPid(self):
    log.info('Searching for Process with regex: %s', self.command.search)
    findProc = subprocess.Popen('ps -ef | grep -P "%s" | grep -v grep' % self.command.search, shell = True, stdout = subprocess.PIPE)
    findOut = findProc.communicate()[0]
    if not findOut:
      return None

    log.info('Found proccess: %s', findOut)
    return findOut.split()[1]

class IrSwitchApp(object):
  def __init__(self):
    self.lircSocket = None
    self.currentProcess = None

    self.commands = {
      'KEY_BLUE' : Command('steam', '.local/share/Steam/.+/steam', needsNine = True), 
      'KEY_YELLOW': Command('xbmc', 'xbmc.bin'),
    }

  def run(self):
    self.currentProcess = Process(self.commands['KEY_YELLOW'])
    self.currentProcess.start()

    while True:
      self._connectToLirc()
      if not self.lircSocket:
        time.sleep(1)
        continue
      
      readable, writable, exception = select([self.lircSocket], [], [])
      data = self.lircSocket.recv(1024)
      if not data:
        self._disconnectFromLirc()
        continue
      self._processLircMessage(data)

  def _runCommand(self, command):
    if command is None:
      return

    if (self.currentProcess) and (command is self.currentProcess.command):
      log.info('This process is already running')
      self.currentProcess.focus()
      return

    if self.currentProcess:
      self.currentProcess.stop()
      self.currentProcess = None

    self.currentProcess = Process(command)
    self.currentProcess.start()

  def _processLircMessage(self, data):
    keyName = data.strip().split()[2]
    log.info('Received IR key: %s', keyName)
    command = self.commands.get(keyName)
    self._runCommand(command)

  def _disconnectFromLirc(self):
    if not self.lircSocket:
      return

    self.lircSocket.close()
    self.lircSocket = None

  def _connectToLirc(self):
    if self.lircSocket is not None:
      return

    self.lircSocket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
      self.lircSocket.connect('/var/run/lirc/lircd')
    except socket.error:
      self._disconnectFromLirc()
      return
    select([], [self.lircSocket], [])

if __name__ == '__main__':
  try:
    IrSwitchApp().run()
  except KeyboardInterrupt:
    pass
  except:
    log.exception('Unhandled exception')

