from irswitch.command import Command
from irswitch.processManager import ProcessManager
from mock import Mock

class TestProcessManager:
  def setup_method(self, method):
    self.command = Mock(Command)
    self.processManager = ProcessManager()

  def testCommandIsRunWhenExecuted(self):
    self.processManager.execute(self.command)
    assert self.command.run.called

  def testPreviousCommandIsStoppedWhenStartingNewCommand(self):
    self.processManager.execute(self.command)
    self.processManager.execute(Mock(Command))
    assert self.command.stop.called
