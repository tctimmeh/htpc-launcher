from irswitch.command import Command
from irswitch.ostools import OsTools
from mock import Mock

class TestCommand:
  def setup_method(self, method):
    self.ostools = Mock(OsTools)
    self.command = Command('something', search = 'whatever', ostools = self.ostools)

  def testCommandIsRun(self):
    self.command.run()
    self.ostools.runProcess.assert_called_with('something')

  def testPidIsKilledWhenStopped(self):
    pid = '1234'
    self.ostools.findPid.return_value = pid
    self.command.stop()
    self.ostools.kill.assert_called_with(pid)

  def testNothingKilledWhenPreviousProcessNotRunning(self):
    self.ostools.findPid.return_value = None
    self.command.stop()
    assert not self.ostools.kill.called