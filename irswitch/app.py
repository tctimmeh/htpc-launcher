import time
import os, logging, logging.handlers
from irreader import IrReader, IrReaderError
from command import Command
from processManager import ProcessManager

class IrSwitchApp:
  def __init__(self):
    self.startLogging()
    self.irReader = IrReader()
    self.processManager = ProcessManager()

    self.commands = {
      'KEY_YELLOW': Command('xbmc', search = 'xbmc.bin'),
      'KEY_BLUE': Command('steam', search = '.local/share/Steam/.+/steam', needsKill = True),
    }

  def run(self):
    try:
      while True:
        try:
          try:
            code = self.irReader.getNextCode()
          except IrReaderError:
            time.sleep(5)
            continue
          self._processIrCode(code)
        except KeyboardInterrupt:
          break
    except:
      self.log.exception('Unhandled exception')

  def startFileLogging(self):
    formatter = logging.Formatter('%(asctime)s %(levelname)s - %(message)s')
    homeDirectory = os.path.expanduser('~')
    filePath = os.path.join(homeDirectory, '.ir-switch.log')

    handler = logging.handlers.RotatingFileHandler(filePath, maxBytes = 1024000, backupCount = 5)
    handler.setFormatter(formatter)
    self.log.addHandler(handler)

  def startStreamLogging(self):
    formatter = logging.Formatter('%(asctime)s %(levelname)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    self.log.addHandler(handler)

  def startLogging(self):
    self.log = logging.getLogger()
    self.log.setLevel(logging.DEBUG)

    self.startStreamLogging()
    self.startFileLogging()

  def _processIrCode(self, code):
    command = self.commands[code]
    if not command:
      return
    self.processManager.execute(command)

