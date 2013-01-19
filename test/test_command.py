from irswitch.command import Command
from irswitch.ostools import OsTools
from mock import Mock

class TestCommand:
  def setup_method(self, method):
    self.ostools = Mock(OsTools)
    self.pid = '1234'
    self.ostools.findPid.return_value = self.pid
    self.command = Command('something', search = 'whatever', ostools = self.ostools)

  def testCommandIsRun(self):
    self.ostools.findPid.return_value = None
    self.command.run()
    self.ostools.runProcess.assert_called_with('something')

  def testPidIsKilledWhenStopped(self):
    self.command.stop()
    self.ostools.terminate.assert_called_with(self.pid)

  def testNothingKilledWhenPreviousProcessNotRunning(self):
    self.ostools.findPid.return_value = None
    self.command.stop()
    assert not self.ostools.terminate.called
    assert not self.ostools.kill.called

  def testNothingStartedWhenProcessAlreadyRunning(self):
    pid = '1234'
    self.ostools.findPid.return_value = pid
    self.command.run()
    assert not self.ostools.runProcess.called

  def testCommandTerminatedWithSigKillIfOptionSet(self):
    self.command.needsKill = True
    self.command.stop()
    self.ostools.kill.assert_called_with(self.pid)
