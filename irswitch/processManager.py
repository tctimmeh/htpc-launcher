class ProcessManager:
  def __init__(self):
    self.currentCommand = None

  def execute(self, command):
    if self.currentCommand and (self.currentCommand != command):
      self.currentCommand.stop()
      self.currentCommand = None

    if not self.currentCommand:
      command.run()
      self.currentCommand = command
