class ProcessManager:
  def __init__(self):
    self.lastCommand = None

  def execute(self, command):
    if self._lastCommandSet() and (not self._commandSameAsLastCommand(command)):
      self._stopAndClearLastCommand()

    if not self._lastCommandSet():
      self._runAndSetCommand(command)

  def _commandSameAsLastCommand(self, command):
    return command == self.lastCommand

  def _lastCommandSet(self):
    return self.lastCommand

  def _stopAndClearLastCommand(self):
    self.lastCommand.stop()
    self.lastCommand = None

  def _runAndSetCommand(self, command):
    command.run()
    self.lastCommand = command
