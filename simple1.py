#!/usr/bin/env python
# encoding: utf-8

import dns.resolver
import os
import httplib
iplist = [] #定义域名IP列表变量
#appdomin = "www.baidu.com"  # 定义业务域名
appdomin = raw_input("plz input your appdomin:")  # 定义业务域名
def get_iplist (domin="") :
    try:
        A = dns.resolver.query(domin,'A')
    except Exception, e:
        print "dns resolver error :" + str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True

def checkip(ip):
    checkurl = ip + ":80"
    getcontent = ""
    httplib.socket.setdefaulttimeout(5)
    conn = httplib.HTTPConnection(checkurl)

    try:
        conn.request("GET","/",headers = {"Host": appdomin})

        r = conn.getresponse()
        getcontent = r.read(15)
        #print getcontent  #打印 getcontent
    finally:
        if getcontent == "<!DOCTYPE html>":
            print ip + "[OK]"
        else:
            print ip + "[Error]"

if __name__ == "__main__":
    if get_iplist(appdomin) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)
    else:
            print "dns resolver error"
