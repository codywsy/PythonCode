# -*- coding: utf-8 -*-

import dns.resolver
import os
import httplib

domain = "www.tianya.cn"
A = dns.resolver.query(domain, 'A')
for i in A.response.answer:
    for j in i.items:
        if isinstance(j,dns.rdtypes.IN.A.A) :
            print j.address
        elif isinstance(j,dns.rdtypes.ANY.CNAME.CNAME):
            print j.target

iplist=[]
appdomain="www.tianya.cn"

def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception as e:
        print "dns resolver error:"+str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            if isinstance(j, dns.rdtypes.IN.A.A):
                iplist.append(j.address)
    return True

def checkip(ip):
    checkurl=ip+":80"
    getcontent=""
    httplib.socket.setdefaulttimeout(5)
    conn=httplib.HTTPConnection(checkurl)

    try:
        conn.request("GET","/",headers={"Host":appdomain})
        r=conn.getresponse()
        getcontent=r.read(15)
    finally:
        if getcontent=="<!DOCTYPE html>":
            print ip+" [OK]"
        else:
            print ip+" [Error]"

if __name__ == "__main__":
    if get_iplist(appdomain) and len(appdomain) > 0:
        for ip in iplist:
            checkip(ip)
    else:
        print "dns resolver error."
    