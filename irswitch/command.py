from ostools import OsTools

class Command:
  def __init__(self, process, ostools = None):
    self.process = process
    self.ostools = ostools
    if not self.ostools:
      self.ostools = OsTools()

  def run(self):
    self.ostools.runProcess(self.process)
