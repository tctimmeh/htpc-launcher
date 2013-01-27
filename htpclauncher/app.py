import time
from htpclauncher.config import Config
from htpclauncher.ostools import OsTools
import os, logging, logging.handlers
from irreader import IrReader, IrReaderError
from processManager import ProcessManager

from . import DEFAULT_CONF_FILE, DEFAULT_LOG_FILE

class HtpcLauncherApp:
  def __init__(self, ostools = None, config = None):
    self._startLogging()

    self.ostools = ostools
    if not self.ostools:
      self.ostools = OsTools()

    self.config = config
    if not self.config:
      self.config = Config()

    self._loadConfig()

    self.irReader = IrReader()
    self.processManager = ProcessManager()

  def run(self):
    try:
      self._processIrCode(self.config.getLaunchCommand())

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

  def _startFileLogging(self):
    formatter = logging.Formatter('%(asctime)s %(levelname)s - %(message)s')
    filePath = os.path.expanduser(DEFAULT_LOG_FILE)

    handler = logging.handlers.RotatingFileHandler(filePath, maxBytes = 1024000, backupCount = 5)
    handler.setFormatter(formatter)
    self.log.addHandler(handler)

  def _startStreamLogging(self):
    formatter = logging.Formatter('%(asctime)s %(levelname)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    self.log.addHandler(handler)

  def _startLogging(self):
    self.log = logging.getLogger()
    self.log.setLevel(logging.DEBUG)

    self._startStreamLogging()
    self._startFileLogging()

  def _loadConfig(self):
    self.log.info('Loading config file from home directory')
    configFile = self.ostools.openUserFile('.%s' % DEFAULT_CONF_FILE)

    if not configFile:
      self.log.info('Config not found in home directory; loading from system config')
      configFile = self.ostools.openSystemConfFile(DEFAULT_CONF_FILE)

    if not configFile:
      raise RuntimeError('Failed to find configuration file')
    self.config.load(configFile)

  def _processIrCode(self, code):
    command = self.config.getCommand(code)
    if not command:
      return
    self.processManager.execute(command)

def main():
  HtpcLauncherApp().run()

