import logging
import os
import subprocess

class OsTools:
  def __init__(self):
    self.log = logging.getLogger('os')

  def runProcess(self, command):
    self.log.info('Running process: %s', command)
    return subprocess.Popen(command, shell = True)

  def findPids(self, regex):
    self.log.debug('Searching for Process with regex: %s', regex)
    findProc = subprocess.Popen('ps -ef | grep -P "%s" | grep -v grep' % regex, shell = True, stdout = subprocess.PIPE)
    stdout_data, stderr_data = findProc.communicate()
    lines = stdout_data.split('\n')

    pids = []
    for line in lines:
      line = line.strip()
      if not line:
        continue
      self.log.debug('Found proccess: %s', line)
      pids.append(line.split()[1])

    return pids

  def terminate(self, pid):
    self.log.debug('Terminating pid %s', str(pid))
    subprocess.call('kill %s' % str(pid), shell = True)

  def kill(self, pid):
    self.log.debug('Killing pid %s', str(pid))
    subprocess.call('kill -9 %s' % str(pid), shell = True)

  def focus(self, process):
    self.log.info('Setting focus to %s' % process)
    subprocess.call('wmctrl -a %s' % process, shell = True)

  def doesWindowExist(self, window):
    try:
      # grep will have an exit status of 1 if no rows are found, which leads check_output to raise an error
      subprocess.check_output("wmctrl -l|grep -i %s" % window, shell=True)
      return True
    except:
      return False

  def openFile(self, path):
    try:
      return open(path)
    except IOError as e:
      self.log.error('Failed to open file: %s', e)
      return None

  def openUserFile(self, fileName):
    return self.openFile(os.path.expanduser(os.path.join('~', fileName)))

  def openSystemConfFile(self, fileName):
    return self.openFile(os.path.join('/', 'etc', fileName))

  def getRotatingLogHandler(self, file, mode = 'a', maxBytes = 0, backupCount = 0, encoding = None, delay = 0):
    return logging.handlers.RotatingFileHandler(file, mode = mode, maxBytes = maxBytes, backupCount = backupCount,
      encoding = encoding, delay = delay)
