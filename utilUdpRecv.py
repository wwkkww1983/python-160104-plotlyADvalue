import time
import socket

def procGetCommand(rcvstr):
	print rcvstr
	return

def procCommand(rcvstr):
	rcvstr = rcvstr.rstrip('\n')
	rcvstr = rcvstr.rstrip('\r')
#	cmds = rcvstr.split(",")
	procGetCommand(rcvstr)
	return

def recvCommand(cmdsock, rcvcmd):
	try:
		data,address = cmdsock.recvfrom(100)
	except socket.error:
		pass
	else:
		rcvcmd = rcvcmd + data
		return rcvcmd, True
	return rcvcmd, False

