import logging

class ProcessManager:
  def __init__(self, ostools = None):
    self.log = logging.getLogger('ProcessManager')
    self.lastCommand = None

  def execute(self, command):
    if self._isNewCommand(command):
      self._stopAndClearLastCommand()

    if self._shouldRun(command):
      self._runAndSetCommand(command)

  def _stopAndClearLastCommand(self):
    self.lastCommand.stop()
    self.lastCommand = None

  def _runAndSetCommand(self, command):
    try:
      command.run()
      self.lastCommand = command
    except:
      pass

  def _isNewCommand(self, command):
   return (self.lastCommand is not None) and (self.lastCommand != command)

  def _shouldRun(self, command):
    if self.lastCommand is None:
      return True
    if not command.isRunning():
      self.log.warn('%s is shutdown or crashed - restarting' % command)
      return True
    return False
