from ostools import OsTools

class Command:
  def __init__(self, process, search = None, ostools = None):
    self.process = process

    self.ostools = ostools
    if not self.ostools:
      self.ostools = OsTools()

    self.search = search
    if not self.search:
      self.search = self.process

  def run(self):
    pid = self.ostools.findPid(self.search)
    if not pid:
      self.ostools.runProcess(self.process)

  def stop(self):
    pid = self.ostools.findPid(self.search)
    if not pid:
      return
    self.ostools.kill(pid)
