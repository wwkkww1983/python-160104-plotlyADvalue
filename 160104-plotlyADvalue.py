import plotly.plotly as py
import time
import datetime
from utilUdpRecv import recvCommand 
import socket

'''
v0.2 2016 Jan 04
  - fix bug > deleted from 1 not from 0
v0.1 2016 Jan 04
  - add udp communication to get AD value
  - add plotly_plot()
  - add main routine 
'''

def plotly_plot(xlist, ylist, addnum, grpTtl, filnam):
	if len(xlist) < addnum:
		return False

	py.plot({
		"data":[{ "x":xlist, "y":ylist }],
		"layout":{ "title": grpTtl }
	},filename=filnam
	,fileopt='extend'
	,privacy='public')

	return True

xlist = [0] * 0
ylist = [0] * 0

graphTitle = "graph as a function of time"
filename = "timegraph160104a"
datsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
datsock.setblocking(1000)
rcvcmd = ""

while True:
	datsock.sendto("data\n", ("192.168.10.4", 7000))
	rcvcmd,rcvd = recvCommand(datsock, rcvcmd)
	if rcvd == False or "\n" not in rcvcmd:	
		continue
	rcvcmd = rcvcmd.rstrip('\n')
	cmds = rcvcmd.split(",")
	yval = cmds[1]
	rcvcmd = ""
	print yval

	today = datetime.datetime.today()
	xdt = today.strftime("%Y-%m-%d %H:%M:%S")
	xlist.append(xdt)
	ylist.append(yval)
	time.sleep(3)
	
	res = plotly_plot(xlist, ylist, 50, graphTitle, filename)
	if res == False:
		continue

	print "added at " + str(xlist[1:])

	del xlist[0:]
	del ylist[0:]

