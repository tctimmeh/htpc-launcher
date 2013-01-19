import logging
import subprocess

class OsTools:
  def __init__(self):
    self.log = logging.getLogger('os')

  def runProcess(self, command):
    return subprocess.Popen(command, shell = True)

  def findPid(self, regex):
    self.log.debug('Searching for Process with regex: %s', regex)
    findProc = subprocess.Popen('ps -ef | grep -P "%s" | grep -v grep' % regex, shell = True, stdout = subprocess.PIPE)
    findOut = findProc.communicate()[0]
    if not findOut:
      return None

    self.log.debug('Found proccess: %s', findOut)
    return findOut.split()[1]

  def kill(self, pid):
    self.log.debug('Killing pid %s', str(pid))
    subprocess.call('kill %s' % str(pid), shell = True)
