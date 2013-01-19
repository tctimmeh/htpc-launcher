from irswitch.command import Command
from irswitch.ostools import OsTools
from mock import Mock

class TestCommand:
  def setup_method(self, method):
    self.ostools = Mock(OsTools)
    self.command = Command('something', ostools = self.ostools)

  def testCommandIsRun(self):
    self.command.run()
    self.ostools.runProcess.assert_called_with('something')
