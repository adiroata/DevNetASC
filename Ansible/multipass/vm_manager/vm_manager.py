import argparse
import os

parser = argparse.ArgumentParser(description="Start, Stop & Delete VM's using multipass")
parser.add_argument("arg", type=str, help="Options: spawn, start, stop, delete")
arg=parser.parse_args()

def spawn():
    os.system("multipass launch -n server")
    os.system("multipass launch -n client1")
    os.system("multipass launch -n client2")
    os.system("multipass list")

def start():
    os.system("multipass start server")
    os.system("multipass start client1")
    os.system("multipass start client2")
    os.system("multipass list")

def stop():
    os.system("multipass stop server")
    os.system("multipass stop client1")
    os.system("multipass stop client2")
    os.system("multipass list")

def delete():
    os.system("multipass delete server")
    os.system("multipass delete client1")
    os.system("multipass delete client2")
    os.system("multipass purge")

if arg.arg == "spawn":
    spawn()
elif arg.arg == "start":
    start()
elif arg.arg == "stop":
    stop()
elif arg.arg == "delete":
    delete()
else:
    "Try -h for more informations."

