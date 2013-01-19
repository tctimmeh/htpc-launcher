import subprocess

class OsTools:
  def runProcess(self, command):
    return subprocess.Popen(command, shell = True)
