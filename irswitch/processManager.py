class ProcessManager:
  def __init__(self):
    self.currentCommand = None

  def execute(self, command):
    if self.currentCommand:
      self.currentCommand.stop()

    command.run()
    self.currentCommand = command
