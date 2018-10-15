# -*- coding: utf-8 -*-

import sys
import nmap

scan_row=[]
input_data="www.qq.com 80,3306,3310,22,1433,3389"
scan_row=input_data.split(" ")
if len(scan_row) != 2:
    print "Input errors, example \"www.qq.com 80,3306,3310,22,1433,3389\""
    sys.exit(0)
hosts=scan_row[0]
port=scan_row[1]

try:
    nm = nmap.PortScanner()
except Exception as e:
    print ('Nmap not found', str(e))
    sys.exit(0)
except:
    print ("Unexpected error:", sys.exc_info()[0])
    sys.exit(0)

try:
    nm.scan(hosts=hosts,arguments=' -v -sS -p '+port)
except Exception as e:
    print "Scan erro:" + str(e)

for host in nm.all_hosts():
    print '-'*20
    print 'Host: %s (%s)'%(host, nm[host].hostname())
    print 'State: %s' % nm[host].state()

    for proto in nm[host].all_protocols():
        print '-'*5
        print 'Protocol: %s' % proto

        lport = nm[host][proto].keys()
        lport.sort()
        for port in lport:
            print 'port: %s\tstate: %s' %(port, nm[host][proto][port]['state'])