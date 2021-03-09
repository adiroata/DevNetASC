import threading
import sys
import os
import telnetlib
import time
import getpass

user = input("Username: ").encode()
password = getpass.getpass().encode()

timestamp = time.strftime("%d" + "-" + "%m" + "-" + "%Y" + "_" + "%H" + ":" + "%M")

def open_telnet(ip):
    print("Executing job on host: "+ip)
    try:
        telnet = telnetlib.Telnet(ip)
        telnet.read_until(b'Username: ', 3)
        telnet.write(user + b'\n')
        telnet.read_until(b'Password: ', 3)
        telnet.write(password + b'\n')
        telnet.write(b'terminal length 0\n')
        telnet.write(b'show interface description\n')
        # telnet.write(b'interface loopback 999\n')
        # telnet.write(b'description test\n')
        # telnet.write(b'end\n')
        telnet.write(b'exit\n')
        output = telnet.read_until(b'exit', 5)
        data = open("output_"+ip+"_"+timestamp, "w")
        data.write(output.decode())
        data.close

        print("Au fost executate comenzile pe hostul: " + str(ip))
    
    except:
        print("Hostul " + str(ip) + " e down!")
 
def create_threads():
    threads = []
    with open('hosts.txt','r') as ipfile:
        for line in ipfile:
            ip = line.strip()
            th = threading.Thread(target = open_telnet ,args = (ip,))
            threads.append(th)
            th.start()
        for thr in threads:
            thr.join()
 
if __name__ == "__main__":
        create_threads()
        print ("Exiting the program")