import time
import os, logging, logging.handlers
from irreader import IrReader, IrReaderError
from command import Command

class IrSwitchApp:
  def __init__(self):
    self.startLogging()
    self.irReader = IrReader()

    self.commands = {
      'KEY_YELLOW': Command('xbmc'),
      'KEY_BLUE': Command('steam'),
    }

  def run(self):
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
#    self.startFileLogging()

  def _processIrCode(self, code):
    command = self.commands[code]
    if not command:
      return
    command.run()
    pass

