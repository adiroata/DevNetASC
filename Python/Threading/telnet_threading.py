import threading
import sys
import os
import telnetlib
import time
import getpass

user = input("Username: ").encode()
password = getpass.getpass().encode()
p1=os.environ.get("ENABLE_PW1")
p2=os.environ.get("ENABLE_PW2")

timestamp = time.strftime("%d" + "-" + "%m" + "-" + "%Y" + "_" + "%H" + ":" + "%M")

# Session manager
def open_telnet(ip):
    print("Executing job on host: "+ip)
    try:
        telnet = telnetlib.Telnet(ip)
        telnet.read_until(b'Username: ', 3)
        telnet.write(user + b'\n')
        telnet.read_until(b'Password: ', 3)
        telnet.write(password + b'\n')
        
        # Raisecom specific
        if telnet.read_until(b'*>', 3):
            telnet.write(b'enable\n')
            if telnet.read_until(b'Password: ', 3):
                telnet.write(p1 + b'\n')
            elif telnet.read_until(b'Password: ', 3):
                telnet.write(p2 + b'\n')
        

        # Write commands here
        # telnet.write(b'terminal length 0\n')
        telnet.write(b'show interface port\n')
        
        # Exiting
        telnet.write(b'exit\n')
        output = telnet.read_until(b'exit', 5)
        
        # Write log
        data = open("output_"+ip+"_"+timestamp, "w")
        data.write(output.decode())
        data.close

        print("Commands executed on host: " + str(ip))
    
    except:
        print("The host " + str(ip) + " is down!")
 
# Yield successive n-sized 
# chunks from l. 
def divide_chunks(l, n):     
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 

# Create and execute threads
def create_threads():
    # Specify chunks size to be executed at once
    chunck_size=3
    with open("loops", "r") as ipfile:
        chunks_list=[]
        for line in ipfile:
            chunks_list.append(line.rstrip("\n"))
        

        chunks = list(divide_chunks(chunks_list, chunck_size))

        for chunk in chunks:
            threads = []
            for line in chunk:
                ip = line.strip()
                th = threading.Thread(target = open_telnet ,args = (ip,))
                threads.append(th)
                th.start()
            for thr in threads:
                thr.join()

            print("Done processing chunk !")
 
if __name__ == "__main__":
        create_threads()
        print ("Ending the program")