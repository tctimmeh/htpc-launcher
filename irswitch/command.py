import logging, time
from ostools import OsTools

class Command:
  def __init__(self, process, search = None, needsKill = False, ostools = None):
    self.log = logging.getLogger('Command')
    self.process = process
    self.needsKill = needsKill

    self.ostools = ostools
    if not self.ostools:
      self.ostools = OsTools()

    self.search = search
    if not self.search:
      self.search = self.process

  def __str__(self):
    return self.process

  def __eq__(self, other):
    return self.process == other.process

  def __ne__(self, other):
    return not self == other

  def run(self):
    if self.isRunning():
      self.ostools.focus(self.process)
      return

    self.log.info('Running %s' % self)
    self.ostools.runProcess(self.process)
    while not self.isRunning():
      time.sleep(0.5)

  def stop(self):
    pid = self.ostools.findPid(self.search)
    if not pid:
      return
    if self.needsKill:
      self.ostools.kill(pid)
    else:
      self.ostools.terminate(pid)

  def isRunning(self):
    pid = self.ostools.findPid(self.search)
    return pid is not None

