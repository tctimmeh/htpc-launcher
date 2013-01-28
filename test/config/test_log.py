from StringIO import StringIO
import os
from htpclauncher import DEFAULT_LOG_FILE
from htpclauncher.config import Config

class TestConfig:
  def setup_method(self, method):
    self.logPath = 'some/path'
    self.contents = StringIO('''
[log]
path = %s
    ''' % self.logPath)
    self.config = Config()
    self.config.load(self.contents)

  def testLogPathIsSetToUserHomeDirectoryIfNoneGiven(self):
    emptyConfig = StringIO('')
    self.config = Config()
    self.config.load(emptyConfig)
    assert self.config.getLogPath() == os.path.expanduser(os.path.join('~', '.' + DEFAULT_LOG_FILE))

  def testLogPathMatchesConfigured(self):
    assert self.config.getLogPath() == self.logPath
