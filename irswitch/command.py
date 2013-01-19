from ostools import OsTools

class Command:
  def __init__(self, process, search = None, needsKill = False, ostools = None):
    self.process = process
    self.needsKill = needsKill

    self.ostools = ostools
    if not self.ostools:
      self.ostools = OsTools()

    self.search = search
    if not self.search:
      self.search = self.process

  def run(self):
    self.ostools.runProcess(self.process)

  def stop(self):
    pid = self.ostools.findPid(self.search)
    if not pid:
      return

    if self.needsKill:
      self.ostools.kill(pid)
    else:
      self.ostools.terminate(pid)
