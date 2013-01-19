from irswitch.irreader import IrReader
from irswitch.socketreader import SocketReader
from mock import Mock

class TestIrReader:
  def setup_method(self, method):
    self.socketReader = Mock(SocketReader)
    self.socketReader.read.return_value = None
    self.reader = IrReader(self.socketReader)

  def testGettingCodeConnectsToSocket(self):
    self.reader.getNextCode()
    assert self.socketReader.connect.called

  def testGettingCodeReturnsCodeFromMessage(self):
    expected = 'KEY_SOMETHING'
    self.socketReader.read.return_value = '0x12345678 0 %s REMOTE_NAME\n' % expected

    code = self.reader.getNextCode()
    assert code == expected
