import os, logging, logging.handlers
from irreader import IrReader

class IrSwitchApp:
  def __init__(self):
    self.startLogging()
    self.irReader = IrReader()

  def run(self):
    while True:
      code = self.irReader.getNextCode()
      self._processIrCode(code)

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
    pass

