import threading
import sys
import os
import telnetlib
import getpass
import re

'''
Hello user,

NATRIX stands for "Network Automation Tools Reduce Ineffective Exchanges" and 
is also a refferece to the term "snake" from old latin.

Code author: 
 - Adrian Roata (github.com/adiroata)

"natrix.py" is a "module" in which I include most of the functions that 
are called from the main file.

The code is still a work in progress and comes with no warranty.
If you decide to use it in a production environment, you may do so at your own risk!

Regards.

'''


user = input("Username: ").encode()
password = getpass.getpass().encode()


########################################################################
# Session manager function
def open_telnet_session(ip):
    print("Executing job on host: "+ip)
    try:
        telnet = telnetlib.Telnet(ip)
        telnet.read_until(b'Username: ', 3)
        telnet.write(user + b'\n')
        telnet.read_until(b'Password: ', 3)
        telnet.write(password + b'\n')
        
        # Write commands here
        telnet.write(b'show ip arp vrf devnet | i FastEthernet0/1.20\n')
        
        # Exiting
        telnet.write(b'exit\n')
        output = telnet.read_until(b'exit', 5)
        
        # Write log
        data = open("TEMPFILES/output_file_"+ip, "w")
        data.write(output.decode())
        data.close

        print("Commands executed on host: " + str(ip))
    
    except:
        print("The host " + str(ip) + " is down!")


########################################################################
# Yield successive n-sized 
# chunks from l. 
def divide_chunks(l, n):     
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 


########################################################################
# Create and execute threads
def create_threads():
    # Specify chunks size to be executed at once
    chunck_size=3
    with open("loops.txt", "r") as ipfile:
        chunks_list=[]
        for line in ipfile:
            chunks_list.append(line.rstrip("\n"))
        
        chunks = list(divide_chunks(chunks_list, chunck_size))

        for chunk in chunks:
            threads = []
            for line in chunk:
                ip = line.strip()
                th = threading.Thread(target = open_telnet_session ,args = (ip,))
                threads.append(th)
                th.start()
            for thr in threads:
                thr.join()


########################################################################
# Filter raw output from 'show' command
def filter_output():   
    with open("loops.txt", "r") as loops:
        for loop in loops:
            loop = loop.strip()
            with open(f"TEMPFILES/clean_file_{loop}", "w") as f:
                try:
                    var=os.popen(f"grep 'Internet' TEMPFILES/output_file_{loop}").read()
                    f.write(var)
                except:
                    pass


########################################################################
# Formats the output to be ready for data extraction
def output_formater_arp(data):
    new_list=[]
    try:
        lines = re.split(" ", data)
        output=[] 
        for line in lines:
            if line != '':
                output.append(line)
        new_output = [i.split("\n", 1) for i in output]
        del new_output[0]
        for n in new_output:
            if n[0] != None:
                x = n[0]
                new_list.append(x)
        
        chunck_size=5
        chunks = list(divide_chunks(new_list, chunck_size))
        
        new_row = []
        for elem in chunks:
            if elem[1] == "-":
                pass
            else:
                new_row.append(elem[0])
        
        return new_row
    except:
        pass


# if __name__ == "__main__":
#         create_threads()
#         print ("Ending the program")