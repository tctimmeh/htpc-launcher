from StringIO import StringIO
from htpclauncher.config import Config

class TestConfig:
  def setup_method(self, method):
    self.contents = StringIO('''
[startup]
launch = LAUNCH_KEY
    ''')
    self.config = Config()
    self.config.load(self.contents)

  def testAutoLaunchKeyIsLoaded(self):
    assert self.config.getLaunchCommand() == 'LAUNCH_KEY'

