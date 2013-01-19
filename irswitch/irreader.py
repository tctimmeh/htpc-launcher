import logging
from socketreader import SocketReader

class IrReader:
  def __init__(self, socketReader = None):
    self.log = logging.getLogger('IrReader')
    self.socketReader = socketReader
    if not self.socketReader:
      self.socketReader = SocketReader('/var/run/lirc/lircd')

  def getNextCode(self):
    self.socketReader.connect()
    message = self.socketReader.read()

    self.log.debug('Read from lircd: %s', message.strip())

    return self._getKeyNameFromMessage(message)

  def _getKeyNameFromMessage(self, message):
    if not message:
      return None
    return message.split()[2]

