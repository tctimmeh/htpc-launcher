import socket
from select import select

class SocketReader:
  def __init__(self, address):
    self.address = address
    self.socket = None

  def connect(self):
    if self.socket is not None:
      return
    self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
      self.socket.connect(self.address)
    except socket.error:
      self.disconnect()
      return
    select([], [self.socket], [])

  def read(self):
    readable, writable, exception = select([self.socket], [], [])
    data = self.socket.recv(1024)
    if not data:
      self.disconnect()
      return None
    return data

  def disconnect(self):
    if not self.socket:
      return
    self.socket.close()
    self.socket = None

